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

RETAILERS = [
    {
        'name' : 'Maxima',
        'city' : 'Tartu'
    },
    {
        'name' : 'Comarket',
        'city' : 'Tartu'
    },
    {
        'name' : 'Consum',
        'city' : 'Tartu'
    },
    {
        'name' : 'Maxima',
        'city' : 'Tallin'
    }
]

if __name__ == '__main__':
    connection = pymongo.Connection('localhost', 27017)
    db = connection.db
    # save products
    products = db.products
    products.drop()
    for p in PRODUCTS:
        products.insert(p)
    # save retailers
    retailers = db.retailers
    retailers.drop()
    for r in RETAILERS:
        retailers.insert(r)