from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'price_check.views.index'),
    url(r'^search$', 'price_check.views.search'),
    url(r'^add$', 'price_check.views.add'),
    url(r'^wish_list$', 'price_check.views.wish_list'),
    url(r'^update$', 'price_check.views.update'),
    # Examples:
    # url(r'^$', 'price_check.views.home', name='home'),
    # url(r'^price_check/', include('price_check.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
