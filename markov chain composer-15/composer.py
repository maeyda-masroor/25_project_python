import streamlit as st
import re
import string
import random
from graph import Graph, Vertex

def get_words_from_text_file(uploaded_file):
    text = uploaded_file.read().decode("utf-8") 
    text = ' '.join(text.split())
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words[:1000]

def make_graph(words):
    g = Graph()
    prev_word = None
    for word in words:
        word_vertex = g.get_vertex(word)
        if prev_word:
            prev_word.increment_edge(word_vertex)
        prev_word = word_vertex
    g.generate_probability_mappings()
    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    return composition

# -------------------- Streamlit Interface --------------------

st.set_page_config(page_title="Markov Chain Text Generator")
st.title("Markov Chain Text Generator")
st.markdown("Upload a `.txt` file and generate a new text composition using a Markov Chain model.")

uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file:
    words = get_words_from_text_file(uploaded_file)
    st.success(f"File uploaded successfully! {len(words)} words extracted.")
    
    length = st.slider("Select length of generated text", min_value=20, max_value=500, value=100, step=10)

    if st.button("Generate Composition"):
        g = make_graph(words)
        composition = compose(g, words, length)
        st.subheader("📝 Generated Text")
        st.write(' '.join(composition))
