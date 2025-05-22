from django.shortcuts import render

# protocolos/views.py
import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProtocoloInputSerializer

openai.api_key = 'SUA_CHAVE_DA_OPENAI'

class GerarProtocoloView(APIView):
    def post(self, request):
        serializer = ProtocoloInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        prompt = f"""
Crie um protocolo jurídico de ação de exoneração de pensão alimentícia com base nos dados:
- Autor: {data['nome_autor']} ({data['cpf_autor']}), residente em {data['endereco_autor']}.
- Réu: {data['nome_reu']}, nascido em {data['data_nascimento_reu']}.
- Processo anterior: {data['processo_anterior']}, percentual fixado: {data['percentual_pensao']}.
- Valor da causa: R$ {data['valor_causa']}.
- Vara: {data['numero_vara']} da Comarca de {data['comarca']}.
- Advogada: {data['nome_advogada']}, OAB {data['oab']}, endereço: {data['endereco_advogada']}.
- Honorários: {data['honorarios']}.

Formate como uma petição inicial jurídica completa.
"""

        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        return Response({"protocolo_formatado": completion.choices[0].message.content})

