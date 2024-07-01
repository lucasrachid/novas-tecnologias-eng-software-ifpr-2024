from django.http import JsonResponse
from django.views import View

class ModulesView(View):

    def get(self, request):
        itens = [{'id': 1, 'nome': 'Item 1'}, {'id': 2, 'nome': 'Item 2'}]
        return JsonResponse({'itens': itens})

    def post(self, request):
        novo_item = {'id': 3, 'nome': 'Novo Item'}
        return JsonResponse({'mensagem': 'Item criado com sucesso!', 'item': novo_item}, status=201)

    def put(self, request):
        id_item = request.POST.get('id')
        item_atualizado = {'id': id_item, 'nome': 'Item Atualizado'}
        return JsonResponse({'mensagem': 'Item atualizado com sucesso!', 'item': item_atualizado})

    def delete(self, request):
        id_item = request.POST.get('id')
        return JsonResponse({'mensagem': 'Item removido com sucesso!', 'id': id_item}, status=204)
