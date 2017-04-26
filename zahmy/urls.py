from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^site/', include('site.urls', namespace='site')),
    url('^', include('django.contrib.auth.urls')),
]
