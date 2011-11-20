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
        'name' : 'Konsum',
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
        'name' : 'Tere Milk 1 Lt',
        'keywords' : ['milk', 'piim'],
        'image' : None,
        'retailers' : {
            'maxima_tartu' : {
                'price' : 0.99
            },
            'comarket_tartu' : {
                'price' : 0.88
            },
	    'maxima_tallinn' : {
                'price' : 0.99
            },
            'consum_tartu' : {
                'price' : 0.77
            }
        }
    },
    {
        'name' : 'White Bread',
        'keywords' : ['bread', 'tortilla', 'white'],
        'image' : 'whitebread.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 0.42
            },
            'comarket_tartu' : {
                'price' : 0.47
            },
	    'maxima_tallinn' : {
                'price' : 0.42
            }, 
            'consum_tartu' : {
                'price' : 0.51
            }
        }
    },
    {
        'name' : 'Pinar Milk 2.0 Lt',
        'keywords' : ['milk', 'piim'],
        'image' : 'pinar.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 1.31
            },
            'comarket_tartu' : {
                'price' : 1.20
            },
	    'maxima_tallinn' : {
                'price' : 1.31
            },
            'consum_tartu' : {
                'price' : 1.33
            }
        }
    },
    {
        'name' : 'Philips SCF510 Microwave',
        'keywords' : ['microwave', 'Oven'],
        'image' : '01.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 34.99
            },
            'maxima_tallinn' : {
                'price' : 45.99
            },
	    'consum_tartu': {
                'price' : 58.99
            },
	    'comarket_tartu': {
                'price' : 58.99
            }
        }
    },
    {
        'name' : 'Persil 3 Kg',
        'keywords' : ['detergent', 'persil'],
        'image' : 'persil.jpeg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 0.39
            },
	     'maxima_tallinn' : {
                'price' : 0.39
            },
            'comarket_tartu' : {
                'price' : 0.48
            },
            'consum_tartu' : {
                'price' : 0.50
            }
        }
    },
    {
        'name' : 'Tekk 150x200 cm',
        'keywords' : ['blanket', 'quilt'],
        'image' : '02.jpg',
        'retailers' : {
             'maxima_tartu' : {
                'price' : 9.99
            },
            'maxima_tallinn' : {
                'price' : 8.99
            },
	    'consum_tartu': {
                'price' : 9.25
            },
	    'comarket_tartu': {
                'price' : 8.90
            }
        }
    },
    {
        'name' : 'Pleed 127x152 cm',
        'keywords' : ['blanket', 'pull', 'shawl'],
        'image' : '03.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 4.49
            },
	    'maxima_tallinn' : {
                'price' : 9.99
            },
            'comarket_tartu' : {
                'price' : 6.79
            },
            'consum_tartu' : {
                'price' : 8.35
            }
        }
    },
    {
        'name' : 'Prugikotid 60 l x 25 tk',
        'keywords' : ['shoppingbag', 'garbbagebag', 'bag','shopper'],
        'image' : '04.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 0.89
            },
	    'maxima_tallinn' : {
                'price' : 0.89
            },
            'comarket_tartu' : {
                'price' : 1.67
            },
            'consum_tartu' : {
                'price' : 1.29
            }
        }
    },
    {
        'name' : 'Jahvatatud Kohv Merrild Red, 500g',
        'keywords' : ['coffee', 'coffeebag', 'groundcoffee'],
        'image' : '05.jpg',
        'retailers' : {
             'maxima_tartu' : {
                'price' : 4.99
            },
            'maxima_tallinn' : {
                'price' : 5.99
            },
	    'consum_tartu': {
                'price' : 4.88
            },
	    'comarket_tartu': {
                'price' : 4.14
            }
        }
    }
    ,
    {
        'name' : 'Farm Cherry Yoghurt',
        'keywords' : ['yoghurt', 'farm'],
        'image' : '13.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 1.15
            },
	    'maxima_tallinn' : {
                'price' : 1.15
            },
            'comarket_tartu' : {
                'price' : 1.05
            },
            'consum_tartu' : {
                'price' : 1.29
            }
        }
    }
    ,
    {
        'name' : 'Alma Yoghurt 360 Gr',
        'keywords' : ['yoghurt', 'alma'],
        'image' : '06.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 0.55
            },
	    'maxima_tallinn' : {
                'price' : 0.55
            },
            'comarket_tartu' : {
                'price' : 0.35
            },
            'consum_tartu' : {
                'price' : 0.78
            }
        }
    }
    ,
    {

        'name' : 'Fresco Frozen Vegetable',
        'keywords' : ['vegetable', 'Segu'],
        'image' : '07.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 0.99
            },
	    'maxima_tallinn' : {
                'price' : 0.99
            },
            'comarket_tartu' : {
                'price' : 1.05
            },
            'consum_tartu' : {
                'price' : 1.04
            }
        }
    }
    ,
    {
        'name' : 'Maggi Chicken Soup',
        'keywords' : ['soup', 'kostilja'],
        'image' : '08.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 1.99
            },
	    'maxima_tallinn' : {
                'price' : 1.99
            },
            'comarket_tartu' : {
                'price' : 1.65
            },
            'consum_tartu' : {
                'price' : 2.24
            }
        }
    }
    ,
    {
        'name' : 'Butter Toffees',
        'keywords' : ['toffee', 'toffee'],
        'image' : '09.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 0.99
            },
	    'maxima_tallinn' : {
                'price' : 0.99
            },
            'comarket_tartu' : {
                'price' : 0.65
            },
            'consum_tartu' : {
                'price' : 0.85
            }
        }
    }
    ,
    {
        'name' : 'Acme Cookies(500 gr Pack)',
        'keywords' : ['cookies', 'cookie'],
        'image' : '10.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 0.99
            },
	    'maxima_tallinn' : {
                'price' : 0.99
            },
            'comarket_tartu' : {
                'price' : 0.65
            },
            'consum_tartu' : {
                'price' : 0.85
            }
        }
    }
    ,
    {
        'name' : 'Pampers in 12 pack',
        'keywords' : ['pampers', 'Pamper'],
        'image' : '11.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 2.81
            },
	    'maxima_tallinn' : {
                'price' : 2.99
            },
            'comarket_tartu' : {
                'price' : 1.90
            },
            'consum_tartu' : {
                'price' : 2.50
            }
        }
    }
    ,
    {
        'name' : 'Ale Coq',
        'keywords' : ['alecoq', 'beer'],
        'image' : '12.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 2.00
            },
	    'maxima_tallinn' : {
                'price' : 1.99
            },
            'comarket_tartu' : {
                'price' : 1.90
            },
            'consum_tartu' : {
                'price' : 2.10
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