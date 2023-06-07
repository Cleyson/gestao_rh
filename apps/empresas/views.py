from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa
from ..funcionarios.models import ListView


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']


    def form_valid(self, form):
        object = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = object
        funcionario.save('none')
        return HttpResponse('OK')


class EmpresaEdit(UpdateView):
        model = Empresa
        fields = ['nome']


class EmpresaList(ListView):
    model = Empresa
    fields = ['nome']