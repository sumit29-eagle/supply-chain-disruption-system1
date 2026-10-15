def get_sample_data():
    return {
        "orders": [
            {"id": "ORD-1001", "customer": "Northstar Retail", "product": "Smart Sensors", "qty": 240, "status": "At risk"},
            {"id": "ORD-1002", "customer": "Metro Devices", "product": "Control Units", "qty": 120, "status": "On track"},
            {"id": "ORD-1003", "customer": "Apex Manufacturing", "product": "Power Modules", "qty": 360, "status": "Delayed"},
            {"id": "ORD-1004", "customer": "BluePeak Systems", "product": "Smart Sensors", "qty": 180, "status": "On track"},
        ],
        "shipments": [
            {"id": "SHP-201", "route": "Shenzhen → Mumbai", "carrier": "OceanBridge", "status": "Delayed", "eta": "3 days late"},
            {"id": "SHP-202", "route": "Pune → Delhi", "carrier": "SwiftLine", "status": "On time", "eta": "Today"},
            {"id": "SHP-203", "route": "Chennai → Mumbai", "carrier": "CargoJet", "status": "Delayed", "eta": "1 day late"},
            {"id": "SHP-204", "route": "Ahmedabad → Jaipur", "carrier": "RoadRunner", "status": "On time", "eta": "Tomorrow"},
        ],
        "inventory": [
            {"item": "Smart Sensors", "stock": 90, "reorder_level": 120, "unit": "units"},
            {"item": "Control Units", "stock": 340, "reorder_level": 100, "unit": "units"},
            {"item": "Power Modules", "stock": 75, "reorder_level": 100, "unit": "units"},
            {"item": "Connector Kits", "stock": 510, "reorder_level": 150, "unit": "kits"},
        ],
        "suppliers": [
            {"name": "Shenzhen Components Co.", "region": "China", "lead_time": "18 days", "risk": 8},
            {"name": "Western Circuit Works", "region": "India", "lead_time": "7 days", "risk": 3},
            {"name": "Pacific Parts Ltd.", "region": "Vietnam", "lead_time": "12 days", "risk": 6},
        ]
    }
