import graphene
from graphene_django import DjangoObjectType
from .models import Paciente

class PacienteType(DjangoObjectType):
    class Meta:
        model = Paciente
        
class Query(graphene.ObjectType):
    pacientes = graphene.List(PacienteType)
    paciente = graphene.Field(PacienteType, id = graphene.ID())
    
    def resolve_pacientes(self, info, **kwargs):
        return Paciente.objects.all()
    
    def resolve_paciente(self, info, id):
        return Paciente.objects.get(id = id)

class CommonMutationsArguments:
    nombre = graphene.String(required=False)
    apellidos = graphene.String(required=False)
    nombre_madre = graphene.String()
    carnet_identidad_madre = graphene.String(required=False)
    direccion = graphene.String()
    telefono = graphene.String(required=False)
    municipio = graphene.String(required=False)
    provincia = graphene.String(required=False)
    diagnostico_ingreso = graphene.String()
    atresia_esofagica = graphene.Boolean(required=False)
    defectos_pared = graphene.Boolean(required=False)
    atresia_estemos_intestinales = graphene.Boolean(required=False)
    defectos_diafragmaticos = graphene.Boolean(required=False)
    otros = graphene.Boolean(required=False)
    resultado_alta = graphene.String()
    embarazada_de_riesgo = graphene.Boolean(required=False)
    comprobacion_consejo_genetico = graphene.Boolean(required=False)
    captacion_precoz = graphene.Boolean(required=False)
    num_controles_embarazo = graphene.Int(required=False)
    diagnostico_prenatal = graphene.Boolean(required=False)
    hoja_contrarreferencia =graphene.Boolean(required=False)
    prog_acciones = graphene.Boolean(required=False)
    cronograma_seguimiento = graphene.Boolean(required=False)
    info_maternidad = graphene.Boolean(required=False)
    coordinacion_equipos_ginecologia = graphene.Boolean()
    criterio_cirujano = graphene.Boolean(required=False)
    neonatologo_salon_parto = graphene.Boolean(required=False)
    actuacion_segun_afeccion = graphene.Boolean(required=False)
    ginecologo_asignado = graphene.Boolean(required=False)
    coordinacion_traslado_provincial = graphene.Boolean(required=False)
    coincidencia_diagnostica = graphene.Boolean(required=False)
    coordinacion_trasado_cerecine = graphene.Boolean(required=False)
    justificacion_traslado = graphene.Boolean(required=False)
    evaluacion_traslado = graphene.String(required=False)
    deficiencias_traslado = graphene.String(required=False)
    interconsulta_cirujano = graphene.Boolean(required=False)
    interconsulta_medica = graphene.Boolean(required=False)
    estudios_intervencion_quirurgica = graphene.Boolean(required=False)
    documentos_contrarreferencia = graphene.String(required=False)
    prog_acciones_caso_individual = graphene.Boolean(required=False)
    cronograma_atencion = graphene.Boolean(required=False)
    confirmacion_segunda_opinion = graphene.Boolean(required=False)
    integracion_equipo_quirurgico = graphene.Boolean(required=False)
    equipo_anestesico_asignado = graphene.Boolean(required=False)
    clasificacion = graphene.String(required=False)   
  
