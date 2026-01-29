from django.shortcuts import redirect,render, get_object_or_404
from inventario.models import Producto

def agregar_producto(request, producto_id):
    # 1. Obtenemos el carrito de la sesión (o creamos uno vacío si no existe)
    carrito = request.session.get('carrito', {})

    # 2. Sumamos el producto al diccionario
    id_str = str(producto_id)
    if id_str in carrito:
        carrito[id_str] += 1
    else:
        carrito[id_str] = 1

    # 3. Guardamos el carrito de nuevo en la sesión
    request.session['carrito'] = carrito
    return redirect('tienda')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos_en_carrito = []
    total_general = 0

    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id)
        subtotal = producto.precio * cantidad
        total_general += subtotal
        
        productos_en_carrito.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal,
        })

    return render(request, 'carrito/carrito.html', {
        'items': productos_en_carrito,
        'total_general': total_general
    })

def eliminar_producto(request, producto_id):
    carrito = request.session.get('carrito', {})
    id_str = str(producto_id)
    if id_str in carrito:
        del carrito[id_str] # Borramos la clave del diccionario
        request.session['carrito'] = carrito
    return redirect('ver_carrito')

def vaciar_carrito(request):
    request.session['carrito'] = {} # Lo reseteamos a un diccionario vacío
    return redirect('ver_carrito')