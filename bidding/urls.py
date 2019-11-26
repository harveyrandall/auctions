from django.urls import path, re_path
from django.urls import reverse
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from . import views
from .forms import RegistrationForm

app_name="bidding"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('closed/', views.ClosedView.as_view(), name="closed"),
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
    path('reset/',
        auth_views.PasswordResetView.as_view(
            template_name="bidding/password_reset_form.html",
            email_template_name="bidding/password_reset_email.html",
            html_email_template_name="bidding/password_reset_email.html",
            success_url="/reset/requested"
        ),
        name="password_reset"),
    path('reset/requested',
        auth_views.PasswordResetDoneView.as_view(
            template_name="bidding/password_reset_requested.html",
        ),
        name="password_reset_requested"),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="bidding/password_reset_confirm.html",
            post_reset_login=True,
            success_url="/reset/success"
        ),
        name="password_reset_confirm"),
    path('reset/success',
        auth_views.PasswordResetCompleteView.as_view(
            template_name="bidding/password_reset_complete.html",
        ),
        name="password_reset_complete"),
    path('search/', views.SearchListView.as_view(), name="search"),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name="user"),
    path('item/add/', views.ItemCreateView.as_view(), name="add_item"),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name="item"),
    path('item/<int:pk>/bid/', views.BidCreateView.as_view(), name="bid")
]