class CreatePacienteMutation(graphene.Mutation):
    class Arguments(CommonMutationsArguments):
        pass
    paciente = graphene.Field(PacienteType)    
      
    def mutate(self, info, nombre_madre, diagnostico_ingreso, direccion, resultado_alta, **kwargs):
        paciente = Paciente(
            nombre_madre = nombre_madre,
            diagnostico_ingreso = diagnostico_ingreso,
            direccion = direccion,
            resultado_alta = resultado_alta,
            nombre = kwargs.get("nombre", ""),
            apellidos = kwargs.get("apellidos", ""),
            carnet_identidad_madre = kwargs.get("carnet_identidad_madre", ""),
            telefono = kwargs.get("telefono", ""),
            municipio = kwargs.get("municipio", ""),
            provincia = kwargs.get("provincia", ""),
            atresia_esofagica = kwargs.get("atresia_esofagica", False),
            defectos_pared = kwargs.get("defectos_pared", False),
            atresia_estemos_intestinales = kwargs.get("atresia_estemos_intestinales", False),
            defectos_diafragmaticos = kwargs.get("defectos_diafragmaticos", False),
            otros = kwargs.get("otros", False),
            embarazada_de_riesgo = kwargs.get("embarazada_de_riesgo", None),
            comprobacion_consejo_genetico = kwargs.get("comprobacion_consejo_genetico", None),
            captacion_precoz = kwargs.get("captacion_precoz", False),
            num_controles_embarazo = kwargs.get("num_controles_embarazo", 0),
            diagnostico_prenatal = kwargs.get("diagnostico_prenatal", False),
            hoja_contrarreferencia = kwargs.get("hoja_contrarreferencia", False),
            prog_acciones = kwargs.get("prog_acciones", False),
            cronograma_seguimiento = kwargs.get("cronograma_seguimiento", False),
            info_maternidad = kwargs.get("info_maternidad", False),
            coordinacion_equipos_ginecologia = kwargs.get("coordinacion_equipos_ginecologia", False),
            criterio_cirujano = kwargs.get("criterio_cirujano", None),
            neonatologo_salon_parto = kwargs.get("neonatologo_salon_parto", None),
            actuacion_segun_afeccion = kwargs.get("actuacion_segun_afeccion", None),
            ginecologo_asignado =  kwargs.get("ginecologo_asignado", None),
            coordinacion_traslado_provincial = kwargs.get("coordinacion_traslado_provincial", None),
            coincidencia_diagnostica = kwargs.get("coincidencia_diagnostica", False),
            coordinacion_trasado_cerecine = kwargs.get("coordinacion_trasado_cerecine", False),
            justificacion_traslado = kwargs.get("justificacion_traslado", False),
            evaluacion_traslado = kwargs.get("evaluacion_traslado", ""),
            deficiencias_traslado = kwargs.get("deficiencias_traslado", ""),
            interconsulta_cirujano = kwargs.get("interconsulta_cirujano", None),
            interconsulta_medica = kwargs.get("interconsulta_medica", None),
            estudios_intervencion_quirurgica = kwargs.get("estudios_intervencion_quirurgica", None),
            documentos_contrarreferencia = kwargs.get("documentos_contrarreferencia", False),
            prog_acciones_caso_individual = kwargs.get("prog_acciones_caso_individual", False),
            cronograma_atencion = kwargs.get("cronograma_atencion", False),
            confirmacion_segunda_opinion = kwargs.get("confirmacion_segunda_opinion", False),
            integracion_equipo_quirurgico = kwargs.get("integracion_equipo_quirurgico", False),
            equipo_anestesico_asignado = kwargs.get("equipo_anestesico_asignado", False),
            clasificacion = kwargs.get("clasificacion", "")
        )
        paciente.save()
        return CreatePacienteMutation(paciente = paciente)
            
class DeletePacienteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    message = graphene.String()    
    
    def mutate(self, info, id):
        note = Paciente.objects.get(id = id)
        note.delete()      
        return DeletePacienteMutation(message = "Paciente borrado exitosamente")

