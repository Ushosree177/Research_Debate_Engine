import google.generativeai as genai
import os
from dotenv import load_dotenv
from retriever import search_papers

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

GEMINI_MODEL = "gemini-flash-latest"


def call_gemini(system: str, user: str) -> str:
    try:
        m = genai.GenerativeModel(GEMINI_MODEL)
        prompt = f"{system}\n\n{user}"
        response = m.generate_content(prompt)
        return response.text
    except Exception as e:
        error = str(e)
        if "429" in error:
            return "[Rate limit hit. Please wait 60 seconds and try again.]"
        if "404" in error or "not found" in error.lower():
            return "[Model not available. Make sure your API key is valid.]"
        return f"[Gemini error: {error}]"



PROPONENT = """You are a rigorous academic proponent debating a research topic.
Your job: make the strongest possible evidence-based argument IN FAVOR of the claim.
Rules:
1. Keep your response under 250 words
2. Cite paper titles from the provided papers where relevant
3. Be persuasive but factually grounded
4. Do not acknowledge weaknesses - that is the skeptic's job"""

SKEPTIC = """You are a rigorous academic skeptic debating a research topic.
Your job: identify methodological weaknesses, counter-evidence, and alternative interpretations.
Rules:
1. Keep your response under 150 words
2. Reference specific papers if they have limitations worth noting
3. Critique precisely — do not dismiss the topic entirely
4. Focus on what the evidence does NOT yet prove"""

SYNTHESIZER = """You are a balanced academic synthesizer.
You have read arguments from both a proponent and a skeptic on a research topic.
Your job: deliver a fair, nuanced verdict.
Rules:
1. Keep your response under 200 words
2. State clearly what the current evidence supports
3. Acknowledge what remains uncertain or contested
4. Suggest one or two directions for future research"""


def run_debate(topic: str):

    yield "Searching arXiv for relevant papers...\n\n"
    papers = search_papers(topic)
    yield f"**Papers found:**\n\n{papers}\n\n---\n\n"

    context = f"Topic: {topic}\n\nRelevant papers:\n{papers}"

    yield "**Proponent** is building the case...\n\n"
    pro = call_gemini(PROPONENT, context)
    yield f"### Proponent\n{pro}\n\n---\n\n"

    yield "**Skeptic** is preparing the counter-argument...\n\n"
    skep = call_gemini(SKEPTIC, context + f"\n\nProponent's argument:\n{pro}")
    yield f"### Skeptic\n{skep}\n\n---\n\n"

    yield "**Synthesizer** is forming the verdict...\n\n"
    synth = call_gemini(
        SYNTHESIZER,
        f"Topic: {topic}\n\nProponent:\n{pro}\n\nSkeptic:\n{skep}"
    )
    yield f"### Verdict\n{synth}\n\n"