from django.contrib import admin
from django.urls import path, include
from Orders import views
from django.conf import settings
from django.conf.urls.static import static
from Orders.views import generate_qr

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('Orders.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('qr/', generate_qr, name='generate-qr'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)