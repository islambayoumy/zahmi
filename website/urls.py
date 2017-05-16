from django.conf.urls import url
from website.views import MainView, AuthView, EventView, ContactView, ChampionshipView, StoreView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', MainView.index, name='index'),
    url(r'^about/$', MainView.about, name='about'),
    url(r'^events/$', EventView.events_list, name='events'),
    url(r'^event/(?P<event_id>\d+)/$', EventView.event_details, name='event'),
    url(r'^contact/$', ContactView.contact, name='contact'),
    url(r'^championship/$', ChampionshipView.show, name='championship'),
    url(r'^store/$', StoreView.home, name='store'),
    url(r'^store/product/$', StoreView.product_show, name='product'),
]
