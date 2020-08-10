from django.urls import path
from django.conf.urls import url
from rfstracker import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


app_name = 'rfstracker'

urlpatterns = [
    path('home',views.index,name='index'),
    path('sales',views.sales,name='sales'),
    path('displaysalesdb',views.displaysalesdb,name='displaysalesdb'),
    url(r'^displaydetailsdb/(?P<pk>\d+)$',views.displaydetailsdb,name='displaydetailsdb'),
    path('addsalesdb',views.addsalesdb,name='addsalesdb'),
    url(r'^editsalesdb/(?P<pk>\d+)$',views.editsalesdb,name='editsalesdb'),
    url(r'^deletesalesdb/(?P<pk>\d+)$',views.deletesalesdb,name='deletesalesdb'),
    url(r'^addprogress/(?P<pk>\d+)$',views.addprogress,name='addprogress'),
    url(r'^viewdetails/(\d+)/(\d+)/$',views.viewdetails,name='viewdetails'),
    path('search',views.search,name='search'),
    path('',auth_views.LoginView.as_view(template_name = 'login.html'),name="login"),
    path('logout',auth_views.LogoutView.as_view(template_name = 'logout.html'),name="logout"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
