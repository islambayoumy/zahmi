from django.conf.urls import url
from website.views import MainView, AuthView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', MainView.home, name='home'),    
    url(r'^about$', MainView.about, name='about'),    
    
    url(r'^login/$', auth_views.login, '''{'template_name': 'accounts/login.html'},''', name='login'),
    url(r'^logout/$', auth_views.logout, '''{'template_name': 'accounts/logout.html'},''', name='logout'),
    #url(r'^register/$', AuthView.register, name='register'),

    url(r'^password_reset/$', auth_views.password_reset, '''{'template_name': 'accounts/reset-password.html'},''', name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, '''{'template_name': 'accounts/reset-password-done.html'},''', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, '''{'template_name': 'accounts/reset-password-confirm.html'},''', name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, '''{'template_name': 'accounts/reset-password-complete.html'},''', name='password_reset_complete'),

]
