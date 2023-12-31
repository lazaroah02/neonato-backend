import graphene
from .enums import EnumResultadoAlta, EnumClasificacion, EnumSiNoNp, EnumSiNo, EnumEvaluacionTraslado

class CommonMutationsArguments:
    nombre = graphene.String(required=False)
    apellidos = graphene.String(required=False)
    nombre_de_la_madre = graphene.String()
    carnet_identidad_madre = graphene.String(required=False)
    direccion = graphene.String()
    telefono = graphene.String(required=False)
    municipio = graphene.String()
    provincia = graphene.String()
    diagnostico_ingreso = graphene.String(required=False)
    diagnostico_egreso = graphene.String()
    alta = EnumResultadoAlta()
    riesgo = EnumSiNoNp(required=False)
    genetico = EnumSiNoNp(required=False)
    precoz = EnumSiNo(required=False)
    numero_control = graphene.Int(required=False)
    diag_prenatal = EnumSiNo(required=False)
    hoja_conf =EnumSiNo(required=False)
    accion_inmediatas = EnumSiNo(required=False)
    cronograma_seg = EnumSiNo(required=False)
    info_maternidad = EnumSiNo(required=False)
    coordinacion_equipo = EnumSiNo()
    criterio_cirujano = EnumSiNoNp(required=False)
    presencia_en_salon = EnumSiNoNp(required=False)
    actuacion_afeccion = EnumSiNoNp(required=False)
    ginecologo_asig = EnumSiNoNp(required=False)
    coordinacion_traslado1 = EnumSiNoNp(required=False)
    coincidencia_diag = EnumSiNo(required=False)
    coordinacion_traslado2 = EnumSiNo(required=False)
    justific_traslado = EnumSiNo(required=False)
    evaluacion_trasl = EnumEvaluacionTraslado(required=False)
    deficiencias_trasl = graphene.String(required=False)
    interconsult_cirujano = EnumSiNoNp(required=False)
    interconsult_medica = EnumSiNoNp(required=False)
    estudios_inter_quirurgica = EnumSiNoNp(required=False)
    doc_contrarref = EnumSiNo(required=False)
    programa_acciones = EnumSiNo(required=False)
    cronograma_atencion = EnumSiNo(required=False)
    confir_segunda_opinion = EnumSiNo(required=False)
    verificar_equipo_quirurgico =EnumSiNo(required=False)
    verificar_equipo_anestesico = EnumSiNo(required=False)
    clasificacion = EnumClasificacion(required=False) 
    fecha = graphene.Date(required=False)