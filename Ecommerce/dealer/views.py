from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import(
    DetailView,
    ListView,
    #UpdateView,
)

#from .forms import DealerModelForm
from Sparke.models import Customer

class DealerListView(ListView):
    template_name = 'dealers/dealer_list.html'
    queryset = Customer.objects.all()

class DealerDetailView(DetailView):
    template_name = 'dealers/dealer_detail.html'
    #queryset = Supplier.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id_)

#class DealerUpdateView(UpdateView):
#    template_name = 'dealers/update_dealer.html'
#    form_class = DealerModelForm
#    queryset = Customer.objects.all()

#    def get_object(self):
#        id_ = self.kwargs.get("id")
#        return get_object_or_404(Customer, id=id_)

#    def form_valid(self, form):
#        print(form.cleaned_data)
#        return super().form_valid(form)