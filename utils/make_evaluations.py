from utils import evaluations_paciente_care
def make_evaluations(instance):
    instance.evaluacion_atencion_primaria = evaluations_paciente_care.evaluacion_atencion_primaria(instance)   
    instance.evaluacion_regreso_neonato_operado = evaluations_paciente_care.evaluacion_regreso_neonato_operado(instance)   
    instance.evaluacion_hogar_materno = evaluations_paciente_care.evaluacion_hogar_materno(instance)   
    instance.evaluacion_servicio_neonatologia_provinciales = evaluations_paciente_care.evaluacion_servicio_neonatologia_provinciales(instance)   
    instance.evaluacion_servicio_neonatologia_cerecine = evaluations_paciente_care.evaluacion_servicio_neonatologia_cerecine(instance)   
    instance.evaluacion_atencion_medica = evaluations_paciente_care.evaluacion_atencion_medica(instance)   
    instance.evaluacion_equipo_quirurgico = evaluations_paciente_care.evaluacion_equipo_quirurgico(instance)   
    instance.save()