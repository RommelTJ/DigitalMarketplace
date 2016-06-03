from django.shortcuts import render
from django.views.generic import View

from digitalmarketplace.mixins import LoginRequiredMixin
from .forms import NewSellerForm

# Create your views here.

class SellerDashboard(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        form = NewSellerForm(request.POST)
        if form.is_valid():
            print "Make user apply model"
        return render(request, "sellers/dashboard.html", {"form":form})

    def get(self, request, *args, **kwargs):
        form = NewSellerForm()
        return render(request, "sellers/dashboard.html", {"form":form})

