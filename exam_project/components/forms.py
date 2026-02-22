from django import forms
from .models import Component


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = [
            'brand',
            'price',
            'category',
            'tags',
            'image',
        ]
        widgets = {
            'image': forms.URLInput(attrs={
                'placeholder': 'Enter image URL (optional)'
            })
        }
        help_texts = {
            'category': 'Select the component type (CPU, GPU, RAM, etc.)',
            'tags': 'Optional tags used for filtering',
            'image': 'Optional - URL to component image',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['brand'].disabled = True

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError('Price must be a positive number.')
        return price