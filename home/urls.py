from django.urls import path
from home import views
from AdminPanelDemo.settings import DEBUG,MEDIA_URL,MEDIA_ROOT,STATIC_URL,STATIC_ROOT

from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='index'),
    path('upload/',views.upload,name='upload'),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
]

if DEBUG:
    urlpatterns+=static(MEDIA_URL,document_root=MEDIA_ROOT)
    urlpatterns+=static(STATIC_URL,document_root=STATIC_ROOT)
