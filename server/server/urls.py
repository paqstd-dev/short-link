from django.contrib import admin
from django.urls import path, re_path, include

from .views import GenerateShortLink, GoToShortLink

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate/', GenerateShortLink.as_view()),
    path('go/<str:hash>/', GoToShortLink.as_view())
]
