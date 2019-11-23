from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from . import views
from .forms import RegistrationForm

app_name="bidding"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('login/',
        auth_views.LoginView.as_view(
            template_name='bidding/login.html',
            authentication_form=AuthenticationForm
        ),
        name="login"),
    path('logout/',
        auth_views.LogoutView.as_view(),
        name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('search/', views.SearchListView.as_view(), name="search"),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name="user"),
    path('item/add/', views.ItemCreateView.as_view(), name="add_item"),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name="item"),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name="delete_item"),
    path('bid/<int:pk>/', views.BidView.as_view(), name="bid")
]