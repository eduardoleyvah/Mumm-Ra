# -*- coding: utf-8 -*-
from lettuce import step, world
from Edad import Edad

@step(u'cuando realizo la operación')
def cuando_realizo_la_operacion(step):
    pass

@step(u'Dado que ingreso el numero "([^"]*)"')
def dado_que_ingreso_el_numero_group1(step, num1):
    world.cal = Edad()
    world.cal.edad(int(num1))

@step(u'entonces la etapa sera "([^"]*)"')
def entonces_la_etapa_sera_group1(step, esperado):
    assert esperado == world.cal.obtener_resultado(),'El resultado esperado es ' +esperado+ ' y el obtenido es ' +str(world.cal.obtener_resultado())