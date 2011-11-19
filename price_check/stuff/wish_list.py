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

    def remove_product(self, product_id):
        for p in self.products:
            print p.id, product_id, p.id == product_id, p.id.__class__, product_id.__class__
            if p.id == product_id:
                print 'removed'
                self.products.remove(p)
                break
    