from django.conf import settings
from django.core.paginator import Paginator


def paginator_func(posts, request):
    page_obj = Paginator(
        posts,
        settings.MAX_PAGE
    ).get_page(request.GET.get('page'))
    return page_obj
