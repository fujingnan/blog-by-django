from django.shortcuts import render

# Create your views here.

def pos_list(request):
    return render(request, 'blog/pos_list.html', {})