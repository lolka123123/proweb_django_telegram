from django import forms


class TranslaterForm(forms.ModelForm):
    class Meta:
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
            })
        }