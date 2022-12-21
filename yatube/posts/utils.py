from django.conf import settings
from django.core.paginator import Paginator


def make_paginate(posts, request):
    return Paginator(
        posts,
        settings.POSTS_LIMIT_PER_PAGE
    ).get_page(request.GET.get('page'))
