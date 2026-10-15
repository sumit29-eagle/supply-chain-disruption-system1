
from .detector import detect
from .inventory import assess as inventory_assess
from .supplier import assess as supplier_assess
from .logistics import assess as logistics_assess
from .data import get_sample_data
from .llm_agents import run_ai_agent


def run_disruption_analysis(disruption):
    # Run the existing rule-based specialist agents
    detection = detect(disruption)
    inventory = inventory_assess(disruption)
    supplier = supplier_assess(disruption)
    logistics = logistics_assess(disruption)

    # Prepare context for the AI coordinator
    context = {
        "disruption": disruption,
        "detection": detection,
        "inventory": inventory,
        "supplier": supplier,
        "logistics": logistics,
        "sample_data": get_sample_data(),
    }

    # Run the LLM-powered coordinator
    ai_result = run_ai_agent(
        agent_name="AI Response Coordinator",
        instructions=(
            "Review the specialist agent findings. "
            "Prioritize actions by urgency, explain trade-offs, "
            "and provide a concise response plan. "
            "Use only the supplied data. Clearly identify assumptions. "
            "Do not claim that actions have been executed."
        ),
        data=context,
    )

    # Collect all agent results
    results = [
        detection,
        inventory,
        supplier,
        logistics,
        ai_result,
    ]

    category = ", ".join(detection["categories"])

    # Build recommended actions
    actions = []
    actions.extend(inventory["recommendations"])
    actions.append(supplier["recommendation"])
    actions.append(logistics["recommendation"])

    # Include the AI response when available
    if ai_result.get("status") == "success":
        actions.append(
            "AI coordinator response: "
            + ai_result.get("analysis", "")
        )

    return {
        "disruption": disruption,
        "summary": (
            f"The system classified this as: {category}. "
            f"Initial severity: {detection['severity']}."
        ),
        "agents": results,
        "recommended_actions": actions,
        "ai_enabled": ai_result.get("status") == "success",
        "disclaimer": (
            "This is a demonstration using rule-based agents, "
            "sample data, and an optional LLM-powered coordinator. "
            "No live ERP, supplier feed, or autonomous purchasing "
            "is connected."
        ),
    }
