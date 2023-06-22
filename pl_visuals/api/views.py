from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from minutes.models import Product
from minutes.serializers import ProductSerializer


# @api_view(["GET"])
# def api_home(request):
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#     return Response(data)


@api_view(["POST"])
def api_home(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        return Response(serializer.data)
