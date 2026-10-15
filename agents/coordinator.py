from .detector import detect
from .inventory import assess as inventory_assess
from .supplier import assess as supplier_assess
from .logistics import assess as logistics_assess

def run_disruption_analysis(disruption):
    results = [
        detect(disruption),
        inventory_assess(disruption),
        supplier_assess(disruption),
        logistics_assess(disruption),
    ]
    category = ", ".join(results[0]["categories"])
    actions = []
    actions.extend(results[1]["recommendations"])
    actions.append(results[2]["recommendation"])
    actions.append(results[3]["recommendation"])
    return {
        "disruption": disruption,
        "summary": f"The system classified this as: {category}. Initial severity: {results[0]['severity']}.",
        "agents": results,
        "recommended_actions": actions,
        "disclaimer": "This is a demonstration using rules and illustrative sample data, not a live ERP, supplier feed, or autonomous purchasing system."
    }
