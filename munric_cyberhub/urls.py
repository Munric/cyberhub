from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('services/', include('services.urls')),
    path('orders/', include('orders.urls')),   # ✅ add this
]