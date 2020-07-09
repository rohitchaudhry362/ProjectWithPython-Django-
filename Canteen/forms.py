from django import forms
from django.forms import ModelForm
from Canteen.models import Ccategory,Cproduct,CartProduct,CatOrder
from users.models import Query



class CcategoryForm(forms.ModelForm):

    class Meta:
        model = Ccategory
        fields = '__all__'
class CproductForm(forms.ModelForm):


    class Meta:
        model = Cproduct
        fields='__all__'

class CcategoryDelete(forms.ModelForm):
    class Meta:
        model=Ccategory
        fields=('CatName',)

class CproductDelete(forms.ModelForm):
    class Meta:
        model=Cproduct
        fields=('PName',)

class CproductEdit(forms.ModelForm):
    class Meta:
        model=Cproduct
        exclude=('CatId',)

class CartProductForm(forms.ModelForm):
    class Meta:
        model = CartProduct
        exclude=('aggregate',)

class CatOrderForm(forms.ModelForm):
     class Meta:
         model = CatOrder
         fields='__all__'
class EditCartProduct(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields=('quantity',)
class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields="__all__"
