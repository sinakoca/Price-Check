import pymongo

RETAILERS = [
    {
        'id' : 'maxima_tartu',
        'name' : 'Maxima',
        'city' : 'Tartu'
    },
    {
        'id' : 'comarket_tartu',
        'name' : 'Comarket',
        'city' : 'Tartu'
    },
    {
        'id' : 'consum_tartu',
        'name' : 'Consum',
        'city' : 'Tartu'
    },
    {
        'id' : 'maxima_tallinn',
        'name' : 'Maxima',
        'city' : 'Tallinn'
    }
]

PRODUCTS = [
    {
        'name' : 'Milk 1L',
        'keywords' : ['milk', 'piim'],
        'retailers' : {
            'maxima_tartu' : {
                'price' : 0.99
            },
            'comarket_tartu' : {
                'price' : 0.88
            },
            'consum_tartu' : {
                'price' : 0.77
            }
        }
    },
    {
        'name' : 'Bread',
        'keywords' : ['bread', 'tortila'],
        'retailers' : {
            'maxima_tartu' : {
                'price' : 0.42
            },
            'comarket_tartu' : {
                'price' : 0.47
            },
            'consum_tartu' : {
                'price' : 0.51
            }
        }
    },
    {
        'name' : 'Milk 2.0L',
        'keywords' : ['milk', 'piim'],
        'retailers' : {
            'maxima_tartu' : {
                'price' : 1.31
            },
            'comarket_tartu' : {
                'price' : 1.20
            },
            'consum_tartu' : {
                'price' : 1.33
            }
        }
    }
]

if __name__ == '__main__':
    connection = pymongo.Connection('localhost', 27017)
    db = connection.db
    # save retailers
    retailers = db.retailers
    retailers.drop()
    for r in RETAILERS:
        retailers.insert(r)
    # save products
    products = db.products
    products.drop()
    for p in PRODUCTS:
        products.insert(p)
