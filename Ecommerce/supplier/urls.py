from django.urls import path
from django.urls.resolvers import URLPattern
from supplier.views import(
    SupplierCreateView,
    SupplierListView,
    SupplierDetailView,
    SupplierUpdateView,
    SupplierDeleteView,
    delete_success,
)

app_name = 'suppliers'
urlpatterns = [
    path('', SupplierListView.as_view(), name='supplier_list'),
    path('create/', SupplierCreateView.as_view(), name='create_supplier'),
    path('<int:id>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('<int:id>/update/', SupplierUpdateView.as_view(), name='update_supplier'),
    path('<int:id>/delete/', SupplierDeleteView.as_view(), name='delete_supplier'),
    path('delete_success/', delete_success, name='delete_success'),
]