from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portal_ensino.base.urls')),

    # LOGIN
    path('contas/', include('django.contrib.auth.urls')),
]
