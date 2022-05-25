from django import forms

from website.models import Sales


class AddNewSaleForm(forms.ModelForm):

    class Meta:
        model = Sales
        # fields = '__all__'  # какие поля нужно отобразить в форме (кроме тех, заполняются автоматически)
        fields = [
            'header',
            'text',
            'image_field',
        ]

    widgets = {
        'header': forms.TextInput(attrs={
            'placeholder': "Наименование акции"
        }),
        'text': forms.Textarea(attrs={
            'placeholder': "Текст акции"
        }),
    }
