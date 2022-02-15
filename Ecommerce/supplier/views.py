from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from supplier.forms import SupplierModelForm
from .models import Supplier

class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'suppliers/create_supplier.html'
    form_class = SupplierModelForm
    queryset = Supplier.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class SupplierListView(ListView):
    template_name = 'suppliers/supplier_list.html'
    queryset = Supplier.objects.all()

class SupplierDetailView(DetailView):
    template_name = 'suppliers/supplier_detail.html'
    #queryset = Supplier.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Supplier, id=id_)

class SupplierUpdateView(UpdateView):
    template_name = 'suppliers/create_supplier.html'
    form_class = SupplierModelForm
    queryset = Supplier.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Supplier, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class SupplierDeleteView(DeleteView):
    template_name = 'suppliers/delete_supplier.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Supplier, id=id_)

    def get_success_url(self):
        return reverse("suppliers:delete_success")

def delete_success(request):
    return render(request, 'suppliers/delete_success.html', {})