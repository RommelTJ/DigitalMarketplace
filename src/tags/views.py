from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from analytics.models import TagView
from .models import Tag

# Create your views here.
class TagDetailView(DetailView):
    model = Tag

    def get_context_data(self, *args, **kwargs):
        context = super(TagDetailView, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated():
            tag = self.get_object()
            TagView.objects.add_count(self.request.user, tag)
        return context

class TagListView(ListView):
    model = Tag

    def get_queryset(self):
        return Tag.objects.filter(active=True)