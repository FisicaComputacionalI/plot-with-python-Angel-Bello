#Python usa librerias como matplotlib con objetos predeterminados como pyplot que tienen propiedades que permiten enviar las instrucciones $
import matplotlib.pyplot as plt
#Construimos el objeto plt introduciendo valores que se grafican contra el numero de entrada. Por ejemplo si queremos graficar el crecimien$
plt.plot([5,3,3,4,3,3,8,3,4,6,8,10,13,13,13,13,15,15,15,15,15,15,15,15,16,16,16,17,18,18])
#Con esta isntruccion colocamos un titulo al eje Y de la grafica.
plt.ylabel('cousins and brothers')
plt.xlabel('Years')
#Con esta isntruccion guardamos la imagen con el formato que queramos.
plt.savefig('tarea1.png')
#Con esta instruccion mostramos la figura.
plt.show()



