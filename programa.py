#esto es un comentario...

print ("Hola Mnundo!") 
print ("Hola Python!") 
nombre = input("ingrese su nombre: ")
print ("Hola "+nombre)
numero1= 20
numero2 = 43
 
promedio = (numero1+numero1)/2
print ("El promedio es : ", promedio)

costo_servicio = 1000

#me falta calcular los inmpuestos 
# iva21%
costo_servicio_iva = costo_servicio * 0.21
#Pais 8%
costo_servicio_Pais= costo_servicio * 0.08
#ganancia30%
costo_servicio_ganancia= costo_servicio * 0.30
#IIBB CABA2%
costo_servicio_IIBB = costo_servicio * 0.02

valor_final = costo_servicio + costo_servicio_iva+costo_servicio_ganancia+costo_servicio_IIBB+costo_servicio_Pais
print ("El valor final a pagar es", valor_final)