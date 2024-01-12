from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name = 'portfolio'


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('principal_photo/', views.PrincipalPhotoView.as_view(), name='principal_photo')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
