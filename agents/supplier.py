from .data import get_sample_data

def assess(disruption):
    suppliers = sorted(get_sample_data()["suppliers"], key=lambda s: (s["risk"], int(s["lead_time"].split()[0])))
    preferred = suppliers[0]
    return {"agent": "Supplier Agent", "preferred_alternative": preferred["name"],
            "recommendation": f"Check capacity and pricing with {preferred['name']} ({preferred['region']}, estimated lead time {preferred['lead_time']}, sample risk score {preferred['risk']}/10).",
            "note": "Supplier options are illustrative sample data and must be verified before procurement."}
