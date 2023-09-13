import datetime
from django.db import models

# Create your models here.
class Paciente(models.Model):
    #Opciones
    options_si_no_np = [("SI","SI"), ("NO","NO"), ("NP","NP"),  ("EMPTY", "EMPTY")]
    options_si_no = [("SI","SI"), ("NO","NO"), ("EMPTY", "EMPTY")]
    options_resultado_alta = [("VIVO", "VIVO"), ("MUERTO", "MUERTO"), ("EMPTY", "EMPTY")]
    options_evaluacion_traslado = [("E", "E"), ("MB","MB"), ("B", "B"), ("AT", "AT"), ("EMPTY", "EMPTY")]
    options_clasificacion = [("D","D"), ("NO_D","NO_D"), ("EMPTY", "EMPTY")]
    
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
    alta = models.CharField(max_length = 6, choices = options_resultado_alta, default="EMPTY")
    #Atencion Primaria
    riesgo = models.CharField(max_length = 5, choices = options_si_no_np, default = "EMPTY", blank=True)  
    genetico = models.CharField(max_length = 5, choices = options_si_no_np, default = "EMPTY", blank=True)  
    precoz = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True) 
    numero_control = models.IntegerField(default = 0, blank=True)
    diag_prenatal = models.CharField(max_length = 5, choices = options_si_no, default = "EMPTY", blank = True)  
    #Al regreso del neonato operado
    hoja_conf = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True) 
    accion_inmediatas = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True)  
    cronograma_seg = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True)  
    #Hogar Materno
    info_maternidad = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True)  
    coordinacion_equipo = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True)  
    criterio_cirujano = models.CharField(max_length = 5, choices = options_si_no_np, default ="EMPTY", blank=True)  
    #Servicios de Neonatologia Provinciales
    presencia_en_salon = models.CharField(max_length = 5, choices = options_si_no_np, default ="EMPTY", blank=True)  
    actuacion_afeccion = models.CharField(max_length = 5, choices = options_si_no_np, default ="EMPTY", blank=True)  
    ginecologo_asig = models.CharField(max_length = 5, choices = options_si_no_np, default ="EMPTY", blank=True)  
    coordinacion_traslado1 = models.CharField(max_length = 5, choices = options_si_no_np, default ="EMPTY", blank=True)  
    #Cervicio de Neonatologia del CERECINE
    coincidencia_diag = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True)  
    coordinacion_traslado2 = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True)  
    justific_traslado = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True)  
    evaluacion_trasl = models.CharField(max_length = 5, choices = options_evaluacion_traslado, default ="EMPTY", blank=True)
    deficiencias_trasl = models.CharField(max_length = 1000, blank = True, default = "")
    interconsult_cirujano = models.CharField(max_length = 5, choices = options_si_no_np, default ="EMPTY", blank=True)  
    interconsult_medica = models.CharField(max_length = 5, choices = options_si_no_np, default ="EMPTY", blank=True)  
    estudios_inter_quirurgica = models.CharField(max_length = 5, choices = options_si_no_np, default ="EMPTY", blank=True)  
    doc_contrarref = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True)  
    programa_acciones = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True) 
    cronograma_atencion = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True)  
    #Equipo quirurgico
    confir_segunda_opinion = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True)  
    verificar_equipo_quirurgico = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True)  
    verificar_equipo_anestesico = models.CharField(max_length = 5, choices = options_si_no, default ="EMPTY", blank=True)  
    #Centro provincial de Genetica Holguin
    clasificacion = models.CharField(max_length = 5, choices=options_clasificacion, default="EMPTY", blank = True)
    fecha = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.id} {self.nombre}"
    
    
    