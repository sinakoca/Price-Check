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
    },
    {
        'id' : 'prisma_tartu',
        'name' : 'Prisma',
        'city' : 'Tartu'
    }
]

PRODUCTS = [
    {
        'name' : 'Tere Piim 1L',
        'keywords' : ['milk', 'piim'],
        'image' : None,
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
        'name' : 'Sai Leib',
        'keywords' : ['bread', 'tortilla', 'white'],
        'image' : None,
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
        'image' : None,
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
    },
    {
        'name' : 'Mikrolaineahi Gamma, SMB177DIH-P',
        'keywords' : ['microwave', 'Oven'],
        'image' : '01.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 34.99
            },
            'maxima_tallinn' : {
                'price' : 45.99
            },
            'prisma_tartu' : {
                'price' : 54.99
            }
        }
    },
    {
        'name' : 'Leib',
        'keywords' : ['bread', 'tortilla'],
        'image' : None,
        'retailers' : {
            'maxima_tartu' : {
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
            'comarket_tartu' : {
                'price' : 14.99
            },
            'consum_tartu' : {
                'price' : 11.99
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
                'price' : 4.19
            },
            'comarket_tartu' : {
                'price' : 5.69
            },
            'consum_tartu' : {
                'price' : 6.72
            }
        }
    }
    ,
    {
        'name' : 'Farm drinking cherry yougart',
        'keywords' : ['yougurt', 'drinking'],
        'image' : '13.jpg',
        'retailers' : {
            'maxima_tartu' : {
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
        'name' : 'alma yougart',
        'keywords' : ['yougart', 'alma'],
        'image' : '06.jpg',
        'retailers' : {
            'maxima_tartu' : {
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
        'name' : 'Segu',
        'keywords' : ['segu', 'Segu'],
        'image' : '07.jpg',
        'retailers' : {
            'maxima_tartu' : {
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
        'name' : 'Kostilja',
        'keywords' : ['kostilja', 'kostilja'],
        'image' : '08.jpg',
        'retailers' : {
            'maxima_tartu' : {
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
        'name' : 'Coockies',
        'keywords' : ['coockies', 'coockie'],
        'image' : '10.jpg',
        'retailers' : {
            'maxima_tartu' : {
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
        'name' : 'pampers',
        'keywords' : ['pampers', 'Pamper'],
        'image' : '11.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 2.81
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
        'name' : 'Al Coq',
        'keywords' : ['alcoq', 'beer'],
        'image' : '12.jpg',
        'retailers' : {
            'maxima_tartu' : {
                'price' : 2.00
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
