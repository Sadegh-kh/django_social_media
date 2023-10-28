from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Count
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from social_media.models import Post

from . import forms

# Create your views here.


def home_page(request):
    content = {}
    return render(request, "home.html", content)


def post_list(request, slug_tag=None):
    posts = Post.objects.all()
    if slug_tag is not None:
        # set for we don't want dublicate post
        posts = set(Post.objects.filter(tags__slug__icontains=slug_tag))
        # list for paginator
        posts = list(posts)
    paginator = Paginator(posts, 2)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = []

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return render(request, "social/post_ajax_list.html", {"posts": posts})
    context = {
        "tag": slug_tag,
        "posts": posts,
    }
    return render(request, "social/post_list.html", context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    tags_id = post.tags.values_list("id", flat=True)
    similar_posts = Post.objects.filter(tags__in=tags_id)
    similar_posts = (
        similar_posts.annotate(count_same_tag=Count("tags"))
        .order_by("-count_same_tag", "-created")
        .exclude(id=pk)
    )
    context = {
        "post": post,
        "similar_posts": similar_posts,
    }
    return render(request, "social/post_detail.html", context)


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


# AJAX view


@login_required
@require_POST
def post_like(request):
    post_id = request.POST.get("post_id", None)
    if post_id is not None:
        post = get_object_or_404(Post, id=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
        return JsonResponse({"liked": liked, "like_count": post.likes.count()})
    else:
        return JsonResponse({"error": "post id not found"})
