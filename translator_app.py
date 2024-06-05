import streamlit as st

translation_dict = {
    "I": "Ndi",
    "you": "wowe",
    "he": "we",
    "she": "we",
    "we": "twebwe",
    "they": "bose",
    "love": "nkunda",
    "like": "nkunda",
    "to": "ku",
    "sleep": "ryama",
    "eat": "rya",
    "drink": "nywa",
    "walk": "genda",
    "run": "iruka",
    "read": "soma",
    "write": "andika",
    "play": "kina",
    "work": "kora",
    "study": "iga",
    "house": "inzu",
    "school": "ishuri",
    "food": "ibiryo",
    "water": "amazi",
    "book": "igitabo",
    "pen": "ikaramu",
    "happy": "ishimye",
    "sad": "ababaye",
    "friend": "inshuti",
    "family": "umuryango"
}


def translate_to_kinyarwanda(sentence):
    words = sentence.split()
    translated_words = [translation_dict.get(word.lower(), word) for word in words]
    return " ".join(translated_words)


st.title("English to Kinyarwanda Translator")

english_sentence = st.text_input("Enter a sentence in English:", "I love to sleep")


if st.button("Translate"):
    kinyarwanda_sentence = translate_to_kinyarwanda(english_sentence)
    st.write("Translation in Kinyarwanda:")
    st.write(kinyarwanda_sentence)


import random

random_sentences = [
    "I love to eat",
    "You like to drink water",
    "He plays with his friend",
    "She reads a book",
    "We work at the house",
    "They study at school",
    "I am happy with my family",
    "You are sad without food"
]

if st.button("Give me a random sentence"):
    random_sentence = random.choice(random_sentences)
    st.write("Try translating this sentence:")
    st.write(random_sentence)
    kinyarwanda_random_sentence = translate_to_kinyarwanda(random_sentence)
    st.write("Translation in Kinyarwanda:")
    st.write(kinyarwanda_random_sentence)
