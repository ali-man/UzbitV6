from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from www.views import HomePageViews

admin.autodiscover()
admin.site.site_header = 'Панель управления'
urlpatterns = [
    path('admin_tools/', include('admin_tools.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api_auth/', include('rest_framework.urls')),

    path('', HomePageViews.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)