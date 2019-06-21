from django.shortcuts import render
from . import forms
from . import models


# Create your views here.
def search(request):
    form = forms.VehicleSearch()
    dic = {'form': form}
    if request.method == 'POST':
        form = forms.VehicleSearch(request.POST)
        if form.is_valid():
            vehicle_no = form.cleaned_data['vehicle']
            customer = form.cleaned_data['customer']
        if vehicle_no != '' and customer == None:
            transport = models.Transport.objects.filter(vehicle=vehicle_no)
            dic.update({'transport': transport})
        elif vehicle_no != '' and customer != None:
            transport = models.Transport.objects.filter(vehicle=vehicle_no, customer_code=customer)
            dic.update({'transport': transport})
        elif vehicle_no == '' and customer != None:
            transport = models.Transport.objects.filter(customer_code=customer)
            dic.update({'transport': transport})

    return render(request, 'search.html', dic)
