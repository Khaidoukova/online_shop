from django import forms
from catalog.models import Product, Version

forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    version = forms.ModelChoiceField(queryset=Version.objects.all(), empty_label=None, label='Версия продукта')
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', 'preview')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if cleaned_data in forbidden_words:
            raise forms.ValidationError('Вы вводите запрещенные слова')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        if cleaned_data in forbidden_words:
            raise forms.ValidationError('Вы вводите запрещенные слова')

        return cleaned_data



class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

