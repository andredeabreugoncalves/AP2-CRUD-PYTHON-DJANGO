from django.shortcuts import render, redirect
from app.forms import MotosForm, clienteForm
from app.models import Motos, cliente
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Motos.objects.filter(modelo__icontains=search)
        data['db'] = Motos.objects.filter(marca__icontains=search)
        data['db'] = Motos.objects.filter(ano__icontains=search)

    else:
        data['db'] = Motos.objects.all()
    return render(request, 'index.html', data)

def pagcliente(request):
    data = {}
    searchcliente = request.GET.get('searchcliente')
    if searchcliente:
        data['db'] = cliente.objects.filter(nome__icontains=searchcliente)
        data['db'] = cliente.objects.filter(cidade__icontains=searchcliente)


    else:
        data['db'] = cliente.objects.all()
    return render(request, 'pagcliente.html', data)

def pagvenda(request):
    data = {}
    data['db'] = Motos.objects.all()
    return render(request, 'pagvenda.html', data)

def pagvendacliente(request):
    data = {}
    data['db'] = cliente.objects.all()
    return render(request, 'pagvenda.html', data)


def form(request):
    data = {}
    data ['form'] = MotosForm()
    return render(request, 'form.html', data)

def formcliente(request):
    data = {}
    data ['form'] = clienteForm()
    return render(request, 'formcliente.html', data)

def create(request):
    form = MotosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def createcliente(request):
    form = clienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pagcliente')

def view(request, pk):
    data = {}
    data['db'] = Motos.objects.get(pk=pk)
    return render(request, 'view.html', data)

def viewcliente(request, pk):
    data = {}
    data['db'] = cliente.objects.get(pk=pk)
    return render(request, 'viewcliente.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Motos.objects.get(pk=pk)
    data['form'] = MotosForm(instance=data['db'])
    return render(request, 'form.html', data)

def editcliente(request, pk):
    data = {}
    data['db'] = cliente.objects.get(pk=pk)
    data['form'] = clienteForm(instance=data['db'])
    return render(request, 'formcliente.html', data)

def update(request, pk):
    data = {}
    data['db'] = Motos.objects.get(pk=pk)
    form = MotosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def updatecliente(request, pk):
    data = {}
    data['db'] = cliente.objects.get(pk=pk)
    form = clienteForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('pagcliente')


def delete(request, pk):
    db = Motos.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def deletecliente(request, pk):
    db = cliente.objects.get(pk=pk)
    db.delete()
    return redirect('pagcliente')




