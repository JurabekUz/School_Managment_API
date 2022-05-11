
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('allauth/',include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
