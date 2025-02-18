from django.shortcuts import  render
def html(request):
    return  render(request,"second.html")

def third(request):
    return  render(request,"third.html")