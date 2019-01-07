# dprojx/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from dappx import views
# from django.contrib.auth.decorators import login_required

# admin.autodiscover()
# admin.site.login = login_required(admin.site.login)
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^tamin/',include('dappx.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
]