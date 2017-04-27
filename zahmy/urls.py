from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^website/', include('website.urls', namespace='website')),
    url('^', include('django.contrib.auth.urls')),
]
