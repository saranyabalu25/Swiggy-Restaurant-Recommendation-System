import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import OneHotEncoder

# Set config
st.set_page_config(page_title="Swiggy Recommender", layout="wide")

# Load files
DATA_PATH = "cleaned_data.csv"
MODEL_PATH = "kmeans_model.pkl"
ENCODER_PATH = "encoder.pkl"

# Load data and models
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

@st.cache_resource
def load_model_and_encoder():
    kmeans = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
    return kmeans, encoder

df = load_data()
kmeans, encoder = load_model_and_encoder()

# UI: Home
st.title("🍽️ Swiggy’s Restaurant Recommendation System")
st.markdown("Get restaurant suggestions based on your city, cuisine, rating, and price.")

st.sidebar.header("User Preferences")

# Get input
city = st.sidebar.selectbox("Select City", sorted(df["city"].unique()))
cuisine = st.sidebar.selectbox("Select Cuisine", sorted(df["cuisine"].unique()))
rating = st.sidebar.slider("Minimum Rating", 0.0, 5.0, 3.0, step=0.1)
price = st.sidebar.slider("Maximum Price (approx)", int(df["price"].min()), int(df["price"].max()), 300)

if st.sidebar.button("Get Recommendations"):
    try:
        # Prepare user input for encoding
        input_dict = {
            'city': [city],
            'cuisine': [cuisine],
            'rating': [rating],
            'price': [price]
        }
        input_df = pd.DataFrame(input_dict)

        # Apply OneHotEncoding
        encoded_input = encoder.transform(input_df).toarray()

        # Predict the cluster
        cluster_label = kmeans.predict(encoded_input)[0]

        # Apply filtering
        recommendations = df[
            (df['city'] == city) &
            (df['cuisine'] == cuisine) &
            (df['rating'] >= rating) &
            (df['price'] <= price) &
            (df['cluster'] == cluster_label)
        ]

        # Display results
        if not recommendations.empty:
            st.subheader(f"Top {len(recommendations)} Restaurants for {cuisine} in {city}")
            for _, row in recommendations.iterrows():
                st.markdown(f"### 🍴 {row['restaurant_name']}")
                st.markdown(f"- 📍 City: {row['city']}")
                st.markdown(f"- ⭐ Rating: {row['rating']}")
                st.markdown(f"- 💰 Price: ₹{row['price']}")
                st.markdown("---")
        else:
            st.warning("No matching restaurants found. Try changing your inputs.")
    except Exception as e:
        st.error(f"An error occurred: {e}")