from agents.utils import generate_text

def copywriter_agent(facts):
    prompt = f"""
    You are a creative copywriter.

    Using this FACT SHEET:
    {facts}

    Generate:

    1. BLOG (500 words, professional, trustworthy)
    2. THREAD (5 posts, engaging, punchy)
    3. EMAIL (1 short teaser paragraph)

    IMPORTANT:
    - Highlight the VALUE PROPOSITION strongly
    - Do NOT invent facts

    Format strictly like:

    BLOG:
    ...

    THREAD:
    ...

    EMAIL:
    ...
    """
    return generate_text(prompt)