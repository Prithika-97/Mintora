import openai
from .config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_content(prompt: str, content_type: str = "blog") -> str:
    system_prompt = f"You are an expert {content_type} writer. Generate high-quality content."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        max_tokens=600,
        temperature=0.8
    )

    return response.choices[0].message['content'].strip()