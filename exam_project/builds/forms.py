from django import forms
from .models import PCBuild


class PCBuildForm(forms.ModelForm):
    class Meta:
        model = PCBuild
        fields = [
            'name',
            'description',
            'components',
            'for_sale',
            'image',
        ]
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Short description of the build'
            }),
            'image': forms.URLInput(attrs={
                'placeholder': 'Image URL (optional)'
            }),
        }
        help_texts = {
            'components': 'Select components included in this build',
        }