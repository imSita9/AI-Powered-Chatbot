import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline
from faq_data import faq_pairs

nltk.download('punkt')

questions = list(faq_pairs.keys())
answers = list(faq_pairs.values())

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Transformer model
generator = pipeline("text-generation", model="gpt2")


def get_faq_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    idx = similarity.argmax()

    if similarity[0][idx] > 0.4:
        return answers[idx]

    return None


def generate_ai_response(user_input):
    result = generator(user_input, max_length=50, num_return_sequences=1)
    return result[0]['generated_text']


def get_response(user_input):
    faq_response = get_faq_response(user_input)

    if faq_response:
        return faq_response

    return generate_ai_response(user_input)