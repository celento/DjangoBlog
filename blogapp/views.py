from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage


def index(request):
    latest_post_list = Post.objects.order_by('date')[:5]
    all_post_list = Post.objects.all()
    paginator = Paginator(all_post_list, 4)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.page_range)

    context = {'latest_post_list': latest_post_list,
               'page_obj': page_obj}
    return render(request, 'index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'details.html', {'post': post})
