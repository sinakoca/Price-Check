class Product(object):
    def __init__(self, dict_object):
        self.id = unicode(dict_object['_id'])
        self.name = dict_object['name']
        self.price = dict_object['price']
        self.keywords = dict_object['keywords']
