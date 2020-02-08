from django import forms

from .models import Delivery_memory, Descent_memory


class DeliveryMemoryForm(forms.ModelForm):
    class Meta:
        model = Delivery_memory
        fields = ['product', 'quantity', 'supply']
        widgets = {'supply': forms.HiddenInput()}

class DescentMemoryForm(forms.ModelForm):
    class Meta:
        model = Descent_memory
        fields = ['product', 'quantity', 'descent']
        widgets = {'descent': forms.HiddenInput()}


