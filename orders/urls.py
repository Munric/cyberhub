from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:service_id>/', views.create_order, name='create_order'),
    path('success/', views.order_success, name='order_success'),  # ✅ ADD
]