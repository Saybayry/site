from django.urls import path
from . import views

app_name = 'storeStaffForArt'
urlpatterns = [
    path("", views.startPage.as_view(), name= 'startpage'),
    path('pageInwork',views.pageInwork ,name ='pageInwork'),
    path('<int:pk>', views.productForArtDetalsview.as_view(), name="productForArt-detail"),

]