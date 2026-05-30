import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos/ventas.csv')

df['total'] = df['cantidad'] * df['precio']

ventas_totales = df['total'].sum()
print(f"Ventas totales: ${ventas_totales:,.0f}")

producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
print(f"Producto mas vendido: {producto_mas_vendido}")

df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.to_period('M')
ventas_por_mes = df.groupby('mes')['total'].sum()
print("\nVentas por mes:")
print(ventas_por_mes)

ventas_por_mes.plot(kind='bar', color='steelblue', figsize=(10,5))
plt.title('Evolucion de Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Total ($)')
plt.tight_layout()
plt.savefig('resultados/grafico_ventas.png')
plt.show()
print("Grafico guardado en resultados/grafico_ventas.png")
