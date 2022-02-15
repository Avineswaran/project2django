from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import WeeklyProfitForm
from django.views.generic import *
from django.db.models import Sum

from allauth.account.models import EmailAddress
from supplier.models import Supplier
from Sparke.models import Customer, Order
from .forms import *
from .models import *
from allauth.account.models import EmailAddress

#from .filters import InvoiceFilter

# Create your views here.
class Dashboard(generic.CreateView):
    template_name = "dashboards/dashboard.html"

    model = WeeklyProfit
    form_class = WeeklyProfitForm
    queryset = WeeklyProfit.objects.all()
    success_url = reverse_lazy('dashboards:dashboard')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        profit = WeeklyProfit.objects.all()

        form = WeeklyProfitForm
        if request.method == "POST":
            form = WeeklyProfitForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = WeeklyProfitForm()

        supplier_count = Supplier.objects.count()
        dealer_count = Customer.objects.count()
        invoice_count = Invoice.objects.count()
        car_supplier = Supplier.objects.filter(vehicleType__contains='Car').count()
        truck_supplier = Supplier.objects.filter(vehicleType__contains='Truck & Used Part').count()
        verified = EmailAddress.objects.filter(verified=True).count()
        not_verified = EmailAddress.objects.filter(verified=False).count()
        income = WeeklyProfit.objects.aggregate(Sum('profit'))['profit__sum']

        sparke_data= {
            "dealer_count" : dealer_count,
            "supplier_count" : supplier_count,
            "invoice_count" : invoice_count,
            "car_supplier" : car_supplier,
            "truck_supplier" : truck_supplier,
            "verified" : verified,
            "not_verified" : not_verified,
            "income" : income,

            'profit' : profit,
            'form' : form,
        }
        return render(request, self.template_name, sparke_data)

def profit_view(request):
    profit = WeeklyProfit.objects.all()
    context= {
        'profit' : profit,
    }
    return render(request, 'dashboards/profit_data.html', context)

def delete_profit(request, profit_id):
    profit = WeeklyProfit.objects.get(pk=profit_id)
    profit.delete()
    return redirect('dashboards:profit_data')

class InvoiceListView(ListView):
    template_name = 'dashboards/invoice_list.html'
    queryset = Invoice.objects.all()

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['filter'] = InvoiceFilter(self.request.GET, queryset=self.get_queryset())
    #    return context  

class MarkupView(ListView):
    template_name = 'dashboards/markup_view.html'
    queryset = Markup.objects.all()

class MarkupUpdateView(UpdateView):
    template_name = 'dashboards/update_markup.html'
    form_class = MarkupModelForm
    queryset = Markup.objects.all()
    success_url = reverse_lazy('dashboards:markup_success')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Markup, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

def markup_success(request):
    return render(request, 'dashboards/markup_success.html', {})
