from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    HomeView,
    CustomLoginView,
    CustomLogoutView,
    SignUp,
    ProfileView,
    EditProfileView,
    UserListView,
    FibonacciView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("accounts/profile/", ProfileView.as_view(), name="profile"),
    path("edit_profile/", EditProfileView.as_view(), name="edit_profile"),
    path("manager/users/", UserListView.as_view(), name="user_list"),
    path("password/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("fibonacci/<int:n>/", FibonacciView.as_view(), name="fibonacci"),
]
