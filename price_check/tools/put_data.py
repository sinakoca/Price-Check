import pymongo

PRODUCTS = [
    {
        'name' : 'Milk 1L',
        'keywords' : ['milk', 'piim'],
        'retail' : {
            'maxima_taru' : {
                'price' : 0.99,
                'discout' : 0.1
            }
        }
    },
    {
        'name' : 'Bread',
        'keywords' : ['bread', 'tortila'],
        'retail' : {
            'maxima_taru' : {
                'price' : 0.99,
                'discout' : 0.1
            }
        }
    },
    {
        'name' : 'Milk 2.0L',
        'keywords' : ['milk', 'piim'],
        'retail' : {
            'maxima_taru' : {
                'price' : 0.99,
                'discout' : 0.1
            }
        }
    }
]

if __name__ == '__main__':
    connection = pymongo.Connection('localhost', 27017)
    db = connection.db
    products = db.products
    products.drop()
    for p in PRODUCTS:
        products.insert(p)