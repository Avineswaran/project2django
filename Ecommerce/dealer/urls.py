from django.urls import path
from django.urls.resolvers import URLPattern
from .views import(
    DealerListView,
    DealerDetailView,
)

app_name = 'dealers'
urlpatterns = [
    path('', DealerListView.as_view(), name='dealer_list'),
    path('<int:id>/', DealerDetailView.as_view(), name='dealer_detail'),
]