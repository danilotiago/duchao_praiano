from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
import bcrypt

from clientes.models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'idade', 'email', 
        'senha', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado']

def cliente_list(request, template_name='clientes/cliente_list.html'):
    cliente = Cliente.objects.all()
    data = {}
    data['object_list'] = cliente
    return render(request, template_name, data)

def cliente_view(request, pk, template_name='clientes/cliente_details.html'):
    cliente= get_object_or_404(Cliente, pk=pk)    
    return render(request, template_name, {'object':cliente})

def cliente_create(request, template_name='clientes/cliente_new.html'):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.instance.senha = bcrypt.hashpw(form.cleaned_data['senha'].encode('utf8'), bcrypt.gensalt())
        form.save()
        return redirect('cliente_list')
    return render(request, template_name, {'form':form})

def cliente_update(request, pk, template_name='clientes/cliente_update.html'):
    cliente= get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.instance.senha = bcrypt.hashpw(form.cleaned_data['senha'].encode('utf8'), bcrypt.gensalt())
        form.save()
        return redirect('cliente_list')
    return render(request, template_name, {'form':form})

def cliente_delete(request, pk, template_name='clientes/cliente_confirm_delete.html'):
    cliente= get_object_or_404(Cliente, pk=pk)    
    if request.method=='POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, template_name, {'object':cliente})