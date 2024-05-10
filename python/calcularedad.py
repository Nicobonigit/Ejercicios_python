#Calcular la Edad en Años a partir de la Fecha de Nacimiento

from datetime import date

def calc_edad_annos(fechadenacimiento):
    fechaactual = date.today()
    resultado = fechaactual.year - fechadenacimiento.year
    resultado -= ((fechaactual.month, fechaactual.day )<(fechadenacimiento.month, fechadenacimiento.day))
    return resultado
#En el parentesis se ingresa la fecha de nacimiento 
fechanacimientoingresa = date (1986, 1, 20)
edad= calc_edad_annos(fechanacimientoingresa)

print ("La persona tiene",(edad),"años de edad")


