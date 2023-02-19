# Importing libraries
import csv      # For handling csv file (to instantiate object from lines)
from tabulate import tabulate     # To output the data in an easy to read manner
import shoe     # The file with the Shoe class
from os import system, name     # import only system from os - for clear screen
from colorama import Fore

# Variables to shorten calls for colour change
cyan = Fore.CYAN
magenta = Fore.MAGENTA
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

# This object and list will hold details of newly captured shoe data
new_shoe_instance = shoe.Shoe(
    'new-shoe', '12345678', 'This is a new shoe', 0, 0)
new_shoe_details = [''] * 5


# ==========Functions outside the class==============

# Function to clear screen from https://www.geeksforgeeks.org/clear-screen-python/
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Function to append the inventory file with a newly captured shoe


# ==== Function to add a new object to the end of the inventory.txt file
def append_the_inventory_file():
    # Try to open the file and append the new shoe
    try:
        with open('inventory.txt', 'a', encoding='utf-8') as f:
            # Note that it writes the price as an integer in pence
            f.write(f'\n{new_shoe_instance.country},{new_shoe_instance.code},{new_shoe_instance.product},{int(new_shoe_instance.cost * 100)},{new_shoe_instance.quantity}')
    # If file not found, return 1 as an error
    except FileNotFoundError:
        return 1
    # If successful, simply return
    else:
        return


