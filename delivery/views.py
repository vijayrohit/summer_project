from django import forms
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'delivery/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'delivery/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-cateringDate']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    #fields = ['orderSource','houseAccount', 'name', 'address', 'mobile', 'deliverydriver', 'deliverytime', 'specialInstruction', 'cateringAmount', 'deliveryFee', 'tips', 'salesTax', 'customerFeedBack', 'onTime', 'deliveryStatus', 'customerPaymentStatus', 'employeePaymentStatus', 'cateringDate', 'commissionAmount', 'commissionStatus', 'estimatedDelivery']


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    fields = ['orderSource','houseAccount', 'name', 'address', 'mobile', 'deliverydriver', 'deliverytime', 'specialInstruction', 'cateringAmount', 'deliveryFee', 'tips', 'salesTax', 'customerFeedBack', 'onTime', 'deliveryStatus', 'customerPaymentStatus', 'employeePaymentStatus', 'cateringDate', 'commissionAmount', 'commissionStatus', 'estimatedDelivery']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['orderSource','houseAccount', 'name', 'address', 'mobile', 'deliverydriver', 'deliverytime', 'specialInstruction', 'cateringAmount', 'deliveryFee', 'tips', 'salesTax', 'customerFeedBack', 'onTime', 'deliveryStatus', 'customerPaymentStatus', 'employeePaymentStatus', 'cateringDate', 'commissionAmount', 'commissionStatus', 'estimatedDelivery']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        #if self.request.user == post.author:
        #    return True
        return True


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        #if self.request.user == post.author:
        #    return True
        return True


def about(request):
    return render(request, 'delivery/about.html', {'title': 'About'})
