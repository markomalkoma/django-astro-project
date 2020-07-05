from . import views
from django.urls import path

#ukljucuje uvek route i view (name i kwargs su optional) 

urlpatterns = [
    path('redirector/', views.redirector, name='redirector'),
    path('handler/', views.handler, name='handler'),
    path('about/', views.about, name='about'),
    path('complete/', views.complete, name='complete'),
    path('complete/group/', views.group, name='group' ),
    path('complete/group/<int:hid>', views.detail, name='detail' ),
    path('dominant/<str:planet1>/<int:aspect1>/<str:planet2>/<str:planet3>/<int:aspect2>/<str:planet4>/', views.dominant, name='dominant'),
    path('combined/<int:results>/<str:planet1>/<str:planet2>/<str:planet3>/<str:planet4>/<str:planet5>/<str:planet6>/', views.combined, name='combined'),
    path('combined/<int:results>/<str:planet1>/<str:planet2>/<str:planet3>/<str:planet4>/<str:planet5>/', views.combined, name='combined'),
    path('combined/<int:results>/<str:planet1>/<str:planet2>/<str:planet3>/<str:planet4>/', views.combined, name='combined'),
    path('combined/<int:results>/<str:planet1>/<str:planet2>/<str:planet3>/', views.combined, name='combined'),
    path('combined/<int:results>/<str:planet1>/<str:planet2>/', views.combined, name='combined'),
    path('refresh/', views.refresh),
    path('', views.blanco, name='blanco'),
]
