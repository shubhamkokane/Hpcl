from django import forms


class Search(forms.Form):
    vehicle = forms.CharField()
    customer= forms.FloatField()
