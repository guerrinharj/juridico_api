from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProtocoloInputSerializer

from dotenv import load_dotenv
from openai import OpenAI
from rest_framework import status
from openai import OpenAIError
import os

# Carrega variáveis de ambiente do .env
load_dotenv()

# Instancia o client da OpenAI com a chave
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # use o modelo ao qual você tem acesso
                messages=[{"role": "user", "content": prompt}]
            )
            return Response({
                "protocolo_formatado": response.choices[0].message.content
            })

        except OpenAIError as e:
            return Response({
                "erro": "Erro ao gerar protocolo com a OpenAI.",
                "detalhes": str(e)
            }, status=status.HTTP_429_TOO_MANY_REQUESTS)