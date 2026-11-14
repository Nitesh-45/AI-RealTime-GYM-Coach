from services.config.workout_config import PROMPT
from google.genai import types


class LLMCoach:
    def __init__(self, gemini_client):
        self.client = gemini_client
        self.history = []
        self.system_prompt = PROMPT

    def give_feedback(self, event, issue):
        prompt = f"Event: {event}"

        if issue:
            prompt += f" Form Issue: {issue}"

        contents = [
            types.Content(
                role="model" if message["role"] == "assistant" else "user",
                parts=[types.Part.from_text(text=message["content"])],
            )
            for message in self.history[-10:]
        ]
        contents.append(
            types.Content(role="user", parts=[types.Part.from_text(text=prompt)])
        )

        response = self.client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=self.system_prompt,
                temperature=0.4,
            ),
        )

        text = (response.text or "").strip()
        if not text:
            raise RuntimeError("Gemini returned an empty coaching response.")

        self.history.append({"role": "user", "content": prompt})
        self.history.append({"role": "assistant", "content": text})

        return text
    