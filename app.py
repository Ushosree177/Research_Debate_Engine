import gradio as gr
from debate import run_debate

EXAMPLES = [
    "Does social media use worsen adolescent mental health?",
    "Can large language models reason or do they just pattern-match?",
    "Is intermittent fasting effective for long-term weight loss?",
    "Does bilingualism delay the onset of dementia?",
    "Does screen time negatively affect children's cognitive development?",
]


def stream_debate(topic: str):
    if not topic.strip():
        yield "Please enter a research topic to begin."
        return
    full = ""
    for chunk in run_debate(topic):
        full += chunk
        yield full


with gr.Blocks(title="Research Debate Engine", theme=gr.themes.Soft()) as demo:

    gr.Markdown(
        """
        ## Research Debate Engine
        Enter any academic topic. Three AI personas will debate it using real papers from arXiv.

        | Persona | Role |
        |---|---|
        | **Proponent** | Makes the strongest case *for* the claim |
        | **Skeptic** | Challenges the evidence and methodology |
        | **Synthesizer** | Delivers a balanced, evidence-based verdict |
        """
    )

    topic_box = gr.Textbox(
        placeholder="e.g. Does exercise improve academic performance in students?",
        label="Research topic",
        lines=2
    )

    gr.Examples(
        examples=EXAMPLES,
        inputs=topic_box,
        label="Try an example topic"
    )

    run_btn = gr.Button("Start Debate", variant="primary", size="lg")
    output = gr.Markdown(label="Debate output")

    run_btn.click(
        fn=stream_debate,
        inputs=topic_box,
        outputs=output
    )

    gr.Markdown(
        """
        ---
        **Powered by:** Gemini · arXiv <p align="right">A Project by U. Raha & Yazhini</p>
        """
    )

demo.launch()