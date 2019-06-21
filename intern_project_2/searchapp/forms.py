from django import forms


class VehicleSearch(forms.Form):
    vehicle = forms.CharField(required=False)
    customer = forms.FloatField(required=False)
