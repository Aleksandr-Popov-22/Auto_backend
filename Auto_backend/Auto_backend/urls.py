from django.contrib import admin
from Auto import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(r'marks/', views.MarkList.as_view(), name='marks-list'),
    path(r'marks/<str:id>/', views.ModelList.as_view(), name='models-list'),
    path(r'marks/<str:id>/<str:id_model>/', views.ModelDetail.as_view(), name='model-detail'),
    path(r'marks/<str:id>/<str:id_model>/characteristic/', views.ModelDetailCharacteristic.as_view(), name='model-detail-characteristic'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
