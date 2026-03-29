from agents.utils import generate_text

def editor_agent(facts, content):
    prompt = f"""
    You are a strict content editor. Review this content:
    {content}

    Based on these facts:
    {facts}

    If the content is good, respond with: APPROVED
    If the content needs changes, respond with: REJECTED - (reason)
    """
    return generate_text(prompt)