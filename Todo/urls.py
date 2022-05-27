
from django.urls import path
from .views import home,Todo_List,Todo_Create,Todo_Update,Todo_Delete,Todo_Detail

urlpatterns = [
    
    path('', home, name="home"),
    path('list/', Todo_List, name="list"),
    path('create/', Todo_Create, name="create"),
    path('update/<int:id>', Todo_Update, name="update"),
    path('delete/<int:id>', Todo_Delete, name="delete"),
    path('detail/<int:id>', Todo_Detail, name="detail"),
   
    
]
