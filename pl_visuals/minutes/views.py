# from django.shortcuts import render
# import pandas as pd
# import os
# from django.conf import settings

# from minutes.utils import get_num_matches, get_minutes
# from minutes.plots import plt_minutes


# def home(request):
#     df_comps = pd.read_csv(os.path.join(settings.STATIC_ROOT, "comps_info.csv"))
#     df_comps_mth = pd.read_csv(os.path.join(settings.STATIC_ROOT, "comps_matches.csv"))

#     df_comps = get_minutes(df_comps)
#     mth_comps = get_num_matches(df_comps_mth)

#     graph_path = plt_minutes(df_comps, "Manchester-United", mth_comps, 10260, "comps")

#     return render(request, "minutes/index.html", {"data": graph_path})


from rest_framework import authentication, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.authentication import TokenAuthentication
from .models import Product
from .permissions import IsStaffEditorPermission
from .serializers import ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if not content:
            content = title
        serializer.save(content=content)


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_detail_view = ProductDetailAPIView.as_view()
product_list_create_view = ProductListCreateAPIView.as_view()
product_update_view = ProductUpdateAPIView.as_view()
product_destroy_view = ProductDestroyAPIView.as_view()


# ****** NOT USED ************
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# ****** NOT PREFERRED METHOD ************
@api_view(["GET", "POST"])
def product_alt_view(request, pk=None):
    method = request.method
    if method == "GET":
        if pk:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if not content:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
