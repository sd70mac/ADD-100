# Main Program goes here.

import os
import sys
import pie_in_the_sky
import menu


# I hope I'm doing this right.
# I know I need to call the functions in main() so that they actually run!
def main():
    """
    Main function to run the Pie in the Sky order process.
    No parameters are passed to this function, and it does not return any values."""
    pie_in_the_sky.clear_screen()
    customer_info = pie_in_the_sky.get_customer_info()
    print(f"Welcome To Pie In The Sky, {customer_info['name']}!")
    past_orders = pie_in_the_sky.get_past_orders(customer_info=customer_info)
    pie_in_the_sky.show_past_orders(past_orders=past_orders)
    order = (
        pie_in_the_sky.select_past_order(past_orders=past_orders)
        or pie_in_the_sky.get_order()
    )  # adding the 'or get_order()' fixed order.extend(selected_items) [Currently line 109]

    """ for category in CATEGORIES:
        available_items = get_available_items(category=category)
        selected_items = get_items_for_category(
            category=category, available_items=available_items
        )
        order.extend(selected_items)  # I have read about combining lists before.
        # Handy link: https://www.w3schools.com/python/ref_list_extend.asp
 """

    food_menu = menu.Menu("menu.txt")
    dessert_menu = menu.Menu("dessert_menu.txt")

    food_menu.menu_summary()
    dessert_menu.menu_summary()

    total = pie_in_the_sky.calculate_bill(order=order)
    pie_in_the_sky.print_bill(order=order, total=total)


## Run the main function when the file is executed
if __name__ == "__main__":
    main()
