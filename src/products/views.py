import os
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from mimetypes import guess_type
from wsgiref.util import FileWrapper

from digitalmarketplace.mixins import LoginRequiredMixin, MultiSlugMixin, SubmitButtonMixin
from models import Product
from mixins import ProductManagerMixin
from forms import ProductAddForm, ProductModelForm

class ProductCreateView(LoginRequiredMixin, SubmitButtonMixin, CreateView):
    model = Product
    template_name = "form.html"
    form_class = ProductModelForm
    # success_url = "/products/"
    submit_button = "Add Product"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        valid_data = super(ProductCreateView, self).form_valid(form)
        form.instance.managers.add(user)
        # Add all default users
        return valid_data

    # def get_success_url(self):
    #     return reverse("products:list")

class ProductUpdateView(ProductManagerMixin, SubmitButtonMixin, MultiSlugMixin, UpdateView):
    model = Product
    template_name = "form.html"
    form_class = ProductModelForm
    # success_url = "/products/"
    submit_button = "Update Product"

class ProductDetailView(MultiSlugMixin, DetailView):
    model = Product

class ProductDownloadView(MultiSlugMixin, DetailView):
    model = Product

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj in request.user.myproducts.products.all():
            filepath = os.path.join(settings.PROTECTED_ROOT, obj.media.path)
            guessed_type = guess_type(filepath)[0]
            wrapper = FileWrapper(file(filepath))
            mimetype = "application/force-download"
            if guessed_type:
                mimetype = guessed_type
            response = HttpResponse(wrapper, content_type=mimetype)

            if not request.GET.get("preview"):
                response["Content-Disposition"] = "attachment; filename=%s" %(obj.media.name)

            response["X-SendFile"] = str(obj.media.name)
            return response
        else:
            raise Http404

class ProductListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(**kwargs)
        query = self.request.GET.get("q")
        qs = qs.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).order_by("title")
        return qs


# Create your views here.
def create_view(request):
    # FORM
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data.get("publish"))
        instance = form.save(commit=False)
        instance.sale_price = instance.price
        instance.save()
    template = "form.html"
    context = {
        "form": form,
        "submit_button": "Create Product",
    }
    return render(request, template, context)

def detail_slug_view(request, slug=None):
    try:
        product = get_object_or_404(Product, slug=slug)
    except Product.MultipleObjectsReturned:
        product = Product.objects.filter(slug=slug).order_by("-title").first()
    template = "detail_view.html"
    context = {
        "object": product,
    }
    return render(request, template, context)

def detail_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    template = "detail_view.html"
    context = {
        "object": product,
    }
    return render(request, template, context)

def update_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    form = ProductModelForm(request.POST or None, instance=product)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    template = "form.html"
    context = {
        "object": product,
        "form": form,
        "submit_button": "Update Product",
    }
    return render(request, template, context)

def list_view(request):
    #list of items
    print(request.user)
    query_set = Product.objects.all()
    template = "list_view.html"
    context = {
        "query_set": query_set
    }
    return render(request, template, context)