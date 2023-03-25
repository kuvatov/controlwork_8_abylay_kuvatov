from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import SearchForm
from webapp.models import Product
from webapp.models.products import CategoryChoice


class ProductListView(ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = 'products'
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value().capitalize()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        categories = CategoryChoice.choices
        context['categories'] = categories
        context['form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)

        if self.search_value:
            query = Q(name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = CategoryChoice.choices
        context['categories'] = categories
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "product/product_create.html"
    fields = ["name", "category", "description", "image"]
    success_url = reverse_lazy("product_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "product/product_update.html"
    fields = ["name", "category", "description", "image"]
    success_url = reverse_lazy("product_list")

    def get_success_url(self):
        return reverse('product_details', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product

    def get(self, request, *args, **kwargs):
        return self.delete(request)

    def get_success_url(self):
        return reverse('product_list')
