from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("wordcounter.urls", "wordcount"), namespace="wordcount")),
]


if settings.DEBUG:
    # this is not currently necessary, but let's setup it anyway:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
