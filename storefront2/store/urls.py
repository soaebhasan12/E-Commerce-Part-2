from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.Product_List.as_view()),
    path('products/<int:id>', views.Product_Detail.as_view()),
    path('collections/<int:pk>', views.collection_detail, name='collection-detail'),
]
