from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import (
    ReservationViewSet, MenuViewSet, CommentViewSet, CategoryViewSet, ChefViewSet
)

# Road API REST
router = DefaultRouter()
router.register(r'reservations', ReservationViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'chefs', ChefViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    path('api/', include(router.urls)),
]
