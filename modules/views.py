from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class ModulesView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        itens = [{'id': 1, 'nome': 'Item 1'}, {'id': 2, 'nome': 'Item 2'}]
        return Response(itens)

    def post(self, request):
        novo_item = {'id': 3, 'nome': 'Novo Item'}
        return Response({'mensagem': 'Item criado com sucesso!', 'item': novo_item}, status=201)

    def put(self, request):
        id_item = request.POST.get('id')
        item_atualizado = {'id': id_item, 'nome': 'Item Atualizado'}
        return Response({'mensagem': 'Item atualizado com sucesso!', 'item': item_atualizado})

    def delete(self, request):
        id_item = request.POST.get('id')
        return Response({'mensagem': 'Item removido com sucesso!', 'id': id_item}, status=204)
