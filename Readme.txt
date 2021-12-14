
Programa desarrollado en python 3.8.12, con el uso de las librerías request y pprint. 

En el primer commit se desarrollo la funcion de listado de organizaciones en el script Practica_2_1410767.py . 
En lineas generales se realiza la solicitud tipo GET y su resultado se pasa a formato json. Posterior a realizar la verificaciones
de errores se almacena en una lista todos los nombres de las organizaciones. La funcion retorna dicha lista y ademas se realiza el print
de la verificacion de errores. 


El script Practica_2_Inventario_1410767 contiene la funcion que realiza el inventario. Para esto se realiza la solicitud get correspondiente y se comparan los valores del key productType;
separando asi aquellos dispositivos del tipo wireless y appliance. Posterior a esto se organiza la informacion que se desea en el inventario con un ciclo for. Finalemente se realiza la escritura 
del inventario en un archivo .csv con ayuda de la libreria del mismo nombre. 