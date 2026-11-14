# Solución de IA - Agente Funcional LogiBot (EP2)
## Descripción
Agente orquestado con LangChain que integra Memoria (ConversationBufferMemory) y Herramientas (Tools) para consultas de pedidos vía API simulada y normativas (RAG).
## Instalación
1. Clonar repo.
2. Crear entorno virtual: `python -m venv venv`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Configurar `.env` con `GOOGLE_API_KEY`.
5. Ejecutar: `python logibot.py`