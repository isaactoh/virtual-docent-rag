import streamlit as st
from search.search import search

st.title("RAG Demo")

query = st.text_input(
    "Enter Question"
)

if st.button("search"):
    if query.strip():
        with st.spinner("Searching..."):
            try:
                ans = search(query)
                st.write(ans)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a search query")