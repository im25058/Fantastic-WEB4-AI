import streamlit as st
import uuid

from agent import ResearchAgent
from hash_utils import generate_hash
from blockchain import store_on_chain


st.title("Fantastic WEB4 AI")

query = st.text_input("Enter your research question")


if st.button("Run AI Agent"):

    agent = ResearchAgent()

    report, logs = agent.run(query)

    st.subheader("Research Report")

    st.write(report)


    report_hash = generate_hash(report)

    execution_id = str(uuid.uuid4())

    tx = store_on_chain(execution_id, report_hash)


    st.subheader("Verification")

    st.write("Execution ID:", execution_id)

    st.write("Report Hash:", report_hash)

    st.write(tx)


    st.subheader("Audit Logs")

    st.json(logs)

