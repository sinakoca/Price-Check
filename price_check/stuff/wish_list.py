from datetime import datetime

class WishList(object):
    def __init__(self):
        self.products = []
        self.created = datetime.now()
        self.last_modified = datetime.now()
    
    def add_product(self, product):
        self.products.append(product)
        self.last_modified = datetime.now()
    