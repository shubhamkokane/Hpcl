from django.shortcuts import render
from . import forms


# Create your views here.
def search(request):
    form=forms.Search()
    dic={'form':form}
    if request.method == 'POST':
        form = forms.Search(request.POST)
        if form.is_valid():
            print(form.cleaned_data['vehicle'])
    return render(request, 'search.html', dic)
