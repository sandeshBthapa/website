from django.urls import path
from .views import listings,listing1,Search

app_name='lis'
urlpatterns = [
    path('',listings,name='listings'),
    path('str:<listing_id>',listing1,name='listing3'),
    path('search',Search,name='search'),

]