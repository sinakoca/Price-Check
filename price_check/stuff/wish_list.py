from datetime import datetime

class WishList(object):
    def __init__(self):
        self.products = []
        self.created = datetime.now()
        self.last_modified = datetime.now()
    
    def add_product(self, product, quantity):
        for p, _ in self.products:
            if p.id == product.id:
                return
        self.products.append((product, quantity))
        self.last_modified = datetime.now()

    def remove_product(self, product_id):
        for p, q in self.products:
            if p.id == product_id:
                self.products.remove((p, q))
                break
    