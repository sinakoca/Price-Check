class Product(object):
    def __init__(self, dict_object):
        self.id = unicode(dict_object['_id'])
        self.name = dict_object['name']
        self.retail = dict_object['retail']
        self.keywords = dict_object['keywords']
