from django.shortcuts import render

# Create your views here.
def agent(request):
    d={'name':'Syeraa','id':'007'}
    return render(request,'agent.html',context= d)