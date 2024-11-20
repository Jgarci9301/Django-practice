from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.ActorsList.as_view()),
    path('actor/<int:pk>/', views.ActorByID.as_view()), #/actor/5 => pk = 5; here pk is obviously an int
]

if settings.DEBUG: #if its in production mode, this code does not run
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)