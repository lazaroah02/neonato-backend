import graphene
from graphene.types.generic import GenericScalar
from paciente.models import Paciente

diagnosticos_egreso = {
    "1": "Atresia Esofágica,",
    "2": "Defectos de la Pared,",
    "3": "Atresias y estenosis intestinales,",
    "4": "Defectos diafragmáticos,",
    "5": "Otros,",
}

class Query(graphene.ObjectType):
    graphic_diagnostico_egreso = GenericScalar()
    
    def resolve_graphic_diagnostico_egreso(self, info):
        pacientes = Paciente.objects.all()
        
        diagnostico_egreso_results = {
            "total_pacientes": pacientes.count(),
            "pacientes_atresia_esofagica": 0,
            "pacientes_defectos_pared": 0,
            "pacientes_atresias_y_estenosis_intestinales": 0,
            "pacientes_defectos_diafragmaticos": 0,
            "pacientes_otros": 0
        }
        
        for paciente in pacientes:
            if paciente.diagnostico_egreso.strip() == diagnosticos_egreso["1"].strip():
                diagnostico_egreso_results["pacientes_atresia_esofagica"] += 1
            if paciente.diagnostico_egreso.strip() == diagnosticos_egreso["2"].strip():
                diagnostico_egreso_results["pacientes_defectos_pared"] += 1
            if paciente.diagnostico_egreso.strip() == diagnosticos_egreso["3"].strip():
                diagnostico_egreso_results["pacientes_atresias_y_estenosis_intestinales"] += 1
            if paciente.diagnostico_egreso.strip() == diagnosticos_egreso["4"].strip():
                diagnostico_egreso_results["pacientes_defectos_diafragmaticos"] += 1
            if paciente.diagnostico_egreso.strip() == diagnosticos_egreso["5"].strip():
                diagnostico_egreso_results["pacientes_otros"] += 1
                
        return diagnostico_egreso_results