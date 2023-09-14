import graphene
from graphene_django import DjangoObjectType
from .models import Paciente
from .commonMutationsArguments import CommonMutationsArguments
from django_filters import FilterSet, OrderingFilter, CharFilter
from graphene_django.filter import DjangoFilterConnectionField
from django.db.models import Q
from .utils import convert_graphqlid_to_int

class PacienteFilter(FilterSet):
    search = CharFilter(method='searching')
    class Meta:
        model = Paciente
        fields = {
            'nombre': ('contains','startswith'),
            'nombre_de_la_madre': ('contains','startswith',),
            'apellidos': ('contains','startswith',),
        }
    order_by = OrderingFilter(
        fields=(
        ('fecha', 'fecha'),
        ),
        field_labels={
        'fecha': 'fecha',
        }
    )
    def searching(self, queryset, name, value):
        return queryset.filter(Q(nombre__icontains=value) | Q(nombre_de_la_madre__icontains=value) | Q(apellidos__icontains=value))

class PacienteType(DjangoObjectType):
    class Meta:
        model = Paciente
        interfaces = (graphene.relay.Node,)
        
class PacienteConnections(graphene.relay.Connection):
    class Meta:
        node = PacienteType
        
class Query(graphene.ObjectType):
    pacientes = DjangoFilterConnectionField(PacienteType, filterset_class = PacienteFilter)
    paciente = graphene.Field(PacienteType, id = graphene.ID())
    
    def resolve_pacientes(self, info, **kwargs):
        return Paciente.objects.all()
    
    def resolve_paciente(self, info, id):
        num_id = convert_graphqlid_to_int(id)
        return Paciente.objects.get(id = num_id)
  
class CreatePacienteMutation(graphene.Mutation):
    class Arguments(CommonMutationsArguments):
        pass
    paciente = graphene.Field(PacienteType)    
      
    def mutate(self, info, fecha, nombre_de_la_madre, direccion, municipio, provincia, diagnostico_egreso, alta, **kwargs):
        paciente = Paciente(
            fecha = fecha,
            nombre_de_la_madre = nombre_de_la_madre,
            direccion = direccion,
            municipio = municipio,
            provincia = provincia,
            diagnostico_egreso = diagnostico_egreso,
            alta = alta,
            nombre = kwargs.get("nombre", ""),
            apellidos = kwargs.get("apellidos", ""),
            carnet_identidad_madre = kwargs.get("carnet_identidad_madre", ""),
            telefono = kwargs.get("telefono", ""),
            riesgo = kwargs.get("riesgo", "EMPTY"),
            genetico = kwargs.get("genetico", "EMPTY"),
            precoz = kwargs.get("precoz", "EMPTY"),
            numero_control = kwargs.get("numero_control", 0),
            diag_prenatal = kwargs.get("diag_prenatal", "EMPTY"),
            hoja_conf = kwargs.get("hoja_conf", "EMPTY"),
            accion_inmediatas = kwargs.get("accion_inmediatas", "EMPTY"),
            cronograma_seg = kwargs.get("cronograma_seg", "EMPTY"),
            info_maternidad = kwargs.get("info_maternidad", "EMPTY"),
            coordinacion_equipo = kwargs.get("coordinacion_equipo", "EMPTY"),
            criterio_cirujano = kwargs.get("criterio_cirujano", "EMPTY"),
            presencia_en_salon = kwargs.get("presencia_en_salon", "EMPTY"),
            actuacion_afeccion = kwargs.get("actuacion_afeccion", "EMPTY"),
            ginecologo_asig =  kwargs.get("ginecologo_asig", "EMPTY"),
            coordinacion_traslado1 = kwargs.get("coordinacion_traslado1", "EMPTY"),
            coincidencia_diag = kwargs.get("coincidencia_diag", "EMPTY"),
            coordinacion_traslado2 = kwargs.get("coordinacion_traslado2", "EMPTY"),
            justific_traslado = kwargs.get("justific_traslado", "EMPTY"),
            evaluacion_trasl = kwargs.get("evaluacion_trasl", "EMPTY"),
            deficiencias_trasl = kwargs.get("deficiencias_trasl", ""),
            interconsult_cirujano = kwargs.get("interconsult_cirujano", "EMPTY"),
            interconsult_medica = kwargs.get("interconsult_medica", "EMPTY"),
            estudios_inter_quirurgica = kwargs.get("estudios_inter_quirurgica", "EMPTY"),
            doc_contrarref = kwargs.get("doc_contrarref", "EMPTY"),
            programa_acciones = kwargs.get("programa_acciones", "EMPTY"),
            cronograma_atencion = kwargs.get("cronograma_atencion", "EMPTY"),
            confir_segunda_opinion = kwargs.get("confir_segunda_opinion", "EMPTY"),
            verificar_equipo_quirurgico = kwargs.get("verificar_equipo_quirurgico", "EMPTY"),
            verificar_equipo_anestesico = kwargs.get("verificar_equipo_anestesico", "EMPTY"),
            clasificacion = kwargs.get("clasificacion", "EMPTY")
        )
        paciente.save()
        return CreatePacienteMutation(paciente = paciente)
            
class DeletePacienteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    message = graphene.String()    
    
    def mutate(self, info, id):
        num_id = convert_graphqlid_to_int(id)
        note = Paciente.objects.get(id = num_id)
        note.delete()      
        return DeletePacienteMutation(message = "Paciente borrado exitosamente")

class UpdatePacienteMutation(graphene.Mutation):
    class Arguments(CommonMutationsArguments):
        id = graphene.ID(required=True)
    paciente = graphene.Field(PacienteType)    
    
    def mutate(self, info, id, **kwargs):
        num_id = convert_graphqlid_to_int(id)
        paciente = Paciente.objects.get(id = num_id)
        paciente.nombre = kwargs.get("nombre", paciente.nombre)
        paciente.apellidos = kwargs.get("apellidos", paciente.apellidos)
        paciente.nombre_de_la_madre = kwargs.get("nombre_de_la_madre", paciente.nombre_de_la_madre)
        paciente.carnet_identidad_madre = kwargs.get("carnet_identidad_madre", paciente.carnet_identidad_madre)
        paciente.direccion = kwargs.get("direccion", paciente.direccion)
        paciente.telefono = kwargs.get("telefono", paciente.telefono)
        paciente.municipio = kwargs.get("municipio", paciente.municipio)
        paciente.provincia = kwargs.get("provincia", paciente.provincia)
        paciente.diagnostico_ingreso = kwargs.get("diagnostico_ingreso", paciente.diagnostico_ingreso)
        paciente.alta = kwargs.get("alta", paciente.alta)
        paciente.riesgo = kwargs.get("riesgo", paciente.riesgo)
        paciente.genetico = kwargs.get("genetico", paciente.genetico)
        paciente.precoz = kwargs.get("precoz", paciente.precoz)
        paciente.numero_control = kwargs.get("numero_control", paciente.numero_control)
        paciente.diag_prenatal = kwargs.get("diag_prenatal", paciente.diag_prenatal)
        paciente.hoja_conf = kwargs.get("hoja_conf", paciente.hoja_conf)
        paciente.accion_inmediatas = kwargs.get("accion_inmediatas", paciente.accion_inmediatas)
        paciente.cronograma_seg = kwargs.get("cronograma_seg", paciente.cronograma_seg)
        paciente.info_maternidad = kwargs.get("info_maternidad", paciente.info_maternidad)
        paciente.coordinacion_equipo = kwargs.get("coordinacion_equipo", paciente.coordinacion_equipo)
        paciente.criterio_cirujano = kwargs.get("criterio_cirujano", paciente.criterio_cirujano)
        paciente.presencia_en_salon = kwargs.get("presencia_en_salon", paciente.presencia_en_salon)
        paciente.actuacion_afeccion = kwargs.get("actuacion_afeccion", paciente.actuacion_afeccion)
        paciente.ginecologo_asig =  kwargs.get("ginecologo_asig", paciente.ginecologo_asig)
        paciente.coordinacion_traslado1 = kwargs.get("coordinacion_traslado1", paciente.coordinacion_traslado1)
        paciente.coincidencia_diag = kwargs.get("coincidencia_diag", paciente.coincidencia_diag)
        paciente.coordinacion_traslado2 = kwargs.get("coordinacion_traslado2", paciente.coordinacion_traslado2)
        paciente.justific_traslado = kwargs.get("justific_traslado", paciente.justific_traslado)
        paciente.evaluacion_trasl = kwargs.get("evaluacion_trasl", paciente.evaluacion_trasl)
        paciente.deficiencias_trasl = kwargs.get("deficiencias_trasl", paciente.deficiencias_trasl)
        paciente.interconsult_cirujano = kwargs.get("interconsult_cirujano", paciente.interconsult_cirujano)
        paciente.interconsult_medica = kwargs.get("interconsult_medica", paciente.interconsult_medica)
        paciente.estudios_inter_quirurgica = kwargs.get("estudios_inter_quirurgica", paciente.estudios_inter_quirurgica)
        paciente.doc_contrarref = kwargs.get("doc_contrarref", paciente.doc_contrarref)
        paciente.programa_acciones = kwargs.get("programa_acciones", paciente.programa_acciones)
        paciente.cronograma_atencion = kwargs.get("cronograma_atencion", paciente.cronograma_atencion)
        paciente.confir_segunda_opinion = kwargs.get("confir_segunda_opinion", paciente.confir_segunda_opinion)
        paciente.verificar_equipo_quirurgico = kwargs.get("verificar_equipo_quirurgico", paciente.verificar_equipo_quirurgico)
        paciente.verificar_equipo_anestesico = kwargs.get("verificar_equipo_anestesico", paciente.verificar_equipo_anestesico)
        paciente.clasificacion = kwargs.get("clasificacion", paciente.clasificacion)
        paciente.save()   
        return UpdatePacienteMutation(paciente = paciente)    
        
class Mutation(graphene.ObjectType):
    create_paciente = CreatePacienteMutation.Field() 
    delete_paciente = DeletePacienteMutation.Field()
    update_paciente = UpdatePacienteMutation.Field()
            

    