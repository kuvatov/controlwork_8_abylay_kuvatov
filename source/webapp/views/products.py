from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = "products"
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"
    context_object_name = "product"


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
