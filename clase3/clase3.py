#conversores
peso = float(input("Ingrese valor de peso en Kg: "))

#1 kg = 2.2046 lb 
libra_kilo = 2.2046 
peso_libras = peso * libra_kilo
peso_auto = float(input("Ingrese valor de peso del auto en Kg: "))
peso_auto_libras = peso * libra_kilo

print("El valor del peso explesado en Kg es: ", peso)
print("El valor del peso explesado en Lb es: ", peso_libras)
