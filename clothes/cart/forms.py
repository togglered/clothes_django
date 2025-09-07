from django import forms

from main.models import ProductSize, Order


class AddToCartForm(forms.Form):
    size = forms.ModelChoiceField(
        queryset=ProductSize.objects.none(),
        empty_label="Выберите размер"
    )

    def __init__(self, product, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['size'].queryset = product.sizes.all()

    
class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'city', 'street', 'house', 'flat', 'email']
