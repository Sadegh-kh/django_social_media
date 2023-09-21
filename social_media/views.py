from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from social_media.models import Post

from . import forms

# Create your views here.


def home_page(request):
    content = {}
    return render(request, "home.html", content)


def post_list(request, slug_tag=None):
    posts = Post.objects.all()
    if slug_tag != None:
        # set for we don't want dublicate post
        posts = set(Post.objects.filter(tags__slug__icontains=slug_tag))

    context = {
        "tag": slug_tag,
        "posts": posts,
    }
    return render(request, "social/post_list.html", context)


def create_post(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect("social:post_list")
    else:
        form = forms.PostForm()
    context = {"form": form}
    return render(request, "social/forms/create_post.html", context)


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
