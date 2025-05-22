# protocolos/serializers.py
from rest_framework import serializers

class ProtocoloInputSerializer(serializers.Serializer):
    nome_autor = serializers.CharField()
    cpf_autor = serializers.CharField()
    endereco_autor = serializers.CharField()
    nome_reu = serializers.CharField()
    data_nascimento_reu = serializers.DateField()
    processo_anterior = serializers.CharField()
    percentual_pensao = serializers.CharField()
    valor_causa = serializers.DecimalField(max_digits=10, decimal_places=2)
    numero_vara = serializers.CharField()
    comarca = serializers.CharField()
    nome_advogada = serializers.CharField()
    oab = serializers.CharField()
    endereco_advogada = serializers.CharField()
    honorarios = serializers.CharField()