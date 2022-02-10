from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('form/', views.Form.as_view(), name='form'),
    path('fullblog/<int:pk>', views.FullBlog.as_view(), name='fullblog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
