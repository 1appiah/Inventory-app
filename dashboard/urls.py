
from django.urls import path
from .views import index, staff, product, order,product_delete, product_update, staff_detail

urlpatterns = [
    path('dashboard/',index, name='dashboard-index'),
    path('staff/',staff, name='dashboard-staff'),
    path('product/',product, name='dashboard-product'),
    path('order/',order, name='dashboard-order'),
    path('product/delete/<int:pk>/',product_delete, name='dashboard-deletepro'),
    path('product/update/<int:pk>/',product_update, name='dashboard-updatepro'),
    path('staff/detail/<int:pk>/',staff_detail, name='dashboard-staff-detail'),
    
]
