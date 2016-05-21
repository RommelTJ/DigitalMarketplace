from django.http import Http404
from django.shortcuts import render, get_object_or_404
from models import Product
from forms import ProductAddForm, ProductModelForm

# Create your views here.
def create_view(request):
    # FORM
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data.get("publish"))
        instance = form.save(commit=False)
        instance.sale_price = instance.price
        instance.save()
    template = "create_view.html"
    context = {
        "form": form,
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

def list_view(request):
    #list of items
    print(request.user)
    query_set = Product.objects.all()
    template = "list_view.html"
    context = {
        "query_set": query_set
    }
    return render(request, template, context)