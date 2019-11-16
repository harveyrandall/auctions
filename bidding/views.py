from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from django.http import JsonResponse, HttpResponse, QueryDict
from django.core.exceptions import ValidationError
from .models import User, Item, Bid
from .forms import RegistrationForm

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
    pass

class SearchListView(generic.ListView):
    pass

class ItemDetailView(generic.DetailView):
    pass

class BidView(generic.TemplateView):
    pass

class UserDetailView(generic.DetailView):
    pass
