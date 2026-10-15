def detect(disruption):
    text = disruption.lower()
    keywords = {
        "transport delay": ["delay", "late", "shipment", "port", "logistics", "route", "weather"],
        "supplier disruption": ["supplier", "factory", "vendor", "strike", "shutdown", "shortage"],
        "inventory shortage": ["inventory", "stock", "out of stock", "raw material", "low stock"],
        "demand spike": ["demand", "surge", "order increase", "spike"],
    }
    matched = [kind for kind, words in keywords.items() if any(word in text for word in words)]
    if not matched:
        matched = ["general supply-chain disruption"]
    return {"agent": "Disruption Detection Agent", "categories": matched,
            "severity": "High" if any(w in text for w in ["stopped", "critical", "shutdown", "urgent"]) else "Medium",
            "finding": f"Detected {len(matched)} disruption category/categories from the provided description."}