# ===== Function to re-write the whole inventory file
def overwrite_inventory_file():
    with open('inventory.txt', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Country', 'Code', 'Product', 'Cost', 'Quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        # Calls the method to convert each instance to dictionary and writes line
        for object in shoe_list:
            writer.writerow(object.make_dictionary())
    return


# Function to read the inventory file and create shoe objects from it
# Researched from https://realpython.com/python-csv/
def read_shoes_data():

    try:
        # Try to open the file
        inv_file = open('inventory.txt', 'r', encoding='utf-8')

    except FileNotFoundError:
        # If file not found, return an error to the main
        return 1, 'Error: The inventory.txt file does not exist in the directory'

    else:
        # If file is found, read the inventory file and create shoe items from it
        try:
            create_items_from_csv_file(inv_file)

        # If any of the data is not valid, return the error to main menu
        # The assertion msgs are defined in the class
        except AssertionError as msg:
            inv_file.close()
            return 1, msg
        else:
            inv_file.close()

    return 0, 'The file has been read successfully'


# ===== Function to create the instances
def create_items_from_csv_file(inv_file):
    global shoe_list

    # use the inventory file to create a list of dictionaries
    file_contents = csv.DictReader(inv_file)
    inventory = list(file_contents)

    # Clear the shoe list
    shoe_list = []

    # For each dictionary in list, instantiate a Shoe object passing
    # the values for each key in the dictionary and add to shoe_list
    for item in inventory:
        shoe_list.append(
            shoe.Shoe(
                country=item.get('Country'),
                code=item.get('Code'),
                product=item.get('Product'),
                cost=float(item.get('Cost')),
                quantity=float(item.get('Quantity'))
            )
        )

    return


# ==== Check file has been read (before running menu selections)
def check_file_has_been_read(function_to_run):
    global shoe_list
    '''
    This function is to be run before each other menu option function
    (apart from the 'read inventory file' function). It's to check 
    whether the inventory file has already been read. If not, it reads it
    and outputs either a success notification, in which case the menu option
    function proceeds, or it fails and the error is presented to the user at
    the main menu.
    '''
    # First, check whether the shoe_list is empty
    if shoe_list == []:
        # If so, run the function to read the inventory file
        notification_type, notification = read_shoes_data()

    # If already/once data in the shoe_list, run the user-chosen function
    notification_type, notification = function_to_run()

    return notification_type, notification


# ==== Capture shoes function - works together with 'add a new shoe' function
def capture_shoes(active_field, error_msg=""):
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    clear()
    print(f'''{cyan}
            ╔═════════════════════════════════════════════╗
            ║            Warehouse Manager Pro            ║
            ║         ───────────────────────────         ║
            ║              {magenta} ADD A NEW SHOE {cyan}               ║
            ║                                             ║
            ║ Fill out the details of the new shoe below  ║
            ║                                             ║
            ╚══════════════╤══════════════════════════════╝
                  Country: │ {new_shoe_details[0]}
            ───────────────┼───────────────────────────────
                 SKU Code: │ {new_shoe_details[1]}
            ───────────────┼───────────────────────────────
                  Product: │ {new_shoe_details[2]}
            ───────────────┼───────────────────────────────
                     Cost: │ £{new_shoe_details[3]}
            ───────────────┼───────────────────────────────
                 Quantity: │ {new_shoe_details[4]}
            ═══════════════╧═══════════════════════════════''')

    # Gets the input for country field
    if active_field == "country":
        print(f" {magenta}            Enter the country where stock is held")
        print(f" {red}            {error_msg}                     ")
        field_output = input(
            f"\033[10f {magenta}                 Country: {cyan}│ {magenta}")
        field_output = field_output.capitalize()
    # Gets the input for sku code field
    elif active_field == "code":
        print(f" {magenta}            Enter the SKU code for the item")
        print(f" {red}            {error_msg}                     ")
        field_output = input(
            f"\033[12f {magenta}                SKU Code: {cyan}│ {magenta}")
    # Gets input for product name
    elif active_field == "product":
        print(f" {magenta}            Enter the product name")
        print(f" {red}            {error_msg}                     ")
        field_output = input(
            f"\033[14f {magenta}                 Product: {cyan}│ {magenta}")
    # Gets input for unit cost
    elif active_field == "cost":
        print(f" {magenta}            Enter the unit cost in GBP")
        print(f" {red}            {error_msg}                     ")
        field_output = input(
            f"\033[16f {magenta}                    Cost: {cyan}│ {magenta}£")
    # Gets input for quantity field
    elif active_field == "quantity":
        print(f" {magenta}            Enter the quantity on hand")
        print(f" {red}            {error_msg}                     ")
        field_output = input(
            f"\033[18f {magenta}                Quantity: {cyan}│ {magenta}")
    # Send the user input back to the main program
    return active_field, field_output


# ==== Add a new shoe function
def add_a_new_shoe():

    # Access the global variables
    global new_shoe_instance
    global new_shoe_details
    global shoe_list

    # Run the capture shoes function which works in conjunction with this function
    completed_field, new_shoe_details[0] = capture_shoes('country')

    while True:
        if completed_field == 'country':
            # If comma in field, or if less than 3 characters, loop round with error
            if ',' in new_shoe_details[0]:
                new_shoe_details[0] = ""
                completed_field, new_shoe_details[1] = capture_shoes(
                    'country', 'Field cannot contain comma \',\'')
                continue
            elif len(new_shoe_details[0]) < 3:
                new_shoe_details[0] = ""
                completed_field, new_shoe_details[0] = capture_shoes(
                    'country', 'Field must contain at least 3 characters')
                continue
            # If ok, continue
            else:
                completed_field, new_shoe_details[1] = capture_shoes(
                    'code')

        elif completed_field == 'code':

            # Try to use the SKU code as a value in the object to validate
            if len(new_shoe_details[1]) != 8:
                new_shoe_details[1] = ''
                completed_field, new_shoe_details[1] = capture_shoes(
                    'code', 'Error: SKUs must be 8 digits')
                continue

            # If all ok
            else:
                completed_field, new_shoe_details[2] = capture_shoes('product')

        elif completed_field == 'product':
            # If comma in field, or if less than 3 characters, loop round with error
            if ',' in new_shoe_details[2]:
                new_shoe_details[2] = ""
                completed_field, new_shoe_details[2] = capture_shoes(
                    'product', 'Field cannot contain comma \',\'')
                continue
            elif len(new_shoe_details[2]) < 3:
                new_shoe_details[2] = ""
                completed_field, new_shoe_details[2] = capture_shoes(
                    'product', 'Field must contain at least 3 characters')
                continue
            # If ok, continue
            else:
                completed_field, new_shoe_details[3] = capture_shoes(
                    'cost')

        elif completed_field == 'cost':
            # Try to cast the number to a float to validate
            try:
                new_shoe_details[3] = float(new_shoe_details[3])

            # If not a number, loop round to try again showing an error
            except ValueError:
                new_shoe_details[3] = ''
                completed_field, new_shoe_details[3] = capture_shoes(
                    'cost', 'Error: Must be a valid number')
                continue

            # If all ok
            else:
                completed_field, new_shoe_details[4] = capture_shoes(
                    'quantity')

        elif completed_field == 'quantity':
            # Try to cast the number to an int to validate
            try:
                new_shoe_details[4] = int(new_shoe_details[4])

            # If not a valid int, loop round to try again showing an error
            except ValueError:
                new_shoe_details[4] = ''
                completed_field, new_shoe_details[4] = capture_shoes(
                    'quantity', 'Error: Must be a valid number')
                continue

            # If all ok, create the instance and try to append to the inventory.txt file
            else:
                new_shoe_instance = shoe.Shoe(
                    new_shoe_details[0],    # Country
                    new_shoe_details[1],    # Code
                    new_shoe_details[2],    # Product
                    float(new_shoe_details[3]),  # Cost in £
                    int(new_shoe_details[4])     # Quantity
                )
                append_attempt_result = append_the_inventory_file()

                # If the result was unsuccessful, return error
                if append_attempt_result == 1:
                    return 1, 'Error - Inventory file not found, item not captured'

                # If successful, append the new shoe instance to inventory list
                else:
                    shoe_list.append(new_shoe_instance)
                    return 0, 'Success! Your new shoe has been added'


# ==== Create a list from an object instance (used to pass to tabulate)
def list_from_shoe_instance(object):
    list_of_shoe_instance = [
        object.country,
        object.code,
        object.product,
        float(object.cost),
        int(object.quantity)
    ]
    return list_of_shoe_instance


# ==== Get the value of an item from the instance, in £
def add_item_value_to_list_from_instance(object):
    # Start with the list as with the function above
    list_of_shoe_instance = list_from_shoe_instance(object)
    # Append the total value of stock for that item to list
    list_of_shoe_instance.append(
        float(object.cost) * int(object.quantity))
    return list_of_shoe_instance


# === View all the shoes function
def view_all():

    clear()
    # Use tabulate to print a table of all stock items
    print(tabulate([list_from_shoe_instance(i) for i in shoe_list], headers=[
          'Country', 'SKU Code', 'Product', 'Cost £', 'Quantity'], tablefmt="fancy_outline", floatfmt=".2f"))

    # Using a variable that's not called just to get user input to return to menu
    return_to_menu = input('Press \'Enter\' to go back the main menu: ')

    # No need for a notification message when returning to main menu
    return 0, ''


# === Find the item with lowest quantity stock
def find_item_with_lowest_quantity_stock():

    # Researched: https://pythonistaplanet.com/max-and-min-of-an-attribute-in-a-list-of-objects/?utm_content=cmp-true
    lowest_stock_item = min(shoe_list, key=lambda x: x.quantity)
    return lowest_stock_item


# ===== Re-stocks the shoe with the lowest quantity stock
def re_stock():
    global shoe_list

    # First find the item with lowest stock, and pass object to variable
    lowest_stock_item = find_item_with_lowest_quantity_stock()

    clear()
    # Print out the screen for the user, with the
    print(f'''{cyan}
            ╔═════════════════════════════════════════════╗
            ║            Warehouse Manager Pro            ║
            ║         ───────────────────────────         ║
            ║              {magenta} RE-STOCK A SHOE {cyan}              ║
            ║                                             ║
            ║ Add the additional stock or enter 0 to exit ║
            ║                                             ║
            ╚══════════════╤══════════════════════════════╝
                  Country: │ {lowest_stock_item.country}
            ───────────────┼───────────────────────────────
                 SKU Code: │ {lowest_stock_item.code}
            ───────────────┼───────────────────────────────
                  Product: │ {lowest_stock_item.product}
            ───────────────┼───────────────────────────────
                     Cost: │ £{lowest_stock_item.get_cost():.2f}
            ───────────────┼───────────────────────────────
                 Quantity: │ 
            ═══════════════╧═══════════════════════════════''')

    # Loop to take the new stock figure to add
    while True:
        try:
            additional_stock = int(input(
                f"\033[2F                {magenta} Quantity: {cyan}│ {lowest_stock_item.quantity}{magenta} + "))
        # If not a valid integer
        except ValueError:
            print(
                f"\033[B    {red}         Invalid quantity, must be a whole number")
            continue
        else:
            if additional_stock < 0:
                print(
                    f"\033[B    {red}         Quantity cannot be negative number")
                continue
            # If all good, exit the loop
            else:
                break

    # If 0 stock to be added, exit to main menu with comment notification
    if additional_stock == 0:
        return 2, 'No new stock was added'

    # Update the quantity of the item (which updates the original object in shoe_list)
    lowest_stock_item.quantity += additional_stock

    # Overwrite the inventory.txt file
    try:
        overwrite_inventory_file()
    except FileNotFoundError:
        return 1, 'The inventory file could not be updated'
    else:
        return 0, 'Stock level successfully updated!'


# ===== Search for a shoe function - displays details of the shoe
def search_shoe():

    clear()
    print(f'''{cyan}
            ╔═════════════════════════════════════════════╗
            ║            Warehouse Manager Pro            ║
            ║         ───────────────────────────         ║
            ║             {magenta} SEARCH FOR A SHOE {cyan}             ║
            ║                                             ║
            ║  Enter the SKU code of the shoe: ________   ║
            ║                                             ║
            ╚═════════════════════════════════════════════╝''')

    # Loop to get a valid SKU
    while True:
        sku_to_search = input(f'\033[7;48H{magenta}        \033[8D')
        print(f'\033[2B\033[K')     # Moves curser to under the box

        try:
            # Check it's 8 digits long
            assert len(sku_to_search) == 8
        # If not, loop round to take another
        except AssertionError:
            print(f'{red}             Invalid code - must be 8 digits{cyan}')
            continue

        # Search for shoe with matching SKU code
        found_shoe = False
        for index, shoe in enumerate(shoe_list):
            if shoe.code == sku_to_search:
                print()
                # Prints the str attribute of the shoe if found
                print(f"{magenta}{shoe_list[index]}")
                found_shoe = True
                break       # Break out of the loop -- successful

        # If not found, inform user and loop to take another code
        if found_shoe == False:
            print(f'{red}             Invalid code - not found         {cyan}')
            continue
        # If the shoe was found and printed, break the loop
        else:
            break

    print(f'''{cyan}

            ═══════════════════════════════════════════════''')

    # Ask user to press Enter to return to main menu
    return_to_main_menu = input(
        f'{cyan}             Press \'Enter\' to return to the main menu')
    return 0, ''


def value_per_item():

    clear()
    # Use tabulate to print a table of all stock items
    print(tabulate([add_item_value_to_list_from_instance(i) for i in shoe_list], headers=[
          'Country', 'SKU Code', 'Product', 'Cost £', 'Quantity', 'Total Stock Value £'], tablefmt="fancy_outline", floatfmt=".2f"))

    # Using a variable that's not called just to get user input to return to menu
    return_to_menu = input('Press \'Enter\' to go back the main menu: ')

    # No need for a notification message when returning to main menu
    return 0, ''


# === Find the item with highest quantity stock
def find_item_with_highest_quantity_stock():

    # Researched: https://pythonistaplanet.com/max-and-min-of-an-attribute-in-a-list-of-objects/?utm_content=cmp-true
    highest_stock_item = max(shoe_list, key=lambda x: x.quantity)
    return highest_stock_item


def highest_qty():
    global shoe_list

    # First find the item with highest stock, and pass object to variable
    highest_stock_item = find_item_with_highest_quantity_stock()

    clear()
    # Print out the screen for the user, with the
    print(f'''{cyan}
            ╔═════════════════════════════════════════════╗
            ║            Warehouse Manager Pro            ║
            ║         ───────────────────────────         ║
            ║              {magenta} DISCOUNT A SHOE {cyan}              ║
            ║                                             ║
            ║ The item with the highest stock value is    ║
            ║ listed below.                               ║
            ║                                             ║
            ║ Enter the % amount to discount the shoe by, ║
            ║ or enter '0' to return to the main menu.    ║
            ║                                             ║
            ╚══════════════╤══════════════════════════════╝
                  Country: │ {highest_stock_item.country}
            ───────────────┼───────────────────────────────
                 SKU Code: │ {highest_stock_item.code}
            ───────────────┼───────────────────────────────
                  Product: │ {highest_stock_item.product}
            ───────────────┼───────────────────────────────
                     Cost: │ 
            ───────────────┼───────────────────────────────
                 Quantity: │ {highest_stock_item.quantity}
            ═══════════════╧═══════════════════════════════''')

    # Loop to take the new stock figure to add
    while True:
        try:
            discount_rate = int(input(
                f"\033[4F                    {magenta} Cost: {cyan}│ £{highest_stock_item.cost}{magenta} less    % \033[5D"))
        # If not a valid integer
        except ValueError:
            print(
                f"\033[B    {red}         Invalid entry, must be a whole number")
            continue
        else:
            if discount_rate < 0:
                print(
                    f"\033[B    {red}         Cannot be negative percentage             ")
                continue
            elif discount_rate > 100:
                print(
                    f"\033[B    {red}         Cannot discount more than 100%             ")
            # If all good, exit the loop
            else:
                break

    # If no discount amount entered, exit to main menu with comment notification
    if discount_rate == 0:
        return 2, 'No discount was applied'

    # Variable to store the sale price
    sale_price = round(highest_stock_item.cost *
                       (1 - (discount_rate / 100)), 2)

    # Confirm with the user they want the price to be discounted
    print('\033[B')
    while True:
        confirm_discount = input(
            f"    {yellow}         Sale price will be {magenta}£{sale_price:.2f}{yellow}. Confirm 'y' or 'n'? : ")

        # User doesn't confirm - abort the discounting!
        if confirm_discount.lower() == 'n':
            return 2, 'No discount was applied'

        # Yes! User wants to discount...
        elif confirm_discount.lower() == 'y':
            # Update the price & sale status of the item (which updates the original object in shoe_list)
            highest_stock_item.cost = sale_price

            # Overwrite the inventory.txt file
            try:
                overwrite_inventory_file()
            except FileNotFoundError:
                return 1, 'The inventory file could not be updated'
            else:
                return 0, 'Discount has been applied successfully!'

        else:
            print(
                f'{red}             Invalid selection. Enter \'y\' or \'n\'\033[F\033[k')


# ==========Main Menu=============
def main(notification_type=None, notification=''):

    while True:
        clear()

        print(f'''{cyan}
                
            ╔═════════════════════════════════════════════╗
            ║            Warehouse Manager Pro            ║
            ║         ───────────────────────────         ║
            ║                 {magenta} MAIN MENU {cyan}                 ║
            ║                                             ║
            ║  Select one of the following options below  ║
            ║                                             ║
            ╚═════════════════╤═══════════════════════════╝
                            r │ Read inventory file
                            a │ Add a new shoe
                           va │ View all inventory
                           vv │ View stock values by item
                           rs │ Re-stock an item
                              │   with the lowest quantity
                           hq │ Show/discount item with
                              │   the highest quantity
                            s │ Search for an item
                            e │ Exit
            ──────────────────┴────────────────────────────

            ═══════════════════════════════════════════════''')

        # Print any notifications
        if notification_type == 0:      # Green for success
            print(f'            {green} {notification}', end='')
        elif notification_type == 1:        # Red for error
            print(f'            {red} {notification}', end='')
        elif notification_type == 2:        # Yellow for information
            print(f'            {yellow} {notification}', end='')

        # === Get the menu selection from the user
        menu_option = input(f'\033[2F {magenta}           : ')

        if menu_option.lower() == 'r':
            notification_type, notification = read_shoes_data()
            continue

        elif menu_option.lower() == 'a':
            # Pass the call to function to add shoe to the function to
            # check whether the inventory file needs to be read first
            notification_type, notification = check_file_has_been_read(
                add_a_new_shoe)
            continue

        elif menu_option.lower() == 'va':
            # Pass the call to function to add shoe to the function to
            # check whether the inventory file needs to be read first
            notification_type, notification = check_file_has_been_read(
                view_all)
            continue

        elif menu_option.lower() == 'rs':
            # Pass the call to function to add shoe to the function to
            # check whether the inventory file needs to be read first
            notification_type, notification = check_file_has_been_read(
                re_stock)
            continue

        elif menu_option.lower() == 's':
            # Pass the call to function to add shoe to the function to
            # check whether the inventory file needs to be read first
            notification_type, notification = check_file_has_been_read(
                search_shoe)
            continue

        elif menu_option.lower() == 'vv':
            # Pass the call to function to add shoe to the function to
            # check whether the inventory file needs to be read first
            notification_type, notification = check_file_has_been_read(
                value_per_item)
            continue

        elif menu_option.lower() == 'hq':
            # Pass the call to function to add shoe to the function to
            # check whether the inventory file needs to be read first
            notification_type, notification = check_file_has_been_read(
                highest_qty)
            continue

        elif menu_option.lower() == 'e':
            print(
                f'        {green} Goodbye! Thinking of taking a break now? ... Just do it! {Fore.RESET}')
            return

        # If invalid entry by user
        else:
            notification_type, notification = 1, 'Invalid selection, please try again'
            continue


# Call to main function
main()
