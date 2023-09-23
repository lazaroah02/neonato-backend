from django.db import models
# Create your models here.
class Paciente(models.Model):
    
    #Identificacion
    nombre = models.CharField(max_length=255, blank=True, default = "")
    apellidos = models.CharField(max_length=255, blank=True, default = "")
    nombre_de_la_madre = models.CharField(max_length=255, default = "")
    carnet_identidad_madre = models.CharField(max_length=255, blank=True, default = "")
    direccion = models.CharField(max_length=500, default = "")
    telefono = models.CharField(max_length=15, default = "", blank=True)
    municipio = models.CharField(max_length=255, default = "")
    provincia = models.CharField(max_length=255, default = "")
    diagnostico_ingreso = models.CharField(max_length=1000, blank=True, default = "")
    diagnostico_egreso = models.CharField(max_length=1000, default = "")
    #Resultado del alta
    alta = models.CharField(max_length = 6, default="")
    #Atencion Primaria
    riesgo = models.CharField(max_length = 5, default = "", blank=True)  
    genetico = models.CharField(max_length = 5, default = "", blank=True)  
    precoz = models.CharField(max_length = 5, default = "", blank=True) 
    numero_control = models.IntegerField(default = 0, blank=True)
    diag_prenatal = models.CharField(max_length = 5, default = "", blank = True)  
    #Al regreso del neonato operado
    hoja_conf = models.CharField(max_length = 5, default ="", blank=True) 
    accion_inmediatas = models.CharField(max_length = 5, default ="", blank=True)  
    cronograma_seg = models.CharField(max_length = 5, default ="", blank=True)  
    #Hogar Materno
    info_maternidad = models.CharField(max_length = 5, default ="", blank=True)  
    coordinacion_equipo = models.CharField(max_length = 5, default ="", blank=True)  
    criterio_cirujano = models.CharField(max_length = 5, default ="", blank=True)  
    #Servicios de Neonatologia Provinciales
    presencia_en_salon = models.CharField(max_length = 5, default ="", blank=True)  
    actuacion_afeccion = models.CharField(max_length = 5, default ="", blank=True)  
    ginecologo_asig = models.CharField(max_length = 5, default ="", blank=True)  
    coordinacion_traslado1 = models.CharField(max_length = 5, default ="", blank=True)  
    #Cervicio de Neonatologia del CERECINE
    coincidencia_diag = models.CharField(max_length = 5, default ="", blank=True)  
    coordinacion_traslado2 = models.CharField(max_length = 5, default ="", blank=True)  
    justific_traslado = models.CharField(max_length = 5, default ="", blank=True)  
    evaluacion_trasl = models.CharField(max_length = 5, default ="", blank=True)
    deficiencias_trasl = models.CharField(max_length = 1000, blank = True, default = "")
    #Atencion medica
    interconsult_cirujano = models.CharField(max_length = 5, default ="", blank=True)  
    interconsult_medica = models.CharField(max_length = 5, default ="", blank=True)  
    estudios_inter_quirurgica = models.CharField(max_length = 5, default ="", blank=True)  
    doc_contrarref = models.CharField(max_length = 5, default ="", blank=True)  
    programa_acciones = models.CharField(max_length = 5, default ="", blank=True) 
    cronograma_atencion = models.CharField(max_length = 5, default ="", blank=True)  
    #Equipo quirurgico
    confir_segunda_opinion = models.CharField(max_length = 5, default ="", blank=True)  
    verificar_equipo_quirurgico = models.CharField(max_length = 5, default ="", blank=True)  
    verificar_equipo_anestesico = models.CharField(max_length = 5, default ="", blank=True)  
    #Centro provincial de Genetica Holguin
    clasificacion = models.CharField(max_length = 5, default="", blank = True)
    fecha = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now_add = True)
    #Evaluaciones de cada apartado(Excelente(E), Bien(E), Regular(R) y Mal(M))
    evaluacion_atencion_primaria = models.CharField(max_length = 15, default="B", blank = True)
    evaluacion_regreso_neonato_operado = models.CharField(max_length = 15, default="B", blank = True)
    evaluacion_hogar_materno =  models.CharField(max_length = 15, default="B", blank = True)
    evaluacion_servicio_neonatologia_provinciales =  models.CharField(max_length = 15, default="B", blank = True)
    evaluacion_servicio_neonatologia_cerecine =  models.CharField(max_length = 15, default="B", blank = True)
    evaluacion_atencion_medica =  models.CharField(max_length = 15, default="B", blank = True)
    evaluacion_equipo_quirurgico =  models.CharField(max_length = 15, default="B", blank = True)
    
    def __str__(self):
        return f"{self.id} {self.nombre}"

    
    
    