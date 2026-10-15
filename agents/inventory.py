from .data import get_sample_data

def assess(disruption):
    data = get_sample_data()
    low = [x for x in data["inventory"] if x["stock"] <= x["reorder_level"]]
    actions = [f"Prioritize allocation of {x['item']} (stock {x['stock']} {x['unit']}; reorder level {x['reorder_level']})." for x in low]
    if not actions:
        actions = ["Current sample inventory is above reorder levels; keep monitoring consumption."]
    return {"agent": "Inventory Agent", "low_stock_items": [x["item"] for x in low], "recommendations": actions}
