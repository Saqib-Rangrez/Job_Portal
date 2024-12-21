from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, add_job

router = DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add_job/', add_job, name='add_job'),
]
