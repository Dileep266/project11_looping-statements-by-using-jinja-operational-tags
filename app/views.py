from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'name':'dileep'}
    return render(request,'forloop.html',d)
