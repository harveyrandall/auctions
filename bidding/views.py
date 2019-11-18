from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from django.http import JsonResponse, HttpResponse, QueryDict
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from .models import User, Item, Bid
from .forms import RegistrationForm, ItemCreateForm

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

class RegisterView(generic.CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "bidding/register.html"

    def form_valid(self, form):
        self.success_url = "/"
        return super(RegisterView, self).form_valid(form)

class UserItemListView(generic.ListView):
    model = User
    template_name = "bidding/user_item_history.html"
    context_object_name = 'items'

    def get_queryset(self, **kwargs):
        u = self.model.objects.get(pk=self.kwargs.get('pk'))
        return u.item_set.all()

class UserBidListView(CurrentUserMixin, generic.ListView):
    model = User
    permission_denied_message = "You can't view other people's bid history!"
    template_name = "bidding/user_bid_history.html"
    context_object_name = "bids"

    def get_queryset(self, **kwargs):
        u = self.model.objects.get(pk=self.kwargs.get('pk'))
        return u.bid_set.all()

class SearchListView(generic.ListView):
    pass

class ItemCreateView(LoginRequiredMixin, generic.CreateView):
    model = Item
    form_class = ItemCreateForm
    template_name = "bidding/add_item.html"


class ItemDetailView(generic.DetailView):
    pass

class ItemDeleteView(generic.DeleteView):
    pass

class BidView(LoginRequiredMixin, generic.TemplateView):
    login_url = "/login"

class UserDetailView(generic.DetailView):
    pass
