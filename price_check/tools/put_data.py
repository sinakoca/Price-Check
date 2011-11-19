import pymongo

PRODUCTS = [
    {
        'name' : 'Milk 1L',
        'price' : '0.99',
        'keywords' : ['milk', 'piim']
    },
    {
        'name' : 'Bread',
        'price' : '1.99',
        'keywords' : ['bread', 'tortila']
    },
    {
        'name' : 'Milk 2.0L',
        'price' : '1.89',
        'keywords' : ['milk', 'piim']
    }
]

if __name__ == '__main__':
    connection = pymongo.Connection('localhost', 27017)
    db = connection.db
    products = db.products
    products.drop()
    for p in PRODUCTS:
        products.insert(p)