class UpdatePacienteMutation(graphene.Mutation):
    class Arguments(CommonMutationsArguments):
        id = graphene.ID(required=True)
    paciente = graphene.Field(PacienteType)    
    
    def mutate(self, info, id, **kwargs):
        paciente = Paciente.objects.get(id = id)
        paciente.nombre = kwargs.get("nombre", paciente.nombre)
        paciente.apellidos = kwargs.get("apellidos", paciente.apellidos)
        paciente.nombre_madre = kwargs.get("nombre_madre", paciente.nombre_madre)
        paciente.carnet_identidad_madre = kwargs.get("carnet_identidad_madre", paciente.carnet_identidad_madre)
        paciente.direccion = kwargs.get("direccion", paciente.direccion)
        paciente.telefono = kwargs.get("telefono", paciente.telefono)
        paciente.municipio = kwargs.get("municipio", paciente.municipio)
        paciente.provincia = kwargs.get("provincia", paciente.provincia)
        paciente.diagnostico_ingreso = kwargs.get("diagnostico_ingreso", paciente.diagnostico_ingreso)
        paciente.atresia_esofagica = kwargs.get("atresia_esofagica", paciente.atresia_esofagica)
        paciente.defectos_pared =kwargs.get("defectos_pared", paciente.defectos_pared)
        paciente.atresia_estemos_intestinales = kwargs.get("atresia_estemos_intestinales", paciente.atresia_estemos_intestinales)
        paciente.defectos_diafragmaticos = kwargs.get("defectos_diafragmaticos", paciente.defectos_diafragmaticos)
        paciente.otros = kwargs.get("otros", paciente.otros)
        paciente.resultado_alta = kwargs.get("resultado_alta", paciente.resultado_alta)
        paciente.embarazada_de_riesgo = kwargs.get("embarazada_de_riesgo", paciente.embarazada_de_riesgo)
        paciente.comprobacion_consejo_genetico = kwargs.get("comprobacion_consejo_genetico", paciente.comprobacion_consejo_genetico)
        paciente.captacion_precoz = kwargs.get("captacion_precoz", paciente.captacion_precoz)
        paciente.num_controles_embarazo = kwargs.get("num_controles_embarazo", paciente.num_controles_embarazo)
        paciente.diagnostico_prenatal = kwargs.get("diagnostico_prenatal", paciente.diagnostico_prenatal)
        paciente.hoja_contrarreferencia = kwargs.get("hoja_contrarreferencia", paciente.hoja_contrarreferencia)
        paciente.prog_acciones = kwargs.get("prog_acciones", paciente.prog_acciones)
        paciente.cronograma_seguimiento = kwargs.get("cronograma_seguimiento", paciente.cronograma_seguimiento)
        paciente.info_maternidad = kwargs.get("info_maternidad", paciente.info_maternidad)
        paciente.coordinacion_equipos_ginecologia = kwargs.get("coordinacion_equipos_ginecologia", paciente.coordinacion_equipos_ginecologia)
        paciente.criterio_cirujano = kwargs.get("criterio_cirujano", paciente.criterio_cirujano)
        paciente.neonatologo_salon_parto = kwargs.get("neonatologo_salon_parto", paciente.neonatologo_salon_parto)
        paciente.actuacion_segun_afeccion = kwargs.get("actuacion_segun_afeccion", paciente.actuacion_segun_afeccion)
        paciente.ginecologo_asignado =  kwargs.get("ginecologo_asignado", paciente.ginecologo_asignado)
        paciente.coordinacion_traslado_provincial = kwargs.get("coordinacion_traslado_provincial", paciente.coordinacion_traslado_provincial)
        paciente.coincidencia_diagnostica = kwargs.get("coincidencia_diagnostica", paciente.coincidencia_diagnostica)
        paciente.coordinacion_trasado_cerecine = kwargs.get("coordinacion_trasado_cerecine", paciente.coordinacion_trasado_cerecine)
        paciente.justificacion_traslado = kwargs.get("justificacion_traslado", paciente.justificacion_traslado)
        paciente.evaluacion_traslado = kwargs.get("evaluacion_traslado", paciente.evaluacion_traslado)
        paciente.deficiencias_traslado = kwargs.get("deficiencias_traslado", paciente.deficiencias_traslado)
        paciente.interconsulta_cirujano = kwargs.get("interconsulta_cirujano", paciente.interconsulta_cirujano)
        paciente.interconsulta_medica = kwargs.get("interconsulta_medica", paciente.interconsulta_medica)
        paciente.estudios_intervencion_quirurgica = kwargs.get("estudios_intervencion_quirurgica", paciente.estudios_intervencion_quirurgica)
        paciente.documentos_contrarreferencia = kwargs.get("documentos_contrarreferencia", paciente.documentos_contrarreferencia)
        paciente.prog_acciones_caso_individual = kwargs.get("prog_acciones_caso_individual", paciente.prog_acciones_caso_individual)
        paciente.cronograma_atencion = kwargs.get("cronograma_atencion", paciente.cronograma_atencion)
        paciente.confirmacion_segunda_opinion = kwargs.get("confirmacion_segunda_opinion", paciente.confirmacion_segunda_opinion)
        paciente.integracion_equipo_quirurgico = kwargs.get("integracion_equipo_quirurgico", paciente.integracion_equipo_quirurgico)
        paciente.equipo_anestesico_asignado = kwargs.get("equipo_anestesico_asignado", paciente.equipo_anestesico_asignado)
        paciente.clasificacion = kwargs.get("clasificacion", paciente.clasificacion)
        paciente.save()   
        return UpdatePacienteMutation(paciente = paciente)    
        
class Mutation(graphene.ObjectType):
    create_paciente = CreatePacienteMutation.Field() 
    delete_paciente = DeletePacienteMutation.Field()
    update_paciente = UpdatePacienteMutation.Field()
            

    