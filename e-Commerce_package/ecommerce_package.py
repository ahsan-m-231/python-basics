class Item:
    def __init__(self, item_id, item_desc, item_quantity, item_price):
        self.item_id = item_id
        self.item_desc = item_desc
        self.item_quantity = item_quantity
        self.item_price = item_price


class ShoppingCart:
    Item_2 = Item(101, "", 5, 3)
