from django.shortcuts import render
from .forms import InvoiceForm
from .models import Invoice
from django.http import HttpResponseRedirect
from django.db.models import Q

def index(request):
    search  =   request.GET.get('search_bar',None)
    invoices = Invoice.objects.all()
    form = InvoiceForm()
    if search is not None:
        invoices    =   Invoice.objects.filter(Q(title__icontains = search) | Q(fromm__icontains = search) | Q(to__icontains = search) | Q(value__icontains = search))
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            Invoice.objects.create(**dados)
            form = InvoiceForm()
            return HttpResponseRedirect("/")
    else:
        form = InvoiceForm()

    return render(request, 'index.html', { 'form': form, 'invoices': invoices })
