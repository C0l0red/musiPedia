from django.conf.urls import include
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.urls.conf import re_path
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from users import views as user_views
from core import views as core_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'users', user_views.UserCreateViewSet)
router.register(r'artists', core_views.ArtistViewSet)
router.register(r'artists', core_views.ArtistCreateViewSet)
router.register(r'albums', core_views.AlbumViewSet)
router.register(r'albums', core_views.AlbumCreateViewSet)
router.register(r'songs', core_views.SongViewSet)
router.register(r'songs', core_views.SongCreateViewSet)
router.register(r'artists', core_views.ArtistRatingViewSet, basename='rate-artist')
router.register(r'albums', core_views.AlbumRatingViewSet, basename='rate-album')
router.register(r'songs', core_views.SongRatingViewSet, basename='rate-song')
# router.register()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False))
]
