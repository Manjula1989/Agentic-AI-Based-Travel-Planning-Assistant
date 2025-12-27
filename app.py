import streamlit as st
from travel_agent import get_itinerary

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Agentic AI-Based Travel Planning Assistant",
    page_icon="🧳",
    layout="centered"
)

# -----------------------------
# UI Header
# -----------------------------
st.title("🧳 Agentic AI-Based Travel Planning Assistant")
st.write("Enter your travel request and let the AI plan your trip.")

# -----------------------------
# User Input
# -----------------------------
query = st.text_input(
    "Travel Request",
    "Plan a 3-day trip from Delhi to Goa with budget options"
)

# -----------------------------
# Button Action
# -----------------------------
if st.button("Generate Itinerary"):
    with st.spinner("Planning your trip using Agentic AI..."):
        try:
            result = get_itinerary(query)
            st.success("Trip Generated Successfully!")
            st.markdown(result)
        except Exception as e:
            st.error("Something went wrong")
            st.exception(e)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("🚀 Agentic AI Travel Planner | Internship Project")
