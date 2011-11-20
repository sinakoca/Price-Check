from datetime import datetime

class WishList(object):
    def __init__(self):
        self.products = []
        self.created = datetime.now()
        self.last_modified = datetime.now()
        self.retail_chains = []
    
    def _sort_products(self):
        self.products.sort(key=lambda x:x[0].name)
    
    def add_product(self, product, quantity):
        for p, q in self.products:
            if p.id == product.id:
                self.products.remove((p, q))
                self.products.append((p, q + quantity))
                self._sort_products()
                return
        self.products.append((product, quantity))
        self.last_modified = datetime.now()
        self._sort_products()


    def update_product(self, product_id, quantity):
        i = 0
        for p, q in self.products:
            if p.id == product_id:
                self.products.pop(i)
                if quantity > 0:
                    self.products.append((p, quantity))
                break
            i += 1
        self._sort_products()