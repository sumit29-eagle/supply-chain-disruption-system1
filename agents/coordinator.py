
from .detector import detect
from .inventory import assess as inventory_assess
from .supplier import assess as supplier_assess
from .logistics import assess as logistics_assess
from .data import get_sample_data
from .llm_agents import run_ai_agent


def run_disruption_analysis(disruption):
    # Existing deterministic agents
    detection = detect(disruption)
    inventory = inventory_assess(disruption)
    supplier = supplier_assess(disruption)
    logistics = logistics_assess(disruption)

    # Context supplied to the AI from our existing sample data
    context = {
        "disruption": disruption,
        "detection": detection,
        "inventory": inventory,
        "supplier": supplier,
        "logistics": logistics,
        "sample_data": get_sample_data(),
    }

    # Real LLM-powered coordinator
    ai_result = run_ai_agent(
        agent_name="AI Response Coordinator",
        instructions=(
            "Review the specialist agent findings. "
            "Prioritize actions by urgency, explain trade-offs, "
            "and provide a concise response plan. "
            "Do not claim that actions have been executed."
        ),
        data=context,
    )

    results = [detection, inventory, supplier, logistics]

    category = ", ".join(detection["categories"])
    actions = []
    actions.extend(inventory["recommendations"])
    actions.append(supplier["recommendation"])
    actions.append(logistics["recommendation"])

    # Keep the original workflow working if AI is unavailable.
    if ai_result["status"] == "success":
        actions.append(
            "AI coordinator response: " + ai_result["analysis"]
        )

    results.append(ai_result)

    return {
        "disruption": disruption,
        "summary": (
            f"The system classified this as: {category}. "
            f"Initial severity: {detection['severity']}."
        ),
        "agents": results,
        "recommended_actions": actions,
        "ai_enabled": ai_result["status"] == "success",
        "disclaimer": (
            "Uses sample supply-chain data and rule-based specialist "
            "agents with an optional LLM-powered coordinator. "
            "No live ERP, supplier feed, or autonomous purchasing "
            "is connected."
        ),
    }
