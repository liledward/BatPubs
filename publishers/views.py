from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .forms import PublisherCreateForm
from .models import Publisher, Category
#from django.views.generic.list import ListView

from .models import Publisher
# Create your views here.


class PublisherListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Publisher.objects.filter(Q(category__iexact=slug))
        else:
            queryset = Publisher.objects.all()
        return queryset.order_by("traffic")


class PublisherDetailView(DetailView):
    queryset = Publisher.objects.all()


class PublisherCreateView(CreateView):
    form_class = PublisherCreateForm
    template_name = 'publishers/form.html'
    success_url = '/publishers/'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Publisher.objects.filter(
            category__title__iexact='website').order_by('traffic')[:10]
        return super(PublisherCreateView, self).get_context_data(**kwargs)


class PublisherUpdateView(UpdateView):
    model = Publisher
    fields = ['name', 'category', 'description', ]
    template_name = 'publishers/update.html'
    success_url = '/'


class CategoryListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("title")
        if slug:
            queryset = Publisher.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = Category.objects.all()
        return queryset


class PubCategoryListlView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        queryset = Publisher.objects.all().filter(category__title__iexact=slug)
        return queryset
