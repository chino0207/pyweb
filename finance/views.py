from django.shortcuts import render

# Create your views here.
def html(request):
    #AI 財經預測
    return render(request, "finance/finance.html")
