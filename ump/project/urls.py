from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.mainV,name='index'),
    path('test/',views.textV,name='tet'),
    path('test/create/',views.textcreateV,name='tetcreate'),
    path('MR/<int:id>/',views.CreportV,name='mr'),
    path('abc/',views.abcV,name='abc'),
    path('search/',views.searchV,name='search'),
    path('Loging/', views.LogingV, name='Loging'),
    path('Logout/', views.logoutV, name='logout'),







]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
