import datetime
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import View
from django.shortcuts import render

from billing.models import Transaction
from products.models import Product, MyProducts
from digitalmarketplace.mixins import AjaxRequiredMixin

# Create your views here.

class CheckoutAjaxView(AjaxRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return JsonResponse({}, status=403)
        user = request.user
        product_id = request.POST.get("product_id")
        exists = Product.objects.filter(id=product_id).exists()
        if not exists:
            return JsonResponse({}, status=404)
        try:
            product_obj = Product.object.get(id=product_id)
        except:
            product_obj = Product.objects.filter(id=product_id).first()

        # run transaction
        # Assume it's succesful
        trans_obj = Transaction.objects.create(
            user=user,
            product=product_obj,
            price=product_obj.get_price,
        )

        my_products = MyProducts.objects.get_or_create(user=user)[0]
        my_products.products.add(product_obj)

        download_link = product_obj.get_download()
        preview_link = download_link + "?preview=True"

        data = {
            "download": download_link,
            "preview": preview_link,
        }
        return JsonResponse(data)

class CheckoutTestView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            if not request.user.is_authenticated():
                data = {
                    "works": False,
                }
                return JsonResponse(data, status=403)
            data = {
                "works": True,
                "time": datetime.datetime.now(),
            }
            return JsonResponse(data)
        else:
            return HttpResponse("Hello there")

    def get(self, request, *args, **kwargs):
        template = "checkout/test.html"
        context = {}
        return render(request, template, context)
