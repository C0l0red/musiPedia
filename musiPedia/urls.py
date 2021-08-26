from django.conf.urls import include
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.urls.conf import re_path
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
# from users import views as user_views
# from core import views as core_views
from containers import dependencies

router = DefaultRouter()
# router.register(r'users', dependencies.UserViewSet)
router.register(r'artists', dependencies.ArtistViewSet)
router.register(r'albums', dependencies.AlbumViewSet)
router.register(r'songs', dependencies.SongViewSet)
# router.register()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False))
]
