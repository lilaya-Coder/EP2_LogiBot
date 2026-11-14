# tools.py
from langchain.tools import tool

@tool
def consultar_estado_pedido(order_id: str) -> str:
    """Útil para consultar el estado y fecha de entrega de un pedido usando su ID (ej. ORD-123)."""
    # Base de datos simulada
    pedidos = {
        "ORD-123": "Entregado el 10-11-2026. Producto: Monitor LG.",
        "ORD-456": "En ruta. Entrega estimada: 15-11-2026. Producto: Teclado Mecánico."
    }
    return pedidos.get(order_id, "Pedido no encontrado en la base de datos transaccional.")

@tool
def consultar_garantias_rag(consulta: str) -> str:
    """Útil para buscar normativas de garantías, devoluciones o daños en tránsito en los manuales PDF."""
    # Simulación de la base vectorial (ChromaDB)
    if "roto" in consulta.lower() or "daño" in consulta.lower() or "tránsito" in consulta.lower():
        return "[Fuente: manual_garantias.pdf - Pág 4] Los daños en tránsito tienen cobertura total si se reportan dentro de los 5 días posteriores a la fecha de entrega."
    return "[Fuente: manual_garantias.pdf - Pág 1] Todos los productos tienen 6 meses de garantía legal."

@tool
def derivar_soporte_humano(motivo: str) -> str:
    """Útil SOLAMENTE cuando la solicitud del cliente no puede ser resuelta por las políticas o requiere intervención de un supervisor."""
    return f"Ticket creado exitosamente para el equipo humano. Motivo de derivación: {motivo}."