# WAREHOUSE MANAGER PRO
### Warehouse Stock Manager app in Python, the 'Capstone 4' project in the HyperionDev DfE Software Engineering Bootcamp

This program can be used for inventory control, designed for a shoe manufacturer with warehouses in multiple countries. 
You can view stock (with line values), search stock, re-stock the line with the lowest stock on hand, and discount
the product line with the greatest stock on hand. 

#### Table of Contents
I'm not sure what you were expecting, but this is it!

### Installation
This is a Python script so will run in your favourite IDE

### Usage
From the main menu, the user is asked to select an option and press Enter:

![finalCapstone - main menu](https://user-images.githubusercontent.com/33696436/219976919-5b5aac54-ea28-482c-a9db-b9ea7d25d9e8.PNG)


To **Add a new shoe**, the user inputs the details attribute by attribute. 
Helper text at the bottom of the screen (shown) is replaced with error messages in red as user inputs are validated.

![finalCapstone - add a new shoe](https://user-images.githubusercontent.com/33696436/219977140-acb349ff-986b-4363-8752-8c8e4508e9df.PNG)


To see a table of all stock held, the user can either **view all inventory** or, to see the same information but also with
the total value of stock held per item/product line the user can **view stock values by item** (shown):

![finalCapstone - view values](https://user-images.githubusercontent.com/33696436/219977239-4dd6df54-c3e4-4f70-b528-89ab0e3760a7.PNG)


To **Re-stock the item with the lowest quantity**, the user is presented with the product line with the lowest level of held stock. 
They can then enter a quantity to increase this by, which is validated as a valid, positive, integer.
Or, they can enter '0' to return to the main menu without adding stock. In this case, a notification is displayed to confirm no changes.

![finalCapstone - restock](https://user-images.githubusercontent.com/33696436/219977387-71452a31-d952-4e2f-98e3-0e5be90ed366.PNG)


To **Show and/or discount the item with the highest quantity** of held stock, the user is first presented with the item details and
asked to enter a percentage to reduce the price by (if they would like the item to be 'on sale'). If they enter '0' they are returned
to the main menu without any changes being made. 

If the user *does* enter a percentage to discount the price by, they are shown the sale price and asked to confirm before the change is made.

![finalCapstone - discount](https://user-images.githubusercontent.com/33696436/219977508-7e86bdd1-0171-49b7-b0e8-9259512cbd40.PNG)


Finally, a user can **Search for an item** by entering the 8-digit SKU code for the product. The details are displayed if the item is stocked.

![finalCapstone - search](https://user-images.githubusercontent.com/33696436/219977537-db7af711-dfec-48c6-9236-947281336e5c.PNG)


### Credits
This program was written by James Brewer, working with a skeleton template file and project idea from HyperionDev.

Several websites were used to research ideas, and links are contained in the comments of the code where these apply.

A special thank you to the mentors/code reviewers - I hope you had as much fun reading all this as I had writing it. 
(Seriously though, thank you!)
