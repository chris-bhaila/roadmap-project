"""URL configuration for career_roadmap project."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from accounts.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='home'),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('profiles.urls')),
    path('predictions/', include('predictions.urls')),
    path('roadmap/', include('roadmap.urls')),
    path('progress/', include('progress.urls')),
    path('admin-panel/', include('admin_panel.urls')),
]

if settings.DEBUG:
    urlpatterns += [path('__reload__/', include('django_browser_reload.urls'))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
