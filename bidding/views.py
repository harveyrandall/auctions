from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views import generic
from django.http import JsonResponse, HttpResponse, QueryDict
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Max
from django.db.models.functions import Now
from .models import User, Item, Bid
from .forms import RegistrationForm, ItemCreateForm, BidCreateForm
import decimal

# Mixins
class CurrentUserMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or kwargs.get('pk', None) != request.user.pk:
            self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

# Create your views here.
class IndexView(generic.ListView):
    model = Item
    template_name = 'bidding/index.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': "All open auctions",
            'no_items': "No open auctions right now!"
        })
        return context

    def get_queryset(self, **kwargs):
        return self.model.objects.filter(end_time__gt=Now())

class ClosedView(generic.ListView):
    model = Item
    template_name = 'bidding/index.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': "All closed auctions",
            'no_items': "No closed auctions yet!"
        })
        return context

    def get_queryset(self, **kwargs):
        return self.model.objects.filter(end_time__lte=Now())


class RegisterView(generic.CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "bidding/register.html"

    def form_valid(self, form):
        self.success_url = "/"
        return super(RegisterView, self).form_valid(form)

class UserDetailView(CurrentUserMixin, generic.DetailView):
    model = User
    permission_denied_message = "You can't look at other people's account!"
    template_name = "bidding/user.html"
    context_object_name = "user"

class SearchListView(generic.ListView):
    model = Item
    template_name = "bidding/search.html"
    context_object_name = "items"

    def get_queryset(self, **kwargs):
        searchterm = self.request.GET.get('search')
        if searchterm:
            self.template_name = "bidding/search_results.html"
            return (self.model.objects.filter(item_name__icontains=searchterm) | self.model.objects.filter(item_description__icontains=searchterm))
        return self.model.objects.all()

class ItemCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Item
    form_class = ItemCreateForm
    template_name = "bidding/add_item.html"
    success_url = "/"
    success_message = "Item posted successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

class ItemDetailView(generic.DetailView):
    model = Item
    template_name = "bidding/item.html"
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_bid = self.model.objects.get(pk=self.kwargs.get('pk')).current_bid
        if current_bid and (self.request.user == current_bid.get('user')):
            context.update({
                'current_highest': True
            })
        return context

class BidCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    login_url = "/login"
    model = Item
    form_class = BidCreateForm
    template_name = "bidding/bid.html"
    success_message = "Bid made successfully."

    def get_initial(self):
        return {
            'user': self.request.user,
            'item': self.model.objects.get(pk=self.kwargs.get('pk'))
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_bid = self.model.objects.get(pk=self.kwargs.get('pk')).current_bid
        context.update({
            'bid': Bid.highest_bid(self.kwargs.get('pk')),
            'redirect': self.get_success_url()
        });
        if self.request.user == self.model.objects.get(pk=self.kwargs.get('pk')).user:
            context.update({
                'owner': True
            })
        elif current_bid and (self.request.user == current_bid.get('user')):
            context.update({
                'current_highest': True
            })
        return context

    def get_success_url(self):
        return self.request.GET.get('next', "/")
