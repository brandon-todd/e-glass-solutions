from django.urls import path,include
from . import views
app_name = 'customers'
urlpatterns = [
    path('',views.customers,name='customers'),

]