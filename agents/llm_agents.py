
import os
import json
from openai import OpenAI


def run_ai_agent(agent_name, instructions, data):
    """Run one AI agent on supplied supply-chain data."""

    if not os.getenv("OPENAI_API_KEY"):
        return {
            "agent": agent_name,
            "status": "error",
            "analysis": "OpenAI API key is not configured."
        }

    try:
        client = OpenAI()

        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-5.5"),
            instructions=(
                f"You are the {agent_name} for a supply-chain "
                "disruption response system. "
                f"{instructions} "
                "Use only the supplied data. Do not invent live "
                "facts, prices, stock levels or delivery times. "
                "Clearly label assumptions and explain your reasoning."
            ),
            input=json.dumps(data, default=str),
            max_output_tokens=500
        )

        return {
            "agent": agent_name,
            "status": "success",
            "analysis": response.output_text
        }

    except Exception as exc:
        # Avoid exposing API keys or other sensitive details.
        print(f"{agent_name} failed: {type(exc).__name__}")
        return {
            "agent": agent_name,
            "status": "error",
            "analysis": "AI analysis failed. Check server logs."
        }
