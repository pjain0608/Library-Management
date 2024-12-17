from django.urls import path
from . import views

urlpatterns =  [
    path('',views.index, name = 'index'),
    path('one/<int:pk>',views.display,name = 'display'),
    path('two/<int:ab>',views.edit, name = 'edit'),
    path('add',views.create,name = 'add'),
]