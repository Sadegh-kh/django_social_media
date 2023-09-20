from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from social_media.models import Post

from . import forms

# Create your views here.


def home_page(request):
    content = {}
    return render(request, "home.html", content)


def post_list(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "social/post_list.html", context)


def ticket(request):
    if request.method == "POST":
        form = forms.TicketForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = f'{request.user.username} from {cd["email"]}\n {cd["message"]}'
            send_mail(
                cd["subject"],
                message,
                settings.EMAIL_HOST_USER,
                [settings.RECIPIENT_ADDRESS],
            )
            return redirect("home")

    else:
        form = forms.TicketForm()
    context = {"form": form}
    return render(request, "social/forms/ticket.html", context)
