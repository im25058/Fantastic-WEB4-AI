import streamlit as st
import uuid
import datetime

from agent import ResearchSystem
from hash_utils import generate_hash
from blockchain import store_on_chain


st.title("Fantastic WEB4 AI")

query = st.text_input("Enter your research question")

if st.button("Run AI Agent"):

    agent = ResearchSystem()

    report, logs, confidence = agent.run(query)

    st.subheader("Research Report")
    st.write(report)

    st.subheader("Verification Result")
    st.write("Confidence Score:", confidence, "%")

    report_hash = generate_hash(report)

    execution_id = str(uuid.uuid4())

    tx = store_on_chain(execution_id, report_hash)

    st.subheader("Verification")

    st.write("Execution ID:", execution_id)
    st.write("Report Hash:", report_hash)
    st.write(tx)

    st.subheader("Audit Logs")
    st.json(logs)

    st.subheader("Agent Workflow")

    st.graphviz_chart("""
    digraph {
    User_Query -> Planner_Agent
    Planner_Agent -> Research_Agent
    Research_Agent -> Verification_Agent
    Verification_Agent -> Final_Report
    Final_Report -> Hash_Generation
    Hash_Generation -> Weilchain
    }
    """)
    st.subheader("AI Execution Certificate")

    certificate = f"""
    AI Research Certificate

    Query: {query}

    Execution Time: {datetime.datetime.now()}

    Confidence Score: {confidence}%

    Report Hash: {report_hash}

    Execution ID: {execution_id}

    Anchored On: Weilchain
    """

    st.text(certificate)

    st.download_button(
        "Download Certificate",
        certificate,
        file_name="ai_execution_certificate.txt"
    )