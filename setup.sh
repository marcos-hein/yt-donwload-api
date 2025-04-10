#!/bin/bash

APP_MODULE="app.main:app"
DEFAULT_PORT=8000

echo "📁 Verificando ambiente virtual..."
if [ ! -d "venv" ]; then
    echo "🔧 Ambiente virtual não encontrado. Criando..."
    python3 -m venv venv || { echo "❌ Erro ao criar venv"; exit 1; }
else
    echo "✅ Ambiente virtual encontrado."
fi

echo "📦 Ativando ambiente virtual..."
source venv/bin/activate || { echo "❌ Erro ao ativar venv"; exit 1; }

echo "📋 Verificando requirements.txt..."
if [ -f "requirements.txt" ]; then
    echo "📥 Instalando dependências..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "⚠️ Arquivo requirements.txt não encontrado. Pulando instalação de dependências."
fi

# Função para verificar se uma porta está em uso
porta_em_uso() {
    lsof -i :$1 &> /dev/null
    return $?
}

PORTA_ESCOLHIDA=$DEFAULT_PORT

if porta_em_uso $DEFAULT_PORT; then
    echo "⚠️ Porta $DEFAULT_PORT já está em uso."
    for i in {8001..8010}; do
        if ! porta_em_uso $i; then
            PORTA_ESCOLHIDA=$i
            echo "✅ Usando porta alternativa: $PORTA_ESCOLHIDA"
            break
        fi
    done
fi

echo "🚀 Iniciando servidor Uvicorn em http://localhost:$PORTA_ESCOLHIDA ..."
uvicorn $APP_MODULE --reload --port $PORTA_ESCOLHIDA
