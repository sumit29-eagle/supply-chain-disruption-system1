from flask import Flask, jsonify, render_template, request
from agents.coordinator import run_disruption_analysis
from agents.data import get_sample_data

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/overview")
def overview():
    data = get_sample_data()
    return jsonify({
        "metrics": {
            "total_orders": len(data["orders"]),
            "delayed_shipments": sum(1 for x in data["shipments"] if x["status"] == "Delayed"),
            "low_stock_items": sum(1 for x in data["inventory"] if x["stock"] <= x["reorder_level"]),
            "at_risk_suppliers": sum(1 for x in data["suppliers"] if x["risk"] >= 7),
        },
        **data
    })

@app.post("/api/analyze")
def analyze():
    payload = request.get_json(silent=True) or {}
    disruption = payload.get("disruption", "").strip()
    if not disruption:
        return jsonify({"error": "Please enter a disruption description."}), 400
    return jsonify(run_disruption_analysis(disruption))

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
