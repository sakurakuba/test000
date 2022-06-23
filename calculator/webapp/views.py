from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def res(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        n1 = int(request.POST.get('number1'))
        n2 = int(request.POST.get('number2'))
        op = request.POST.get('calc')
        print(n1, n2, op)
        x = calc(n1, n2, op)

        context = {
            'number1': request.POST.get('number1'),
            'number2': request.POST.get('number2'),
            'calc': request.POST.get('calc'),
            'result': x
        }
        return render(request, 'result.html', context)


def calc(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return round(n1 / n2, 2)
