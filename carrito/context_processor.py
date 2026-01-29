def importe_total_carrito(request):
    total = 0
    if 'carrito' in request.session:
        for key, value in request.session['carrito'].items():
            total += value
    return {'cantidad_carrito': total}