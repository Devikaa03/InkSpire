from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from agents.research import research_agent
from agents.copywriter import copywriter_agent
from agents.editor import editor_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    text: str


@app.post("/generate")
def generate(data: InputData):
    logs = []

    # 1. Research
    logs.append("🔍 Research Agent analyzing...")
    facts = research_agent(data.text)

    # 2. Copywriter
    logs.append("✍️ Copywriter generating content...")
    content = copywriter_agent(facts)

    # 3. Editor
    logs.append("🛡️ Editor reviewing...")
    review = editor_agent(facts, content)

    # Feedback loop
    if "REJECTED" in review:
        logs.append("❌ Editor rejected. Regenerating...")
        content = copywriter_agent(facts)
        review = editor_agent(facts, content)

    logs.append("✅ Final Approved")

    return {
        "facts": facts,
        "content": content,
        "review": review,
        "logs": logs }