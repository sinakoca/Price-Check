import pprint
from operator import itemgetter
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, \
     HttpResponseBadRequest, Http404
import pymongo
from pymongo.objectid import ObjectId

from stuff.product import Product
from stuff.wish_list import WishList
from stuff.geolocation import get_city

from django.utils import simplejson as json

import settings

#regsitration
from django import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt

connection = pymongo.Connection(settings.MONGO_SERVER, settings.MONGO_PORT)
products = connection.db.products
retailers = connection.db.retailers

def index(request, login_error=False):
    _check_session_wish_list(request.session)
    wish_list = _get_wish_list(request.session)
    _check_session_city(request)
    city = _get_city(request.session)
    return render_to_response('index.html', {'user': request.user, 'city' : city, 'wish_list' : wish_list, 'login_error' : login_error})
    
def search(request):
    query = request.GET.get('q') or ''
    if not query:
        return HttpResponseRedirect("/")
    _check_session_wish_list(request.session)
    wish_list = _get_wish_list(request.session)
    _check_session_city(request)
    city = request.GET.get('city') or _get_city(request.session)
    request.session['city'] = city
    product_set = set()
    terms = query.lower().split()
    for term in terms:
        relevant_productcs = products.find({'keywords' : term})
        for p in relevant_productcs:
            product = Product(p)
            product_set.add(product)
    return render_to_response('search.html', {'user': request.user, 'query' : query, 'products' : product_set, 'city' : city,
        'wish_list' : wish_list})
    
def add(request):
    query = request.GET.get('q') or ''
    product_id = request.GET.get('product_id')
    quantity_value = request.GET.get('quantity')
    if not quantity_value.isdigit():
        quantity_value = '1'
    quantity = int(quantity_value)
    
    _check_session_wish_list(request.session)
    wish_list = _get_wish_list(request.session)
    # _check_session_city(request)
    # city = _get_city(request.session)
    if product_id:
        product_object = products.find_one({'_id' : ObjectId(product_id) })
        if product_object:
            product = Product(product_object)
            wish_list.add_product(product, quantity)
    request.session['wish_list'] = wish_list
    return HttpResponseRedirect("/search?q=" + query)
    # return render_to_response('search.html', {'user': request.user, 'query' : query, 'city' : city, 'wish_list' : wish_list})

def wish_list(request):
    product_id = request.GET.get('product_id')
    _check_session_wish_list(request.session)
    wish_list = _get_wish_list(request.session)
    _check_session_city(request)
    city = _get_city(request.session)
    
    return render_to_response('list.html', {'user': request.user, 'city' : city, 'wish_list' : wish_list})
    
# def remove(request):
#     product_id = request.GET.get('product_id')
# 
#     _check_session_wish_list(request.session)
#     wish_list = _get_wish_list(request.session)
#     wish_list.remove_product(product_id)
#     request.session['wish_list'] = wish_list
#     return render_to_response('index.html', {'wish_list' : wish_list})

def update(request):
    query = request.GET.get('q') or ''
    product_id = request.GET.get('product_id')
    if not product_id:
        raise Http404()
    quantity_value = request.GET.get('quantity')
    if not quantity_value.isdigit():
        quantity_value = '1'
    quantity = int(quantity_value)
    _check_session_wish_list(request.session)
    wish_list = _get_wish_list(request.session)
    # _check_session_city(request)
    # city = _get_city(request.session)
    
    wish_list.update_product(product_id, quantity)
    request.session['wish_list'] = wish_list
    return HttpResponseRedirect("/search?q=" + query)
    # return render_to_response('index.html', {'user': request.user, 'city' : city, 'wish_list' : wish_list})

def compare(request):
    _check_session_wish_list(request.session)
    wish_list = _get_wish_list(request.session)
    _check_session_city(request)
    city = _get_city(request.session)
    # get retailers based on location
    retailer_objects = retailers.find({'city' : city})
    retailer_ids, retailer_names = [], []
    retailer_totals = []
    for r in retailer_objects:
        retailer_ids.append(r['id'])
        retailer_names.append(r['name'])
    totals = [0] * len(retailer_ids)
    products_with_prices = []
    for p, q in wish_list.products:
        prices = []
        for i, retailer_id in enumerate(retailer_ids):
            retailer = p.retailers.get(retailer_id)
            price = None
            if retailer:
                price = retailer.get('price')
                totals[i] += price * q
            prices.append(price)
        products_with_prices.append((p, q, prices))
    return render_to_response('compare.html', {'user': request.user, 'products_with_prices' : products_with_prices,
            'retailer_names' : retailer_names, 'totals' : totals})

@csrf_exempt
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return render_to_response("register_completed.html")
        # else:
        #     form = UserCreationForm()
    return render_to_response("register.html", {'form': form,})

@csrf_exempt
def login(request):
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=email, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/")
    else:
        # Show an error page
        return index(request, True)

@csrf_exempt
def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")

def update_location(request):
    city = request.GET.get('city')
    request.session['city'] = city
    return HttpResponseRedirect("/")

def _check_session_wish_list(session):
    if 'wish_list' not in session:
        session['wish_list'] = WishList()

def _get_wish_list(session):
    return session['wish_list']

def _check_session_city(request):
    if 'city' not in request.session:
        ip = get_client_ip(request)
        # ip = '62.85.60.2'
        city = get_city(ip) or 'Tartu'
        request.session['city'] = city

def _get_city(session):
    return session['city']

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

    