def assess(disruption):
    text = disruption.lower()
    if any(w in text for w in ["port", "ocean", "sea", "ship"]):
        action = "Compare an alternate port or air/rail option for critical items; validate cost, customs, and capacity."
    elif any(w in text for w in ["weather", "road", "route", "truck", "transport", "delay"]):
        action = "Compare a secondary carrier and alternate route; request updated ETAs and prioritize time-critical orders."
    else:
        action = "Ask carriers for current ETAs and prepare a contingency route for priority shipments."
    return {"agent": "Logistics Agent", "recommendation": action}
