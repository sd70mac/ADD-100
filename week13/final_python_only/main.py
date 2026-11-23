import pie_in_the_sky
import menu

# CHANGE LOG:
# - Replaced the placeholder/hard-coded order flow with menu selection and past-order support.
# - Removed the old hard-coded "Cheddar Potato, Shepherds', Lemonade" order path.
# - Updated bill printing to pass the customer name into the order-save logic.

def main():
    """Run the Pie in the Sky kiosk."""
    pie_in_the_sky.clear_screen()
    customer_info = pie_in_the_sky.get_customer_info()
    print(f"Welcome To Pie In The Sky, {customer_info['name']}!")

    past_orders = pie_in_the_sky.get_past_orders(customer_info=customer_info)
    pie_in_the_sky.show_past_orders(past_orders=past_orders)
    order = pie_in_the_sky.select_past_order(past_orders=past_orders)
    if not order:
        food_menu = menu.Menu(pie_in_the_sky.MENU_FILE)
        dessert_menu = menu.Menu(pie_in_the_sky.DESSERT_MENU_FILE)
        print("\n************************* Menu *************************")
        food_menu.menu_summary()
        dessert_menu.menu_summary()
        print("\n*********************** Selections ***********************")
        order = pie_in_the_sky.get_order()

    total = pie_in_the_sky.calculate_bill(order=order)
    pie_in_the_sky.print_bill(
        order=order,
        total=total,
        customer_name=customer_info["name"],
    )


## Run the main function when the file is executed
if __name__ == "__main__":
    main()
