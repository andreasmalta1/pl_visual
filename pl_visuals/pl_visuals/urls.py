from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("minutes.urls")),
    path("api/", include("api.urls")),
    path("api/products/", include("minutes.urls")),
    path("api/v2/", include("pl_visuals.routers")),
]
