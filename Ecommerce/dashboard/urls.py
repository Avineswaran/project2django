from django.urls import path
from .views import *

app_name = 'dashboards'
urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('profit_data/', profit_view, name='profit_data'),
    path('delete_profit/<profit_id>', delete_profit, name='delete_profit'),

    path('invoice/', InvoiceListView.as_view(), name='invoice_list'),
    path('markup/', MarkupView.as_view(), name='markup_view'),
    path('markup/<int:id>/update/', MarkupUpdateView.as_view(), name='update_markup'),

    path('markup_success/', markup_success, name="markup_success"),
]