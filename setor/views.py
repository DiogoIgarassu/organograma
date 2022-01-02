from django.shortcuts import render
from setor.models import Setor

# Create your views here.
def add_setor(request):
    context = {}
    dados = Setor.objects.all()

    if request.method == 'POST':
        updados = dict(request.POST.items())
        print(updados)
        id_setor_imediato = updados['setor_imediato']
        nivel_setor_imediato = Setor.objects.get(id=id_setor_imediato)
        nivel_hierarquia = nivel_setor_imediato.nivel_hierarquia + 1
        setor = Setor.objects.create(
            nome=updados['nome'],
            telefone=updados['telefone'],
            descricao=updados['descricao'],
            secretaria_imediata=updados['secretaria_imediata'],
            setor_imediato=updados['setor_imediato'],
            nivel_hierarquia=nivel_hierarquia,
        )
        setor.save()
    context['dados'] = dados

    return render(request, 'setor/add.html', context)
