from django.core.paginator import Paginator
from django.conf import settings


def paginator(posts, request):
    paginator = Paginator(posts, settings.MAX_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
