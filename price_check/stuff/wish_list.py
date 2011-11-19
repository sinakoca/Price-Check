from datetime import datetime

class WishList(object):
    def __init__(self):
        self.products = []
        self.created = datetime.now()
        self.last_modified = datetime.now()
    
    def add_product(self, product):
        for p in self.products:
            if p.id == product.id:
                return
        self.products.append(product)
        self.last_modified = datetime.now()
    