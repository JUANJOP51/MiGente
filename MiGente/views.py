from pipes import Template
from django.http import HttpResponse
from django.template import loader 

def miTemplate1(self):
    name='Patricia'
    par='esposa'
    act='comerciante'
    diccionario={'nombre':name, 'actividad':act, 'parentesco': par}
    plantilla=loader.get_template('template2.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def miTemplate2(self):
    name='Mauro'
    par='hijo Mayor'
    act='profesor de Educacion Fisica'
    diccionario={'nombre':name, 'actividad':act, 'parentesco': par}
    plantilla=loader.get_template('template3.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def miTemplate3(self):
    name='Facundo'
    par='hijo Menor'
    act='Marketing'
    diccionario={'nombre':name, 'actividad':act, 'parentesco': par}
    plantilla=loader.get_template('template3.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)
