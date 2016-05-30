import datetime
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import View
from django.shortcuts import render

# Create your views here.

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
