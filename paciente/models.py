import datetime
from django.db import models

# Create your models here.

class Paciente(models.Model):
    #Identificacion
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellidos = models.CharField(max_length=255, blank=True, null=True)
    nombre_madre = models.CharField(max_length=255)
    carnet_identidad_madre = models.CharField(max_length=255, blank=True, null = True)
    direccion = models.CharField(max_length=500)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    municipio = models.CharField(max_length=255, blank=True, null=True)
    provincia = models.CharField(max_length=255, blank=True, null = True)
    diagnostico_ingreso = models.CharField(max_length=1000)
    #Diagnostico Ingreso
    atresia_esofagica = models.BooleanField(default=False) #True(si) False(no)
    defectos_pared = models.BooleanField(default=False) #True(si) False(no)
    atresia_estemos_intestinales = models.BooleanField(default=False) #True(si) False(no)
    defectos_diafragmaticos = models.BooleanField(default=False) #True(si) False(no)
    otros = models.BooleanField(default=False) #True(si) False(no)
    #Resultado del alta
    resultado_alta = models.CharField(max_length = 255)
    #Atencion Primaria
    embarazada_de_riesgo = models.BooleanField(default = None, blank=True, null = True) #True(si) False(no) null(NP)
    comprobacion_consejo_genetico = models.BooleanField(default = None, blank=True, null = True) #True(si) False(no) null(NP)
    captacion_precoz = models.BooleanField(default=False) #True(si) False(no)
    num_controles_embarazo = models.IntegerField(default = 0)
    diagnostico_prenatal = models.BooleanField(default = False) #True(si) False(no) 
    #Al regreso del neonato operado
    hoja_contrarreferencia =models.BooleanField(default = False) #True(si) False(no)
    prog_acciones = models.BooleanField(default = False) #True(si) False(no) 
    cronograma_seguimiento = models.BooleanField(default = False) #True(si) False(no) 
    #Hogar Materno
    info_maternidad = models.BooleanField(default = False) #True(si) False(no) 
    coordinacion_equipos_ginecologia = models.BooleanField(default = False) #True(si) False(no) 
    criterio_cirujano = models.BooleanField(default = None, blank = True, null = True) #True(si) False(no) null(NP)
    #Servicios de Neonatologia Provinciales
    neonatologo_salon_parto = models.BooleanField(default=None, blank = True, null = True) #True(si) False(no) null(NP)
    actuacion_segun_afeccion = models.BooleanField(default=None, blank = True, null = True) #True(si) False(no) null(NP)
    ginecologo_asignado = models.BooleanField(default=None, blank = True, null = True) #True(si) False(no) null(NP)
    coordinacion_traslado_provincial = models.BooleanField(default=None, blank = True, null = True) #True(si) False(no) null(NP)
    #Cervicio de Neonatologia del CERECINE
    coincidencia_diagnostica = models.BooleanField(default = False) #True(si) False(no) 
    coordinacion_trasado_cerecine = models.BooleanField(default = False) #True(si) False(no) 
    justificacion_traslado = models.BooleanField(default = False) #True(si) False(no) 
    evaluacion_traslado = models.CharField(max_length = 255, blank = True, null=True)
    deficiencias_traslado = models.CharField(max_length = 1000, blank = True, null = True)
    interconsulta_cirujano = models.BooleanField(default=None, blank = True, null = True) #True(si) False(no) null(NP)
    interconsulta_medica = models.BooleanField(default=None, blank = True, null = True) #True(si) False(no) null(NP)
    estudios_intervencion_quirurgica = models.BooleanField(default=None, blank = True, null = True) #True(si) False(no) null(NP)
    documentos_contrarreferencia = models.BooleanField(default = False) #True(si) False(no) 
    prog_acciones_caso_individual = models.BooleanField(default = False) #True(si) False(no)
    cronograma_atencion = models.BooleanField(default = False) #True(si) False(no) 
    #Equipo quirurgico
    confirmacion_segunda_opinion = models.BooleanField(default = False) #True(si) False(no) 
    integracion_equipo_quirurgico = models.BooleanField(default = False) #True(si) False(no) 
    equipo_anestesico_asignado = models.BooleanField(default = False) #True(si) False(no) 
    #Centro provincial de Genetica Holguin
    clasificacion = models.CharField(max_length = 255, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.id} {self.nombre}"
    
    
    