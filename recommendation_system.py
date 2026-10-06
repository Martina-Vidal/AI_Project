"""Recomienda productos según la categoría y el presupuesto del usuario."""


# Catálogo de ejemplo incluido directamente en este archivo.
PRODUCTOS = [
	{"nombre": "Auriculares inalámbricos", "categoria": "electrónica", "precio": 45.99},
	{"nombre": "Altavoz portátil", "categoria": "electrónica", "precio": 32.50},
	{"nombre": "Teclado mecánico", "categoria": "electrónica", "precio": 79.00},
	{"nombre": "Botella reutilizable", "categoria": "hogar", "precio": 18.99},
	{"nombre": "Lámpara de escritorio", "categoria": "hogar", "precio": 27.50},
	{"nombre": "Manta de algodón", "categoria": "hogar", "precio": 35.00},
	{"nombre": "Mochila urbana", "categoria": "accesorios", "precio": 42.00},
	{"nombre": "Gafas de sol", "categoria": "accesorios", "precio": 29.99},
]


def recomendar_productos(categoria, presupuesto):
	"""Devuelve hasta tres productos que cumplen los criterios indicados."""
	coincidencias = [
		producto
		for producto in PRODUCTOS
		if producto["categoria"] == categoria and producto["precio"] <= presupuesto
	]

	# Los productos más económicos aparecen primero.
	return sorted(coincidencias, key=lambda producto: producto["precio"])[:3]


def main():
	"""Solicita los criterios al usuario y muestra las recomendaciones."""
	categorias = sorted({producto["categoria"] for producto in PRODUCTOS})
	print("Categorías disponibles: " + ", ".join(categorias))
	categoria = input("¿Qué categoría te interesa? ").strip().lower()

	try:
		presupuesto = float(input("¿Cuál es tu presupuesto? ").strip())
		if presupuesto < 0:
			print("El presupuesto no puede ser negativo.")
			return
	except ValueError:
		print("Introduce un presupuesto válido usando un número.")
		return

	recomendaciones = recomendar_productos(categoria, presupuesto)
	if recomendaciones:
		print("\nRecomendaciones:")
		for producto in recomendaciones:
			print(f"- {producto['nombre']}: ${producto['precio']:.2f}")
	else:
		print("No se encontraron productos para esa categoría y presupuesto.")


if __name__ == "__main__":
	main()
