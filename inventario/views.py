from django.shortcuts import render, get_object_or_404, redirect # Importamos redirect aquí
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Producto 

# 1. Vista de la Tienda Principal
def lista_productos(request):
    productos = Producto.objects.all() 
    return render(request, 'inventario/tienda.html', {'productos': productos})

# 2. Vista del Detalle del Producto
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'inventario/detalle.html', {'producto': producto})

# 3. Vista de Registro de Usuarios
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ya puedes iniciar sesión.')
            return redirect('login') # Ahora sí funcionará porque importamos 'redirect'
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})