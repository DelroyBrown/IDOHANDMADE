from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

app_name = "idohandmade_base"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("markets/", include("idohandmade_markets.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
