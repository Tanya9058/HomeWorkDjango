from django.urls import path
from One.views import MyClass, MyClassTwo

urlpatterns =[
    path('', MyClass.as_view()),  # статус-код 400
    # path('', MyClassTwo.as_view())  # статус-код 201
]