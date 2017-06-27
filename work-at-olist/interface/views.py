from django.shortcuts import render
from .models import Channel, Category


def channel_list(request):
    channels = Channel.objects.order_by('name')
    return render(request, 'interface/channel_list.html', {'channels': channels})


def category_list(request):
    categories = Category.objects.order_by('name')
    return render(request, 'interface/category_list.html', {'categories': categories})
