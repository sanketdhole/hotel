from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_view, name='default_view'),
    # room rates
    path('room-rate/', views.room_rate_list, name='room_rate_list'),
    path('room-rate/create/', views.room_rate_create, name='room_rate_create'),
    path('room-rate/update/<int:room_id>/', views.room_rate_update, name='room_rate_update'),
    path('room-rate/delete/<int:room_id>/', views.room_rate_delete, name='room_rate_delete'),
    # over ridden rates
    path('over-ridden-rates/', views.overridden_rate_list, name='overridden_rate_list'),
    path('over-ridden-rates/create/', views.overridden_rate_create, name='overridden_rate_create'),
    path('over-ridden-rates/update/<int:overridden_rate_id>/', views.overridden_rate_update, name='overridden_rate_update'),
    path('over-ridden-rates/delete/<int:overridden_rate_id>/', views.overridden_rate_delete, name='overridden_rate_delete'),
    # discounts 
    path('discount/', views.discount_list, name='discount_list'),
    path('discount/create/', views.discount_create, name='discount_create'),
    path('discount/update/<int:pk>/', views.discount_update, name='discount_update'),
    path('discount/delete/<int:pk>/', views.discount_delete, name='discount_delete'),
    # apply discounts to rooms
    path('discount-room-rates/', views.discount_room_rate_list, name='discount_room_rate'),
    path('discount-room-rates/update/<int:discount_room_rate_id>/', views.discount_room_rate_update, name='discount_room_rate_update'),
    path('discount-room-rates/delete/<int:discount_room_rate_id>/', views.discount_room_rate_delete, name='discount_room_rate_delete'),
    
]
