from django import forms
from Stationary.models import Scategory,Sproduct,CartProduct,StatOrder
from users.models import Query

class ScategoryForm(forms.ModelForm):

    class Meta:
        model = Scategory
        fields = '__all__'
class SproductForm(forms.ModelForm):


    class Meta:
        model = Sproduct
        fields='__all__'

class ScategoryDelete(forms.ModelForm):
    class Meta:
        model = Scategory
        fields=('CatName',)

class SproductDelete(forms.ModelForm):
    class Meta:
        model=Sproduct
        fields=('PName',)

class SproductEdit(forms.ModelForm):
    class Meta:
        model=Sproduct
        exclude=('CatId',)

class CartProductForm(forms.ModelForm):
     class Meta:
         model = CartProduct
         exclude=('aggregate',)
class SOrderForm(forms.ModelForm):
     class Meta:
         model = StatOrder
         fields='__all__'
class EditCartProduct1(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields=('quantity',)

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields="__all__"
