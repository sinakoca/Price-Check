class Product(object):
    def __init__(self, dict_object):
        self.id = unicode(dict_object['_id'])
        self.name = dict_object['name']
        self.retailers = dict_object['retailers']
        self.keywords = dict_object['keywords']
