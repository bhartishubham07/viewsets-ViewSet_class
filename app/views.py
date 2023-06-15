from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework.viewsets import ViewSet
from app.models import *
from app.serializers import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@permission_classes([IsAuthenticated])
class ProductCrudVS(ViewSet):
    def list(self, request):
        PQS = Product.objects.all()
        PSD = ProductSerializer(PQS, many=True)
        return Response(PSD.data)
    
    def create(self, request):
        SD = ProductSerializer(data=request.data)
        if SD.is_valid():
            SD.save()
            return Response({'SUCCESS':'Product Created Successfully!'})
        else:
            return Response({'FAILED': 'Something went wrong while creating the product.'})
        
    def retrieve(self, request, pk):
        PQS = Product.objects.get(pk=pk)
        PSD = ProductSerializer(PQS)
        return Response(PSD.data)
    
    def update(self, request, pk):
        PO = Product.objects.get(pk=pk)
        SPD = ProductSerializer(PO, data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'SUCCESS': 'Product Updated Successfully!'})
        else:
            return Response({'FAILED': 'Something went wrong while updating the product.'})
        
    def partial_update(self, request, pk):
        PO = Product.objects.get(pk=pk)
        SPD = ProductSerializer(PO, data=request.data, partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'SUCCESS': 'Product Partial-Updated Successfully!'})
        else:
            return Response({'FAILED': 'Something went wrong while partially updating the product.'})
        
    def destroy(self, request, pk):
        Product.objects.get(pk=pk).delete()
        return Response({'SUCCESS':'Product Deleted Successfully!'})