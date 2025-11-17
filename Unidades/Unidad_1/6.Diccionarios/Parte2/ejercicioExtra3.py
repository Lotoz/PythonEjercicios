#Para este ejercicio se ha considera que el mes es de 30 dias
#El analisis sera con 4 productos, llamados A, B, C, D
#Empezaremos vendiendolos por 5 dias

#No afecta que sea asi y se ve mejor
ventas = { 
    "A": {1: 5, 2: 3, 3: 6, 4: 8, 5: 1}, 
    "B": {1: 3, 2: 7, 3: 2, 4: 0, 5: 4}, 
    "C": {1: 6, 2: 4, 3: 3, 4: 5, 5: 2}, 
    "D": {1: 0, 2: 2, 3: 1, 4: 3, 5: 0} 
}

# Suma total de un producto
def sumaTotal(buscado):
    return sum(ventas.get(buscado, {}).values())

# Día con mayor venta para un producto (devuelve el número de día)
def diaMayor(buscado):
    dias = ventas.get(buscado, {})
    if not dias:
        return None
    return max(dias.items(), key=lambda kv: kv[1])[0]

# Día con menor venta para un producto (devuelve el número de día)
def diaMenor(buscado):
    dias = ventas.get(buscado, {})
    if not dias:
        return None
    return min(dias.items(), key=lambda kv: kv[1])[0]

# Ventas diarias de un producto (imprime)
def ventasDiarias(buscado):
    dias = ventas.get(buscado, {})
    if not dias:
        print(f'El producto {buscado} no existe o no tiene ventas.')
        return
    print(f'Ventas diarias del producto {buscado}:')
    for ind, numero in sorted(dias.items()):
        print(f'  Dia {ind}: {numero} unidades vendidas')

# Promedio diario de ventas de un producto
def promedioPorDia(buscado):
    dias = ventas.get(buscado, {})
    if not dias:
        return 0.0
    return sum(dias.values()) / len(dias)

# Calculos generales
productos = list(ventas.keys())
totales = {p: sumaTotal(p) for p in productos}

for p in productos:
    total = totales[p]
    dmax = diaMayor(p)
    dmin = diaMenor(p)
    print(f'Ventas totales del producto {p}: {total}, dia mayor: {dmax}, dia menor: {dmin}')

# Producto más y menos vendido (por total)
producto_mas_vendido = max(totales, key=totales.get)
producto_menos_vendido = min(totales, key=totales.get)

print(f'\nEl producto más vendido es {producto_mas_vendido} con {totales[producto_mas_vendido]} unidades.')
print(f'El producto menos vendido es {producto_menos_vendido} con {totales[producto_menos_vendido]} unidades.')

# Mostrar ventas diarias del producto más vendido
ventasDiarias(producto_mas_vendido)

# Promedio por día del producto más vendido
promedio_mas_vendido = promedioPorDia(producto_mas_vendido)
print(f'Promedio diario del producto más vendido ({producto_mas_vendido}): {promedio_mas_vendido:.2f} unidades/día')
