import random

import streamlit as st

import menu
import pie_in_the_sky


# CHANGE LOG - CLI to Streamlit:
# - Replaced clear_screen(), input(), print(), and sys.exit() kiosk flow with Streamlit widgets.
# - Replaced the CLI menu/selection/receipt screens with browser sections and session state.
# - Replaced the old hard-coded "Cheddar Potato, Shepherds', Lemonade" order path.
# - Reused Menu parsing, menu-price lookup, tax rates, and file-saving helpers.
# - Retained customer-name input, past-order support, quantities, drink add-ons, and tax summary.


st.set_page_config(
    page_title="Pie in the Sky",
    page_icon="PI",
    layout="wide",
)


ENTREE_CATEGORIES = (
    "Pies",
    "Other Entrees",
    "Soups",
    "Sandwiches",
    "Pastas",
)


def quantity_selections(category):
    """Display quantity controls for one menu category."""
    items = pie_in_the_sky.get_available_items(category)
    selections = st.multiselect(category, items, key=f"select_{category}")

    selected_items = []
    for item in selections:
        quantity = st.number_input(
            f"{item} quantity",
            min_value=1,
            max_value=20,
            value=1,
            step=1,
            key=f"quantity_{category}_{item}",
        )
        selected_items.extend([item] * quantity)
    return selected_items


def build_order(customer_name):
    """Build an order from Streamlit widgets and saved past orders."""
    order = []

    past_orders = pie_in_the_sky.get_past_orders(
        customer_info={"name": customer_name}
    )
    if past_orders:
        st.subheader("Past Orders")
        labels = [
            ", ".join(str(item) for item in past_order)
            for past_order in past_orders
        ]
        choice = st.selectbox(
            "Reorder a saved order",
            ["Start a new order"] + labels,
        )
        if choice != "Start a new order":
            index = labels.index(choice)
            return past_orders[index]

    st.subheader("Appetizers")
    order.extend(quantity_selections("Appetizers"))

    st.subheader("Entrees")
    for category in ENTREE_CATEGORIES:
        order.extend(quantity_selections(category))

    st.subheader("Desserts")
    dessert_menu = menu.Menu(pie_in_the_sky.DESSERT_MENU_FILE)
    dessert_items = dessert_menu.get_menu().get("Pies", [])
    other_dessert_items = dessert_menu.get_menu().get("Other Desserts", [])

    for label, items in (
        ("Dessert Pies", dessert_items),
        ("Other Desserts", other_dessert_items),
    ):
        selections = st.multiselect(label, items, key=f"select_{label}")
        for item in selections:
            quantity = st.number_input(
                f"{item} quantity",
                min_value=1,
                max_value=20,
                value=1,
                step=1,
                key=f"quantity_dessert_{item}",
            )
            order.extend([item] * quantity)

    st.subheader("Drinks")
    drinks = quantity_selections("Drinks")
    for drink_index, drink in enumerate(drinks):
        if drink in ("Tea", "Coffee", "Decaf"):
            milk = st.checkbox(f"{drink}: Add milk", key=f"milk_{drink}_{drink_index}")
            sugar = st.checkbox(f"{drink}: Add sugar", key=f"sugar_{drink}_{drink_index}")
            addons = []
            if milk:
                addons.append("milk")
            if sugar:
                addons.append("sugar")
            if addons:
                drink = f"{drink} with {' and '.join(addons)}"
        order.append(drink)

    return order


def main():
    """Run the Pie in the Sky Streamlit application."""
    st.title("Pie in the Sky Ordering Kiosk")

    customer_name = st.text_input("Customer Name", value="Guest")
    customer_name = customer_name.strip().title() or "Guest"

    with st.expander("View Menu", expanded=False):
        food_menu = menu.Menu(pie_in_the_sky.MENU_FILE)
        dessert_menu = menu.Menu(pie_in_the_sky.DESSERT_MENU_FILE)
        st.write("**Food Menu**")
        for category, items in food_menu.get_menu().items():
            st.write(f"**{category}**")
            st.write(", ".join(items))
        st.write("**Dessert Menu**")
        for category, items in dessert_menu.get_menu().items():
            st.write(f"**{category}**")
            st.write(", ".join(items))

    order = build_order(customer_name)

    st.subheader("Full Order")
    if order:
        for item in order:
            st.write(f"- {item}")
    else:
        st.info("No items selected yet.")

    subtotal = pie_in_the_sky.calculate_bill(order=order)
    tax = round(subtotal * pie_in_the_sky.SALES_TAX_RATE, 2)
    grand_total = round(subtotal + tax, 2)

    st.write(f"**Subtotal:** ${subtotal:.2f}")
    st.write("**Woodstock, Illinois Sales Tax:** 8.75%")
    st.write(f"**Total:** ${grand_total:.2f}")

    if st.button("Place Order", type="primary", disabled=not order):
        order_number = random.randint(1000, 9999)
        st.success(f"Your order number is: {order_number}")
        pie_in_the_sky.open_order_file(order, grand_total)
        pie_in_the_sky.save_frequent_order(customer_name, order)
        st.balloons()


if __name__ == "__main__":
    main()
