from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class MyView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"message":"Hello World"})

class GoodMorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"message":"Good Morning"})

class GoodEveningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"message":"Good Evening"})

class GoodNightView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"message":"Good Night"})

class AddView(APIView):
    def post(self,request,*args,**kwargs):
        n1=int(request.data.get("num1"))
        n2=int(request.data.get("num2"))
        res=n1+n2
        return Response({"message":res})

class SubtractionView(APIView):
    def post(self,request,*args,**kwargs):
        n1=int(request.data.get("num1"))
        n2=int(request.data.get("num2"))
        res=n1-n2
        return Response({"message":res})

class MultiplicationView(APIView):
    def post(self,request,*args,**kwargs):
        n1=int(request.data.get("num1"))
        n2=int(request.data.get("num2"))
        res=n1*n2
        return Response({"message":res})

class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("number"))
        res=n**3
        return Response({"message":res})

class FactorialView(APIView):
    def post(self,request,*args,**kwargs):
        num=int(request.data.get("number"))
        def fact(n):
            if n==1:
                return 1
            else:
                return n*fact(n-1)
        res=fact(num)
        return Response({"message":res})

class PrimeOrNotView(APIView):
    def post(self,request,*args,**kwargs):
        num=int(request.data.get("number"))
        def prime(n):
            flag = 0
            for i in range(2, n):
                if (n % i == 0):
                    flag = 1
                    break
            if flag == 1 or n<2:
                return "Not prime"
            else:
                return "Prime"
        res=prime(num)
        return Response({"message":res})




