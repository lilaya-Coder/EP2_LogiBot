# agent.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.memory import ConversationBufferMemory
from tools import consultar_estado_pedido, consultar_garantias_rag, derivar_soporte_humano

# 1. Cargar variables de entorno
load_dotenv()

# 2. Inicializar el LLM y la Memoria (Corto Plazo)
llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# 3. Lista de Herramientas disponibles
tools = [consultar_estado_pedido, consultar_garantias_rag, derivar_soporte_humano]

# 4. Crear el Prompt del Agente (Reglas de comportamiento)
prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres LogiBot, asistente técnico de LogiTech Chile S.A. Resuelve dudas usando tus herramientas. Siempre basa tus respuestas en los datos recuperados."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# 5. Configurar el Agente
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)

# --- PRUEBA DEL AGENTE ---
if __name__ == "__main__":
    print("--- INICIANDO LOGIBOT ---")
    
    # Interacción 1
    print("\n[Cliente]: Hola, mi pedido es el ORD-123. Llegó ayer pero la pantalla está rota.")
    respuesta_1 = agent_executor.invoke({"input": "Hola, mi pedido es el ORD-123. Llegó ayer pero la pantalla está rota."})
    print(f"\n[LogiBot]: {respuesta_1['output']}\n")
    
    # Interacción 2 (Prueba de Memoria)
    print("\n[Cliente]: ¿Qué producto era exactamente y cubre la garantía esto?")
    respuesta_2 = agent_executor.invoke({"input": "¿Qué producto era exactamente y cubre la garantía esto?"})
    print(f"\n[LogiBot]: {respuesta_2['output']}\n")