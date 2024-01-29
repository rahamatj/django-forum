from django.shortcuts import render
from post.models import Post
from django.core.paginator import Paginator

def home_view(request):
    posts_qs = Post.objects.all().order_by('-id')

    paginator = Paginator(posts_qs, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "home-view.html", {"page_obj": page_obj})
