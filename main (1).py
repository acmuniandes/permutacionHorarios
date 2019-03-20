import json
import itertools, operator
from datetime import datetime

#Abrir el archivo de cursos y asignarlo a la variable data
with open('./courses.json', 'r', encoding="latin-1") as f:
  data = json.load(f)
  data = data['records']

#Agregar una llave a cada objeto para buscar más facil
#La llave es el departamento+el curso
#Ej: ADMI1101
for x in data:
  x['curso'] = x['class']+x['course']
#Input del usuario
#Cada curso debe estar seguido por coma sin espacios
#ISIS1001,ISIS1104,ISIS1105
cursos = input('Nombre curso: ')
#Split del input
arr = cursos.split(',')
arrMaterias = []

#Recorrido de los cursos para agregar todas las secciones de cada materia en ArrMaterias
for x in arr:
  aux = []
  for b in data:
      if(x==b['curso']):
          aux.append(b)
  arrMaterias.append(aux)
  aux = []
#Combinatoria de n cursos que esten en arrMaterias
nArr = list(itertools.product(*arrMaterias))#Aun no hace nada este metodo xd
def conflictosHorario(combinaciones):
  #print(combinaciones[0][0])
    pass

def cambioFormato(combinaciones):
  for tupla in combinaciones:
      for materia in tupla:
          horarios = []
          for horario in materia["schedules"]:
              aux = {}
              fechaInicio = horario["date_ini"]
              fechaFin = horario["date_fin"]
              horaInicio = horario["time_ini"]
              horaInicioN = horaInicio[:2]+':'+ horaInicio[-2:]
              horaFin = horario["time_fin"]
              horaFinN = horaFin[:2]+':'+ horaFin[-2:]
              fechaInicioHoraInicio = datetime.strptime(fechaInicio+' '+horaInicioN,'%d-%b-%y %H:%M')
              fechaInicioHoraFin = datetime.strptime(fechaInicio + ' ' + horaFinN,'%d-%b-%y %H:%M')
              fechaFinHoraInicio = datetime.strptime(fechaFin + ' ' +horaInicioN,'%d-%b-%y %H:%M')
              fechaFinHoraFin =datetime.strptime(fechaFin + ' ' + horaFinN,'%d-%b-%y %H:%M')
              aux['fechaInicioHoraInicio'] = fechaInicioHoraInicio
              aux['fechaInicioHoraFin'] = fechaInicioHoraFin
              aux['fechaFinHoraInicio'] = fechaFinHoraInicio
              aux['fechaFinHoraFin'] = fechaFinHoraFin
              horarios.append(aux)
          materia['horarios'] = horarios

def arreglo(*kwargs):
    #print(len(kwargs[0]['nrc']))
    pass

def darSinCruces(combinaciones):
    retorno = []
    sirve = True
    for tupla in combinaciones:
        count = 0
        sirve = True
        for i in range(0, len(tupla)):
            tuplaI = tupla[i]
            for j in range(len(tupla)-1, i, -1):
                tuplaJ = tupla[j]
                for x in tuplaI['horarios']:
                    for b in tuplaJ['horarios']:
                        if(not((x['fechaInicioHoraInicio']>=b['fechaInicioHoraFin']) or (x['fechaInicioHoraFin'] <= b['fechaInicioHoraInicio']))):
                            count = count + 1
        if(count>0):
            retorno.append(tupla)
            
    return retorno
cambioFormato(nArr)
sinCruces = list(darSinCruces(nArr))
print(len(sinCruces[0]))
for x in range(0, len(sinCruces)):
    #print(sinCruces[x])
    pass
conflictosHorario(nArr)