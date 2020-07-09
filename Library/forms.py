from django import forms
from Library.models import BookCategory,Stream,Book,BookStock,LibraryOrder


class BookCategoryForm(forms.ModelForm):

    class Meta:
        model = BookCategory
        fields = '__all__'

class StreamForm(forms.ModelForm):
    class Meta:
        model=Stream
        fields='__all__'

class StreamEditForm(forms.ModelForm):
    class Meta:
        model=Stream
        exclude=('BookCatId',)

class AddBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"

class EditBookForm(forms.ModelForm):
    class Meta:
        model=Book
        exclude=('BookCatId','StreamId','BookId',)


class BookStockForm(forms.ModelForm):
    class Meta:
        model=BookStock
        fields=("BookId","BookStockSerial","Issued",)
class LibOrderForm(forms.ModelForm):
    class Meta:
        model=LibraryOrder
        fields="__all__"
