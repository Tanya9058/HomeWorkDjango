from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class MyClass(View):
    def get(self, request):
        return HttpResponse(status=400)


class MyClassTwo(View):
    def get(self, request):
        return HttpResponse(status=201)