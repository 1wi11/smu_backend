from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('login_module.urls')),
    path('', include('board.urls')),
]
