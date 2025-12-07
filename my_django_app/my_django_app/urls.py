# urls.py

from django.contrib import admin
from django.urls import include, path
from hello.views import custom_login_view  # Ensure this is correctly imported

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('inadmin/', admin.site.urls),  # True admin site
    path('login/', custom_login_view, name='custom_login'),  # Custom login URL
]
