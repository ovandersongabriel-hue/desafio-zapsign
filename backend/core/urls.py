from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import DocumentViewSet, CompanyViewSet  

router = DefaultRouter()
router.register(r'documents', DocumentViewSet)
router.register(r'companies', CompanyViewSet)  

urlpatterns = [
    path('', include(router.urls)),
]