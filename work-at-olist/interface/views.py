from django.shortcuts import render
from .models import Channel, Category


def channel_list(request):
    channels = Channel.objects.all
    return render(request, 'interface/channel_list.html', {'channels': channels})

def category_list(request):
    categories = Category.objects.all
    return render(request, 'interface/category_list.html', {'categories': categories})
