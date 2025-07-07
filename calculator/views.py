from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.http import HttpResponse

def home(request):
    result = None
    error = None

    if request.method == 'POST':
        try:
            a = float(request.POST.get('Num1'))
            b = float(request.POST.get('Num2'))
            op = request.POST.get('Op')

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                if b != 0:
                    result = a / b
                else:
                    error = "Cannot divide by zero"
            else:
                error = "Invalid operation"

            if error:
                return render(request, 'home.html', {'error': error})
            else:
                return render(request, 'result.html', {'result': result})

        except ValueError:
            return render(request, 'home.html', {'error': 'Please enter valid numbers'})

    return render(request, 'home.html')

def hello(request):
    return HttpResponse("helloworld")