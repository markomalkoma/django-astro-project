
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('astrology.urls')),
    path('<str:c1>/', include('astrology.urls')),
    path('<str:c1>/<str:c2>/', include('astrology.urls')),
    path('<str:c1>/<str:c2>/<str:c3>/', include('astrology.urls')),
    path('<str:c1>/<str:c2>/<str:c3>/<str:c4>/', include('astrology.urls')),
    path('<str:c1>/<str:c2>/<str:c3>/<str:c4>/<str:c5>/', include('astrology.urls')),
]
