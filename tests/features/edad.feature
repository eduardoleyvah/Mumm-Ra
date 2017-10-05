Feature: Etapa segun la edad
    Como usuario de la calculadora
    deseo realizar el calculo de una edad
    para obtener uno de los resultados posibles

    Scenario: Edad de -1
        Dado que ingreso el numero "-1"
        cuando realizo la operación
        entonces la etapa sera "No existes"

    Scenario: Edad de 10
        Dado que ingreso el numero "10"
        cuando realizo la operación
        entonces la etapa sera "Eres ninio"

    Scenario: Edad de 15
        Dado que ingreso el numero "15"
        cuando realizo la operación
        entonces la etapa sera "Eres adolescente"

    Scenario: Edad de 50
        Dado que ingreso el numero "50"
        cuando realizo la operación
        entonces la etapa sera "Eres adulto"

    Scenario: Edad de 70
        Dado que ingreso el numero "70"
        cuando realizo la operación
        entonces la etapa sera "Eres adulto mayor"

    Scenario: Edad de 150
        Dado que ingreso el numero "150"
        cuando realizo la operación
        entonces la etapa sera "Eres Mumm-Ra"
