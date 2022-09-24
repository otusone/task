from itertools import product
from traceback import print_tb
from turtle import title
from unicodedata import name
from django.shortcuts import render
from cherrypicker import CherryPicker
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CreateProductSerializer, AddVarientSerializer
from .models import Product, Varients

# Create your views here.

def errors(b):
    picker = CherryPicker(b).flatten().get()    
    kk = {}
    for i,j in picker.items():
        td = i.count("_")
        if td>1:
            b = i.index("_")   
            c = i.index("_",b+1)
            kk[i[:c]] = j
        else:
            b= i.index("_")
            kk[i[:b]] = j
    return kk

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def index(request):
    return Response({'msg':'sucess'})

@api_view(["POST"])
def create(request):
    serializer = CreateProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save() 
        return Response({"success": True})
    kk = errors(serializer.errors)
    return Response({"result":{"errors":kk}})

@api_view(["POST"])
def addvarient(request):
    p_name = request.data['product_name']
    if not p_name:
        return Response({"result":{"errors":"please Enter Product Name First"}})
    pk = Product.objects.get(name = p_name)
    serializer = AddVarientSerializer(data=request.data)
    if serializer.is_valid():
        g = serializer.save() 
        g.product_name = pk
        g.save()
        return Response({"success": True})

    kk = errors(serializer.errors)
    return Response({"result":{"errors":kk}})

@api_view(["GET"])
def singleproduct(request, name=None):
    variants = []
    try:
        obj = Product.objects.get(name=name)
        pr = Product.objects.filter(name=name).values()[0]
    except:
        return Response({"error": "product does not exists"})
    try:
        vr = Varients.objects.filter(product_name=obj)
        for i in vr:
            variant = {}
            variant['title'] = i.title
            variant['availableStock'] = i.availableStock
            variants.append(variant)
    except:
        variants = []
    pr['variants'] = variants
    return Response(pr)

@api_view(["POST"])
def listall(request):
    result = []
    fil = dict(request.data)
    ab = list(fil.keys())[0]
    if ab == 'name':
        pr = Product.objects.filter(name=fil[ab][0]).values()
    elif ab == 'status':
        pr = Product.objects.filter(status=fil[ab][0]).values()
    elif ab == 'class':
        pr = Product.objects.filter(class_name=fil[ab][0]).values()
    else:
        return Response({"success": "product does not Exists"})
    for i in pr:
        result.append({"id":i["id"], "name":i["name"],"status":i["status"]})
    return Response(result)

@api_view(["PATCH"])
def update(request, name=None):
    try:
        pr = Product.objects.get(name=name)
    except:
        return Response({"error": "product does not exists"})
    ser = CreateProductSerializer(pr, data=request.data, partial=True)
    if ser.is_valid():
        ser.save()
        return Response({"success": True})
    kk = errors(ser.errors)
    return Response({"result":{"errors":kk}})



@api_view(["DELETE"])
def delete_product(request, name=None):
    try:
        pr = Product.objects.get(name=name)
    except:
        return Response({"error": "product does not exists"})
    pr.delete()
    return Response({"success": True})

@api_view(["DELETE"])
def delete_variant(request, name=None, title=None):
    try:
        pr = Product.objects.get(name=name)
    except:
        return Response({"error": "product does not exists"})
    try:
        vr = Varients.objects.get(product_name=pr, title = title)
    except:
        return Response({"error": "title does not exists"})
    vr.delete()
    return Response({"success": True})