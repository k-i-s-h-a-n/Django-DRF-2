from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('person/', person,name = "person"),
    
]




urlpatterns = router.urls
