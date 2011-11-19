from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, \
     HttpResponseBadRequest, Http404
import pymongo
from pymongo.objectid import ObjectId

from stuff.product import Product
from stuff.wish_list import WishList

connection = pymongo.Connection('localhost', 27017)
products = connection.db.products

def index(request):
    _check_session_wish_list(request.session)
    return render_to_response('index.html', {})
    
def search(request):
    query = request.GET.get('q') or ''
    product_list = []
    relevant_productcs = products.find({'keywords' : query})
    for p in relevant_productcs:
        product = Product(p)
        product_list.append(product)
    return render_to_response('index.html', {'query' : query, 'products' : product_list, 'wish_list' : _get_wish_list(request.session)})
    
def add(request):
    product_id = request.GET.get('product_id')
    
    _check_session_wish_list(request.session)
    wish_list = _get_wish_list(request.session)
    if product_id:
        product_object = products.find_one({'_id' : ObjectId(product_id) })
        if product_object:
            product = Product(product_object)
            wish_list.add_product(product)
    request.session['wish_list'] = wish_list
    return render_to_response('index.html', {'wish_list' : wish_list})
    
def remove(request):
    product_id = request.GET.get('product_id')

    _check_session_wish_list(request.session)
    wish_list = _get_wish_list(request.session)
    wish_list.remove_product(product_id)
    request.session['wish_list'] = wish_list
    return render_to_response('index.html', {'wish_list' : wish_list})

def _check_session_wish_list(session):
    if 'wish_list' not in session:
        session['wish_list'] = WishList()

def _get_wish_list(session):
    return session['wish_list']