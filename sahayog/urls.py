"""
URL configuration for Sahayog project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('route-optimizer/', include('route_optimizer.urls')),
    path('', RedirectView.as_view(url='/route-optimizer/', permanent=False)),
    path("notifications/<int:id>/mark_read/", views.mark_read, name="mark_read"),
path("notifications/<int:id>/mark_unread/", views.mark_unread, name="mark_unread"),

]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
