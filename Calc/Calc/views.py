from django.http import response
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def index(request):
    number1 =int(request.GET.get("num1"))
    number2 =int(request.GET.get("num2"))
    operator = request.GET.get("operator")
    answers = {"ans": None}
    if operator == "sum":
        answers["ans"] = number1 + number2
    elif operator == "sub":
        answers["ans"] = number1 - number2
    elif operator == "mul":
        answers["ans"] = number1 * number2
    else:
        answers["ans"] = number1 / number2
        
    return render(request , "index.html", answers)