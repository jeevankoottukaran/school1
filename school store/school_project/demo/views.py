from django.shortcuts import render

# Create your views here.
def demo1(request):
    return render(request,'base.html')