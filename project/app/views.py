from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView, ListView, View
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import UserRegistrationForm, EditProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from .models import CustomUser
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class FibonacciView(View):
    @method_decorator(cache_page(60 * 15))
    def get(self, request, n):
        def fibonacci(n):
            if n <= 1:
                return n
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

        result = fibonacci(n)
        return HttpResponse(f"Fibonacci number for {n} is {result}")


class HomeView(TemplateView):
    template_name = "accounts/home.html"


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("profile")


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")


class SignUp(FormView):
    template_name = "accounts/signup.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend="django.contrib.auth.backends.ModelBackend")
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


class EditProfileView(LoginRequiredMixin, UpdateView):
    form_class = EditProfileForm
    template_name = "accounts/edit_profile.html"

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("profile")


class ManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="Manager").exists()


class UserListView(ManagerRequiredMixin, ListView):
    model = CustomUser
    template_name = "accounts/user_list.html"
    context_object_name = "users"
