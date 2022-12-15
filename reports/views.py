from django.shortcuts import render
from django.http import HttpResponse
from .models import MobileList

# Create your views here.
def index(request):
    data=MobileList.objects.all()
    context={
        'data':data,
    }
    return render(request,'index.html',context)