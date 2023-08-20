from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, members


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    pto = members.objects.all()
    return render(request, "index.html", {'result': obj, 'work': pto})

#
# def about(request):
#     return render(request, 'about.html')
#
#
# def contact(request):
#     return HttpResponse("hello world")
#
#
# def addition(request):
#     one = int(request.GET['num1'])
#     two = int(request.GET['num2'])
#
#     ans1 = one + two
#     ans2 = one - two
#     ans3 = one / two
#     ans4 = one * two
#
#     return render(request, 'result.html', {'addition': ans1, 'subtraction': ans2, 'division': ans3, 'multiply': ans4})
