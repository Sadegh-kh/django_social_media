from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.urls import is_valid_path, reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.


class SignUpView(CreateView):
    form_class = forms.SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("accounts:login")


def profile_view(request):
    context = {}
    return render(request, "registration/profile.html", context)


def edit_user_view(request):
    user = get_user_model().objects.get(username=request.user.username)
    if request.method == "POST":
        form = forms.EditUserForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
    else:
        form = forms.EditUserForm(instance=user)
    context = {"form": form}
    return render(request, "registration/edit_user.html", context)
