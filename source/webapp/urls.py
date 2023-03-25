from django.urls import path

from webapp.views.products import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from webapp.views.reviews import ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/detail", ProductDetailView.as_view(), name="product_detail"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path('product/<int:pk>/review/create', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/update', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete', ReviewDeleteView.as_view(), name='review_delete'),
]
