from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product/create',views.create,name='create'),
    path('product/<int:product_id>',views.detail,name='detail'),
    path('product/upvote/<int:product_id>',views.upvote,name='upvote'),
]
