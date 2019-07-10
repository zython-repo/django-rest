from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'rest_back', views.ListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('detail/<tag>/', views.DetailView.as_view(), name='detail'),
]
