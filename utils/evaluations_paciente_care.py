def evaluacion_atencion_primaria(paciente):
    """_summary_
    Evaluación Atencion Primaria:
    Mal: Menos de 8 controles
    Regular:  8 controles y todo lo demás deficiente 
    Bien: 8 controles  y el 1 o el 2 
    Excelente: cuando todo este cumplido
    """
    if paciente.numero_control >= 8 and paciente.riesgo == "SI" and paciente.genetico == "SI" and paciente.precoz == "SI" and paciente.diag_prenatal == "SI":
        return "E"
    if paciente.numero_control < 8:
        return "M"
    if paciente.numero_control >= 8 and paciente.riesgo != "SI" and paciente.genetico != "SI" and paciente.precoz != "SI" and paciente.diag_prenatal != "SI":
        return "R"
    return "B"

def evaluacion_regreso_neonato_operado(paciente):
    """_summary_
    Evaluación al regreso del neonato operado:
    Mal: Sin hoja de contrareferncia
    Regular: Solo con hoja de contra referencia y los aspectos 2 y 3 sin cumplir
    Bien. Hoja de contra referencia y uno de los aspectos 2 0 3  cumplidos
    Excelente: todo cumplido
    """
    if paciente.hoja_conf == "SI" and paciente.accion_inmediatas == "SI" and paciente.cronograma_seg == "SI":
        return "E"
    if paciente.hoja_conf != "SI":
        return "M"
    if paciente.hoja_conf == "SI" and paciente.accion_inmediatas != "SI" and paciente.cronograma_seg != "SI":
        return "R"
    return "B"

def evaluacion_hogar_materno(paciente):
    """_summary_
    Evaluación Hogar Materno:
    Mal: 1 no cumplido
    Regular: 1 cumplido
    B: 1 cumplido más alguno  2 o 3 
    E: Todo cumplido
    """
    if paciente.info_maternidad == "SI" and paciente.coordinacion_equipo == "SI" and paciente.criterio_cirujano == "SI":
        return "E"
    if paciente.info_maternidad != "SI":
        return "M"
    if paciente.info_maternidad == "SI" and paciente.coordinacion_equipo != "SI" and paciente.criterio_cirujano != "SI":
        return "R"
    return "B"

def evaluacion_servicio_neonatologia_provinciales(paciente):
    """_summary_
    Evaluación servicio de Neonatologia Provinciales:
    1.	Mal: 1 no cumplido
    2.	Regular: 1 cumplido
    3.	B: 1 cumplido más alguno  2, 3  o 4
    4.	E: Todo cumplido
    """
    if paciente.presencia_en_salon == "SI" and paciente.actuacion_afeccion == "SI" and paciente.ginecologo_asig == "SI" and paciente.coordinacion_traslado1 == "SI":
        return "E"
    if paciente.presencia_en_salon != "SI":
        return "M"
    if paciente.presencia_en_salon == "SI" and paciente.actuacion_afeccion != "SI" and paciente.ginecologo_asig != "SI" and paciente.coordinacion_traslado1 != "SI":
        return "R"
    return "B"

def evaluacion_servicio_neonatologia_cerecine(paciente):
    """_summary_
    Evaluación Servicio de Neonatologia CERECINE:
    1.	Mal: 1 no cumplido
    2.	Regular: 1 cumplido
    3.	B: 1 cumplido más alguno  2, 3  o 4
    4.	E: Todo cumplido
    """
    if paciente.coincidencia_diag == "SI" and paciente.coordinacion_traslado2 == "SI" and paciente.justific_traslado == "SI" and paciente.evaluacion_trasl == "E":
        return "E"
    if paciente.coordinacion_traslado2 != "SI":
        return "M"
    if paciente.coordinacion_traslado2 == "SI" and paciente.coincidencia_diag != "SI" and paciente.justific_traslado != "SI" and paciente.evaluacion_trasl != "E":
        return "R"
    return "B"

def evaluacion_atencion_medica(paciente):
    """_summary_
    Evaluación Atencion Medica:
    1.	Mal: 1 no cumplido o 5 no cumplido
    2.	Regular: 1 cumplido o 5 cumplidos
    3.	B: 1  y 5 cumplido más alguno  2, 3  o 4
    4.	E: Todo cumplido
    """
    if paciente.interconsult_cirujano == "SI" and paciente.interconsult_medica == "SI" and paciente.estudios_inter_quirurgica == "SI" and paciente.doc_contrarref == "SI" and paciente.programa_acciones == "SI" and paciente.cronograma_atencion == "SI":
        return "E"
    if paciente.interconsult_cirujano != "SI" or paciente.programa_acciones != "SI":
        return "M"
    if paciente.interconsult_cirujano == "SI" and paciente.programa_acciones == "SI" and paciente.interconsult_medica != "SI" and paciente.estudios_inter_quirurgica != "SI" and paciente.doc_contrarref != "SI" and paciente.cronograma_atencion != "SI":
        return "R"
    return "B"

def evaluacion_equipo_quirurgico(paciente):
    """_summary_
    Evaluación Equipo Quirurgico:
    1.	Mal: 1 no cumplido
    2.	Regular: 1 cumplido
    3.	B: 1 cumplido más alguno  2 o 3
    4.	E: Todo cumplido
    """
    if paciente.confir_segunda_opinion == "SI" and paciente.verificar_equipo_quirurgico == "SI" and paciente.verificar_equipo_anestesico == "SI":
        return "E"
    if paciente.confir_segunda_opinion != "SI":
        return "M"
    if paciente.confir_segunda_opinion == "SI" and paciente.verificar_equipo_quirurgico != "SI" and paciente.verificar_equipo_anestesico != "SI":
        return "R"
    return "B" 
    