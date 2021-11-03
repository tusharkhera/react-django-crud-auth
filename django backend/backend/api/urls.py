from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from .views import QuoteViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('quotes', QuoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
]