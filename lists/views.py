from django.http import HttpResponse
from django.shortcuts import redirect, render

from lists.models import Item


def home_page(request):
    return render(request, 'home.html')


def view_lists(request):
    '''представление списка'''
    all_items = Item.objects.all()
    return render(request, 'list.html', {'items': all_items})


def new_list(request):
    '''новый список'''
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/personal-list/')
