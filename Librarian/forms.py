from django import forms
from Librarian.models import BookCategory1,Stream1,Book1,BookStock1,LibraryOrder1,ReturnBook,FineAmount1
from users.models import Query

class BookCategoryForm(forms.ModelForm):

    class Meta:
        model = BookCategory1
        fields = '__all__'

class StreamForm(forms.ModelForm):
    class Meta:
        model=Stream1
        fields='__all__'

class StreamEditForm(forms.ModelForm):
    class Meta:
        model=Stream1
        exclude=('BookCatId',)

class AddBookForm(forms.ModelForm):
    class Meta:
        model=Book1
        fields="__all__"

class EditBookForm(forms.ModelForm):
    class Meta:
        model=Book1
        exclude=('BookCatId','StreamId','BookId',)

class BookStockForm(forms.ModelForm):
    class Meta:
        model=BookStock1
        fields=("BookId","BookStockSerial","Issued",)

class LibOrderForm(forms.ModelForm):
    class Meta:
        model=LibraryOrder1
        fields="__all__"

class ReturnForm(forms.ModelForm):
    class Meta:
        model=ReturnBook
        fields="__all__"

class FineAmountForm(forms.ModelForm):
    class Meta:
        model=FineAmount1
        fields="__all__"
class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields="__all__"
