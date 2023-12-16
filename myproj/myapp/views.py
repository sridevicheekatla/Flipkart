import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


class ProcessProductSpecView(APIView):
    def get(self, request):
        try:
            json_data = product_spec_list = fit_found = fabric_val = ideal_val = None

            model_dict = {
                'Regular Fit': RegularFit,
                'Relaxed Fit': RelaxedFit
            }

            products = AllProducts.objects.filter(active=True)

            for product in products:
                product_spec = product.product_specifications

                if product_spec and not product_spec == '{"product_specification"=>nil}':
                    json_data = json.loads(product_spec.replace("=>", ":"))

                if isinstance(json_data, dict):
                    product_spec_list = json_data.get('product_specification')

                if product_spec_list:
                    for spec in product_spec_list:
                        if isinstance(spec, dict):
                            if spec.get('key') == 'Fit' and spec.get('value') in ["Regular Fit", "Relaxed Fit"]:
                                fit_found = True

                        if fit_found:
                            for fit_found_product in product_spec_list:
                                if fit_found_product.get('key') == 'Fabric':
                                    fabric_val = fit_found_product.get('value')

                                if fit_found_product.get('key') == 'Ideal For':
                                    ideal_val = fit_found_product.get('value')

                            if fabric_val and ideal_val:
                                model_dict[spec.get('value')].objects.create(
                                    fabric=fabric_val,
                                    ideal_for=ideal_val
                                )

                                fit_found = False
                                product.active = False
                                product.save()
            return Response({"result": "Data uploaded successfully"}, status=200)

        except Exception as e:
            return Response({"result": f"Data failed to upload, Error: {str(e)}"}, status=500)


class FitListView(APIView):
    def get(self, request):
        kwargs = request.query_params.get("type_of_fit")
        model_dict = {
            'relaxed': {'model': RelaxedFit, 'serializer': RelaxedFitSerializer},
            'regular': {'model': RegularFit, 'serializer': RegularFitSerializer}
        }
        if kwargs in ['relaxed', 'regular']:
            queryset = model_dict[kwargs]['model'].objects.all()
            serializer = model_dict[kwargs]['serializer'](queryset, many=True)
        else:
            return Response(status=400)
        return Response(serializer.data, status=200)
