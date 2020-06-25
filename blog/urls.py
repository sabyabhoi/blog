from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.PostList.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('base/', views.base, name='base'),
  path('<slug:slug>/', views.post_detail, name='post_detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)