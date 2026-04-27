import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def analyze_profile(profile_text):

    prompt = f"""
Act as a LinkedIn profile coach.

Analyze this profile.

Provide:
1. Profile score out of 100
2. Headline suggestions
3. About section improvements
4. Experience bullet improvements

Profile:
{profile_text[:12000]}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content