from django import forms
from .models import Component


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = [
            'brand',
            'category',
            'tags',
            'price',
            'image',]

        widgets = {
            'image': forms.URLInput(attrs={
                'placeholder': 'Image URL (optional)'
            }),
        }

        help_texts = {
            'category': 'Select component type (CPU, GPU, RAM, etc.)',
            'tags': 'Used for filtering builds',}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['brand'].disabled = True

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError('Price must be a positive number.')
        return price