# 🧾 Juridico API – Protocolo Gerador com Django + OpenAI

Este é um projeto de API em Python usando **Django** e **Django REST Framework** que permite gerar **protocolos jurídicos automatizados** (ex: exoneração de pensão alimentícia) a partir de dados estruturados enviados por POST. A formatação dos textos é feita via integração com a **API da OpenAI (GPT-4/3.5)**.

---

## 🚀 Tecnologias Utilizadas

- **Django 5.2**
- **Django REST Framework**
- **OpenAI SDK**
- **httpx** para requisições assíncronas
- **Pydantic** para validação (back-end futuro ou compatibilidade com FastAPI)
- **Python 3.11+**

---

## 🛠️ Instalação

```bash
git clone https://github.com/seu-usuario/juridico-api.git
cd juridico-api

# Crie e ative um ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrations
python manage.py migrate

# Inicie o servidor
python manage.py runserver