# import core
from django.urls import path, re_path, include

# import project
from .views import GenerateShortLink, GoToShortLink

urlpatterns = [
    path('go/', include([
        path('generate/', GenerateShortLink.as_view()),
        path('<str:hash>/', GoToShortLink.as_view())
    ]))
]
