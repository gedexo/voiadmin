from datetime import datetime, timedelta

from apis.models import *
from django.http.response import Http404
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class AdminCategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = AdminCategorySerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.all()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AdminCategoryRetriveSerializer
        return AdminCategorySerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class AdminSubcategoryViewset(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = AdminSubcategorySerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.all()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)


class AdminSubSubcategoryViewset(viewsets.ModelViewSet):
    # define queryset
    queryset = SubSubCategory.objects.all()
    # specify serializer to bce used
    serializer_class = AdminSubSubcategorySerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.all()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()


class AdminOptionsViewset(viewsets.ModelViewSet):
    # define queryset
    queryset = Options.objects.all()
    # specify serializer to bce used
    serializer_class = AdminoptionsSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.all()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()


class AdminOffersaleViewset(viewsets.ModelViewSet):
    # define queryset

    queryset = Products.objects.filter(offers__OfferEuro__gt=0)
    # specify serializer to bce used
    serializer_class = AdminproductSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.all()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()


class AdminNewArrivalsViewset(viewsets.ModelViewSet):
    queryset = NewCollection.objects.all()
    serializer_class = AdminNewCollectionSerializer

    def get_queryset(self):
        return self.queryset.all()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()

    def get_serializer_class(self):
        if self.action == "create":
            return AdminNewCollectionCreateSerializer
        return AdminNewCollectionSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class AdminTrendingProductViewset(viewsets.ModelViewSet):
    queryset = BottomProductDisplay.objects.all()
    serializer_class = AdminTrendingProductSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.all()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()

    def get_serializer_class(self):
        if self.action == "create":
            return AdminTrendingProductCreateSerializer
        return AdminTrendingProductSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class AdminNewCollectionViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = AdminproductSerializer

    def get_queryset(self):
        productIds = []
        if NewCollection.objects.filter().exists():
            newcollection = NewCollection.objects.all()
            for new in newcollection:
                productIds.append(new.product_id)
        return self.queryset.filter(id__in=productIds)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.all()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()


class AdminProductsViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = AdminproductSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.all()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()


class DeleteCategory(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response({"msg": "success"})


class DeleteSubCategory(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return SubCategory.objects.get(pk=pk)
        except SubCategory.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        subcategory = self.get_object(pk)
        subcategory.delete()
        return Response({"msg": "success"})


class DeleteSubSubCategory(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return SubSubCategory.objects.get(pk=pk)
        except SubSubCategory.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        subsubcategory = self.get_object(pk)
        subsubcategory.delete()
        return Response({"msg": "success"})


class DeleteProduct(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response({"msg": "success"})


class DeleteOption(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Options.objects.get(pk=pk)
        except Options.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        option = self.get_object(pk)
        option.delete()
        return Response({"msg": "success"})


class DeleteSize(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Sizes.objects.get(pk=pk)
        except Sizes.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        size = self.get_object(pk)
        size.delete()
        return Response({"msg": "success"})


class DeleteBrand(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        brand = self.get_object(pk)
        brand.delete()
        return Response({"msg": "success"})


class AdminBrandViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Brand.objects.all()
    # specify serializer to be used

    serializer_class = AdminBrandSerializer


class AdminSizeViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Sizes.objects.all()
    # specify serializer to be used

    serializer_class = AdminSizesSerializer


class AdminAddOfferViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Offer.objects.all()
    # specify serializer to be used

    serializer_class = AdminAddOfferSerializer


class AdminOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    # specify serializer to be used

    serializer_class = OrderListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer
        ## Need Optimization

        return OrderListSerializer


class ProductsNameIdViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsNameIdserializer
