from agents.utils import generate_text

def research_agent(text):
    prompt = f"""
    You are a research analyst. Analyze the following content and extract:
    - Key facts
    - Main topics
    - Target audience
    - Tone and style

    Content: {text}
    """
    return generate_text(prompt)