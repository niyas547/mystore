from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from mobile.models import mobiles
# Create your views here.
class MobileViews(APIView):
    def get(self,request,*args,**kwargs):
        all_mobiles=mobiles
        if "display" in request.query_params:
            disp=request.query_params.get("display")
            all_mobiles=[mob for mob in all_mobiles if mob.get("display")==disp]
        if "brand" in request.query_params:
            brand=request.query_params.get("brand")
            all_mobiles=[mob for mob in all_mobiles if mob.get("brand")==brand]
        if "band" in request.query_params:
            band=request.query_params.get("band")
            all_mobiles=[mob for mob in all_mobiles if mob.get("band")==band]
        return Response({"mobiles":all_mobiles})

    def post(self,request,*args,**kwargs):
        data=request.data
        mobiles.append(data)
        return Response({"mobiles":"mobile added"})

class MobileDetailViews(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        mobile=[mob for mob in mobiles if mob.get("id")==id].pop()
        return Response({"mobile":mobile})
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        update_data=request.data
        mobile=[mob for mob in mobiles if mob.get("id")==id].pop()
        mobile.update(update_data)
        return Response({"mobiles":"mobile updated"})
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        mobile_delete=[mob for mob in mobiles if mob.get("id")==id].pop()
        mobiles.remove(mobile_delete)
        return Response({"mobile":"mobile deleted"})