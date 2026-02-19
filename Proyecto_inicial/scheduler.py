import time
import schedule

from scripts.extractor import WeatherstackExtractor  # ajusta si tu clase se llama distinto

def ejecutar_etl():
    print("⏳ Ejecutando ETL...")
    extractor = WeatherstackExtractor()
    extractor.ejecutar_extraccion()  # ajusta si tu método se llama distinto
    print("✅ ETL finalizado.")

# Cada 1 hora
schedule.every(1).hours.do(ejecutar_etl)

# (Opcional) ejecutar una vez al iniciar
ejecutar_etl()

print("🟢 Scheduler corriendo. Se ejecutará cada 1 hora.")

while True:
    schedule.run_pending()
    time.sleep(60)
