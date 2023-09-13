import graphene

class EnumResultadoAlta(graphene.Enum):
    MUERTO = "MUERTO"
    VIVO = "VIVO"
    EMPTY = "EMPTY"

class EnumSiNoNp(graphene.Enum):
    SI = "SI"
    NO = "NO"
    NP = "NP"
    EMPTY = "EMPTY"   

class EnumSiNo(graphene.Enum):
    SI = "SI"
    NO = "NO"
    EMPTY = "EMPTY"    

class EnumEvaluacionTraslado(graphene.Enum):
    E = "E"
    MB = "MB"
    B = "B"       
    AT = "AT"       
    EMPTY = "EMPTY"     
      
class EnumClasificacion(graphene.Enum):
    D = "D"
    NO_D = "NO_D"
    EMPTY = "EMPTY"       