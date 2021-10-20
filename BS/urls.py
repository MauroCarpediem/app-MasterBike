
#Rutas de Backstoness


from django.contrib import admin
from django.urls import path, include
from .views import  index, galeria, agendarhora,eliminar ,  informaciones,registrate , regreparacion, tienda ,administracion ,regprod ,cerrar_sesion ,Quienes_somos, sucursal, ficha ,  tipos_bici, login


urlpatterns = [
    path ('', index, name='IND'),
    path ('gale/', galeria, name='GALE' ),
    path ('agenda/',agendarhora, name='AGENDARHORA'),
    path ('info/',informaciones, name='INFO'),
    path ('tienda/',tienda, name='TIENDA'),
    path ('regprod/',regprod, name='REGPROD'),
    path ('Quiene_somos/', Quienes_somos, name='QUIENESSOMOS'),
    path ('sucursal/', sucursal, name='SUCURSAL'),
    path ('tiposBici/', tipos_bici, name='TIPOBICI'),
    path ('login/', login, name= 'LOGIN'),
    path ('cerrar/', cerrar_sesion, name= 'CERRAR'),
    path ('registrate/', registrate, name= 'REGISTRATE'),
    path ('regreparacion/', regreparacion, name= 'REGREPARACION'),
    path ('administracion/', administracion, name= 'ADMINISTRACION'),
    path ('administracion/', administracion, name= 'ADMINISTRACION'),
    path ('ficha/<id>/', ficha, name='FICHA'),
    path ('eliminar/<id>/',eliminar, name='ELIMINAR'),

]
