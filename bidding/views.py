from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from django.http import JsonResponse, HttpResponse, QueryDict
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.functions import Now
from .models import User, Item, Bid
from .forms import RegistrationForm, ItemCreateForm, BidCreateForm

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
        return context

    def get_queryset(self, **kwargs):
        return self.model.objects.filter(end_time__gt=Now())

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

class ItemDeleteView(generic.DeleteView):
    pass

class BidView(LoginRequiredMixin, generic.CreateView):
    login_url = "/login"
    model = Bid
    form_class = BidCreateForm
    template_name = "bidding/bid.html"

    def get_context_data(self, **kwargs):
        print(dir(self))

