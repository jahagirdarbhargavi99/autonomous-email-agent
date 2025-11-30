import re
import json
import google.generativeai as genai

class ClassifierAgent:

    def __init__(self, model_name="gemini-2.5-flash"):
        self.model = genai.GenerativeModel(model_name)

    def classify(self, email_text):
        print("\nClassifierAgent: Classifying email...")

        prompt = f"""
Return JSON only.

Required JSON structure:
{{
  "category": "",
  "summary": "",
  "entities": [],
  "urgency": ""
}}

Urgency must be: High, Medium, Low

Email:
{email_text}
"""

        try:
            response = self.model.generate_content(prompt)
            raw = response.text

            raw = raw.replace("```json", "").replace("```", "").strip()

            match = re.search(r"\{.*\}", raw, re.DOTALL)
            if not match:
                raise ValueError(f"No JSON found: {raw}")

            data = json.loads(match.group(0))

            # defaults
            data.setdefault("category", "Other")
            data.setdefault("entities", [])
            data.setdefault("summary", f"General request: {email_text[:60]}")
            if data.get("urgency") not in ["High", "Medium", "Low"]:
                data["urgency"] = "Medium"

            print("ClassifierAgent: Classification complete.")
            return data

        except Exception as e:
            print("ClassifierAgent Error:", e)
            return {
                "category": "Other",
                "summary": f"Fallback summary for: {email_text[:50]}",
                "entities": [],
                "urgency": "Medium"
            }
