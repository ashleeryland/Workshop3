_author__ = 'jc260183'

def number_items():
    items_shipped = int(input("Please enter the amount of items to be shipped: "))
    if items_shipped < 0:
        print("invalid number of items")
    print(items_shipped)


def shipping_cost(number_items):
    shipping_cost = number_items * 8.5
    print("$", shipping_cost)
