from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.models import Review, Product


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['text', 'rating']
    template_name = 'review/review_create.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        form.instance.product = product
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.kwargs['pk']})


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['text', 'rating']
    template_name = 'review/review_update.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.product.pk})


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review

    def get(self, request, *args, **kwargs):
        return self.delete(request)

    def get_success_url(self):
        return reverse('product_list')
