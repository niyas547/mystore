from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from mobapi.seriallizers import MobileSerializer
from mobapi.models import Mobiles
from mobapi.seriallizers import MobileModelSerializer

# Create your views here.
class MobileView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        if "brand" in request.query_params:
            qs=qs.filter(brand=request.query_params.get("brand"))
        if "band" in request.query_params:
            qs=qs.filter(band=request.query_params.get("band"))
        if "name" in request.query_params:
            qs=qs.filter(name__contains=request.query_params.get("name"))

        serializer=MobileSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            Mobiles.objects.create(**serializer.validated_data)
            return Response(data=serializer.validated_data)
        else:
            return Response(data=serializer.errors)

class MobileDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileSerializer(qs)
        return Response(data=serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.filter(id=id)
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            qs.update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        qs.delete()
        return Response({"message":"mobile deleted"})




        # qs.name=serializer.validated_data.get("name")
        # qs.brand=serializer.validated_data.get("brand")
        # qs.band=serializer.validated_data.get("band")
        # qs.display=serializer.validated_data.get("display")
        # qs.price=serializer.validated_data.get("price")
        # qs.rating=serializer.validated_data.get("rating")
        # qs.save()

class MobileModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        serializer=MobileModelSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=MobileModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
class MobileModelDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(qs)
        return Response(data=serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        qs.delete()
        return Response({"message":"mobile deleted"})