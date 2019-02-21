from django.conf.urls import url
from breakfast import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
]