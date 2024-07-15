from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about,name='about'),
    path('menu',views.menu,name="menu"),
    path('details<int:id>.html', views.details, name='details'),
    path('reservation',views.reservation,name="reservation"),
    path('creat_res',views.creat_res,name="creat_res"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)