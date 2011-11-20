class Product(object):
    def __init__(self, dict_object):
        self.id = unicode(dict_object['_id'])
        self.name = dict_object['name']
        self.image = dict_object.get('image')
        self.retailers = dict_object['retailers']
        self.keywords = dict_object['keywords']
