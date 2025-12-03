import streamlit as st
from crewai import Crew
from crew_agents import create_agents
from tasks import create_tasks
from local_llm import LocalLLM

MODEL_PATH = r"C:\Users\ritvika.t\Desktop\crewAI\models\Phi-3-mini-4k-instruct-q4.gguf"   # Update to your model path

@st.cache_resource
def load_local_llm():
    return LocalLLM(model_path=MODEL_PATH)

st.title("Local Trading Research Assistant (No Rate Limits)")

llm = load_local_llm()
agents = create_agents()
tasks = create_tasks(agents)

if st.button("Run Analysis"):
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        llm=llm
    )

    result = crew.kickoff()
    st.subheader("Final Output")
    st.write(result)
