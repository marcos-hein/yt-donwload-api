#!/bin/bash

echo "🔧 Criando ambiente virtual..."
python3 -m venv venv

echo "✅ Ambiente virtual criado!"

echo "📦 Ativando o ambiente virtual..."
source venv/bin/activate

echo "📥 Instalando dependências do projeto..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Instalação concluída!"

echo "🚀 Iniciando servidor com Uvicorn na porta 5000..."
uvicorn app.main:app --reload --port 5000
