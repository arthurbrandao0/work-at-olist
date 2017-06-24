from django.shortcuts import render


def channel_list(request):
    return render(request, 'interface/channel_list.html', {})
