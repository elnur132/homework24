from django.shortcuts import render
from .models import Page
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = Page.objects.all()
    paginator = Paginator(data, 2)

    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {
        'page':page
    }
    return render(request, 'home.html', context)