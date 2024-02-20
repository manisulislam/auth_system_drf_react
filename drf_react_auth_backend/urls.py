
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/',include('accounts_app.urls')),
    path('api/v1/auth/',include('social_accounts_app.urls')),
]
