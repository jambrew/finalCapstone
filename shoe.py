'''This file is to define the shoe class'''
from tabulate import tabulate     # To make the output for str method easily readable


# ========The beginning of the class==========
class Shoe:

    # Initialise the instance, declaring what data types should be passed
    def __init__(self, country: str, code: str, product: str, cost: float, quantity=0):

        # Validate the arguments received
        assert len(code) == 8, 'Invalid SKU code - check data'
        assert cost >= 0, f'£{cost} not a valid cost - check data'
        assert quantity >= 0, f'{quantity} not valid quantity - check data'

        # Assign arguments to self object
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost / 100)     # Turns this into £ and p.
        self.quantity = int(quantity)       # This will always be integer

    # Getters for cost and quantity
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    # A method that creates a dictionary - for writing to csv
    def make_dictionary(self):
        return {
            'Country': self.country,
            'Code': self.code,
            'Product': self.product,
            # Turning into pence for file-writing
            'Cost': int(self.cost * 100),
            'Quantity': self.quantity
        }

# Sets the output that represents the object when called directly
    def __repr__(self) -> str:
        return f"Shoe('{self.country}', {self.code}, {self.product}, {self.cost}, {self.quantity})"

    # Return a tabulate table for the object when instance is printed
    def __str__(self):
        list_from_object = [[self.country, self.code,
                            self.product, self.cost, self.quantity],
                            ['', '', '', '', '', '']]   # Blank list for padding
        return tabulate(list_from_object, headers=['Country', 'Code', 'Product', 'Cost', 'Quantity'], tablefmt="fancy_outline", floatfmt=".2f")
