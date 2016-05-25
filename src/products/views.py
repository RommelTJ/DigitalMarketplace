from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from digitalmarketplace.mixins import MultiSlugMixin, SubmitButtonMixin
from models import Product
from forms import ProductAddForm, ProductModelForm

class ProductCreateView(SubmitButtonMixin, CreateView):
    model = Product
    template_name = "form.html"
    form_class = ProductModelForm
    success_url = "/products/"
    submit_button = "Add Product"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        valid_data = super(ProductCreateView, self).form_valid(form)
        form.instance.managers.add(user)
        # Add all default users
        return valid_data

class ProductUpdateView(SubmitButtonMixin, MultiSlugMixin, UpdateView):
    model = Product
    template_name = "form.html"
    form_class = ProductModelForm
    success_url = "/products/"
    submit_button = "Update Product"

    def get_object(self, *args, **kwargs):
        user = self.request.user
        obj = super(ProductUpdateView, self).get_object(*args, **kwargs)
        if obj.user == user or user in obj.managers.all():
            return obj
        else:
            raise Http404

class ProductDetailView(MultiSlugMixin, DetailView):
    model = Product

class ProductListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(**kwargs)
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