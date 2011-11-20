from datetime import datetime

class WishList(object):
    def __init__(self):
        self.products = []
        self.created = datetime.now()
        self.last_modified = datetime.now()
    
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

    # def remove_product(self, product_id):
    #     for p, q in self.products:
    #         if p.id == product_id:
    #             self.products.remove((p, q))
    #             break
    #     self._sort_products()
    
    def update_product(self, product_id, quantity):
        for p, q in self.products:
            if p.id == product_id:
                self.products.remove((p, q))
                if q > 0:
                    self.products.append((p, quantity))
                break
        self._sort_products()