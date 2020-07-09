from django.contrib import admin
from users.models import MyUser,Student,card,Query,mobile
from Student.models import Documents
from Canteen.models import Ccategory,Cproduct,CatOrder,CatOrderDetails,CartProduct,CatOrder,CatOrderDetails,Mydetails
from Stationary.models import Scategory,Sproduct,StatOrder,StatOrderDetails,CartProduct
from Library.models import BookCategory,Stream,Book,BookCart,BookStock,LibraryOrder,LibOrderDetails
from Librarian.models import BookCategory1,Stream1,Book1,BookStock1,BookCart1,LibraryOrder1,LibOrderDetails1,ReturnBook
admin.site.register(Query)
admin.site.register(card)
admin.site.register(mobile)
admin.site.register(Documents)
admin.site.register(Ccategory)
admin.site.register(Cproduct)
admin.site.register(CartProduct)
admin.site.register(CatOrder)
admin.site.register(Mydetails)
admin.site.register(CatOrderDetails)
admin.site.register(Scategory)
admin.site.register(Sproduct)
admin.site.register(StatOrder)
admin.site.register(StatOrderDetails)
admin.site.register(BookCategory)
admin.site.register(Stream)
admin.site.register(Book)
admin.site.register(BookCart)
admin.site.register(BookStock)
admin.site.register(LibraryOrder)
admin.site.register(LibOrderDetails)
admin.site.register(BookCategory1)
admin.site.register(Stream1)
admin.site.register(Book1)
admin.site.register(BookStock1)
admin.site.register(BookCart1)
admin.site.register(LibraryOrder1)
admin.site.register(LibOrderDetails1)
admin.site.register(ReturnBook)
admin.site.register(MyUser)
admin.site.register(Student)
