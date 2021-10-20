from django.db.models.fields.related import ForeignObject
from django.shortcuts import render
from .models import Categoria, Producto, Arriendo, Reparacion

#IMPORTAR EL MODELO DE TABLA  :  LOGIN
from django.contrib.auth.models import User
#IMPORTAR LIBRERIA PARA AUTENTICAR :  LOGIN
from django.contrib.auth import authenticate, logout, login as login_aut
#IMPORTAR LIBRERIA DECORADORA EVITA INGRESO A PAGINAS SIN AUTORIZACION
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request):
    tipos =  ["asesoria Corte pelo", "Asesoria corte Barba", "Asesoria tratamientos faciales" ]
    productos = Producto.objects.filter(portada=True)
    contexto = {"tipos":tipos, "productos":productos}
    return render(request, "index.html", contexto)

def galeria(request):
    return render(request, "galeria.html")



def informaciones(request):
    return render(request, "informaciones.html")

def tienda(request):
    productos = Producto.objects.filter(publicado=True)
    contexto = {"productos" : productos}
    return render(request, "tienda.html", contexto)

def ficha(request, id):
    productos = Producto.objects.get(nombre=id)
    contexto = {"productos":productos}
    return render(request, "ficha.html", contexto)

def Quienes_somos(request):
    return render(request, "Quienes_somos.html")

def sucursal(request):
    return render(request, "sucursal.html")

def tipos_bici(request):
    return render(request, "tipos_bici.html")

def login(request):
    mensaje= ""
    if request.POST:
        nombre = request.POST.get("txtUsuario")
        contra = request.POST.get("txtPass")
        us = authenticate(request,username=nombre, password=contra)
        if us is not None and us.is_active:
            login_aut(request,us)
            categoria = Categoria.objects.all()
            productos = Producto.objects.filter(portada=True)
            mensaje = "usuario logueado"
            contexto = {"productos":productos,"mensaje":mensaje , "categoria": categoria}
            return render(request, "index.html", contexto)
        else:
            mensaje = "usuario o contrasena incorrecto"
    contexto = {"mensaje":mensaje}
    return render(request, "login.html", contexto)

def cerrar_sesion(request):
    logout(request)
    productos = Producto.objects.filter(portada=True)
    contexto = {"productos":productos}
    return render(request, "index.html", contexto)

def registrate(request):
    mensaje = ""
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        correo = request.POST.get("txtEmail")
        user = request.POST.get("txtUser")
        passw1 = request.POST.get("txtPass1")

        try:
            usu = User.objects.get(username=user)
            mensaje = "usuario ya existe"
        except:
            usu = User()
            usu.first_name = nombre
            usu.last_name = apellido
            usu.email = correo
            usu.username = user
            usu.set_password(passw1)
            usu.save()
            mensaje= "Usuario Registrado"
    contexto = {"mensaje" : mensaje}
    return render(request, "registrate.html", contexto)

##############################
##############################


def regprod(request):
    categorias = Categoria.objects.all()
    contexto = {"categorias" : categorias}

    if request.POST:
        nombre = request.POST.get("txtNombre")
        precio = request.POST.get("txtPrecio")
        desc = request.POST.get("txtDesc")
        foto = request.FILES.get("txtImg")
        cate = "productos"
        obj_categoria = Categoria.objects.get(nombre=cate)

        prod = Producto(
            nombre=nombre,
            precio=precio,
            descripcion=desc,
            foto = foto,
            categoria = obj_categoria
            )
        prod.save()
        contexto = {"categorias" : categorias, "mensaje":"producto grabado"}
    return render(request, "regprod.html", contexto)


def regreparacion(request):
    usuario_actual = request.user.username

    if request.POST:
        usuario  = usuario_actual
        Telefono = request.POST.get("txtTelefono")
        correo = request.POST.get("txtCorreo")
        desc = request.POST.get("txtDesc")
        foto = request.FILES.get("txtImg")
        cate = "Reparacion"
        obj_categoria = Categoria.objects.get(nombre=cate)
        rep = Reparacion(
            usuario = usuario_actual,
            telefono = Telefono,
            correo = correo,
            foto = foto,
            detalle_cliente = desc,
            categoria = obj_categoria
            )
        rep.save()
        mensaje = "Reparacion ingresada, nos pondremos en contacto contigo para coordinar la reparacion."

        contexto  = {"usuario_actual":usuario_actual,"mensaje":mensaje}

    return render(request, "regreparacion.html")


def eliminar (request, id):
    mensaje=""
    try:
        prod = Producto.objects.get(nombre=id)
        prod.delete()
        mensaje="Se elimino producto"
    except:
        mensaje=""

    productos = Producto.objects.all()
    contexto = { "productos": productos, "mensaje":mensaje}
    return render(request, "administracion.html", contexto)


@login_required(login_url='/login/')
def agendarhora(request):
    usuario_actual = request.user.username
    contexto = {"usuario_actual":usuario_actual}

    if request.POST:
        usuario  = usuario_actual
        Telefono = request.POST.get("txtTelefono")
        fecha_arriendo = request.POST.get("cbFecha")
        tipobici = request.POST.get("cboBici")
        cate = "Arriendos"
        obj_categoria = Categoria.objects.get(nombre=cate)
        precio = 1000

        arriendo = Arriendo(
            usuario = usuario_actual,
            telefono = Telefono,
            fecha_arriendo = fecha_arriendo,
            categoria = obj_categoria,
            tipobici= tipobici,
            precio = precio
            )
        arriendo.save()
        contexto = {"usuario_actual":usuario_actual, "mensaje":"Agenda ingresada, puedes venir el dia solicitado a retirar tu MasterBike"}

    return render(request, "agendarhora.html", contexto)

@login_required(login_url='/login/')
def administracion(request):
    usuario_actual = request.user.username
    if usuario_actual == "admin":
        productos = Producto.objects.all()
        arriendos = Arriendo.objects.all()
        reparacion = Reparacion.objects.all()
        contexto = {"productos":productos, "usuario_actual":usuario_actual, "arriendos":arriendos, "reparacion":reparacion}
        return render(request, "administracion.html", contexto)

    else:
        arriendos = Arriendo.objects.filter(usuario=usuario_actual)
        reparacion = Reparacion.objects.filter(usuario=usuario_actual)
        contexto = {"usuario_actual":usuario_actual, "arriendos":arriendos, "reparacion":reparacion}
        return render(request, "administracion.html", contexto)


#def registrarCuenta(reques) / Metodo Pendiente
#def regHora(reques) / Metodo Pendiente
