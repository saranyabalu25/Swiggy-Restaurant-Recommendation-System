# Swiggy-Restaurant-Recommendation-System

# 🍽️ Swiggy’s Restaurant Recommendation System using Streamlit

## 📌 Project Title
**Swiggy’s Restaurant Recommendation System using Streamlit**

## 🧠 Domain
Recommendation Systems | Data Analytics | Streamlit App Development

## 🎯 Objective
To develop a restaurant recommendation system that suggests personalized dining options based on user preferences such as **city, cuisine, rating, and price**. This system uses **K-Means Clustering** and **One-Hot Encoding** to deliver relevant restaurant suggestions through a **Streamlit** web app interface.

---

## 🛠️ Skills Applied
- Data Preprocessing (Cleaning, Encoding)
- Clustering using K-Means
- Streamlit Application Development
- Python Programming
- Machine Learning for Recommendation
- Pickle Model Serialization

---

## 📂 Dataset Description
Raw Dataset Columns:
- `id`, `name`, `city`, `rating`, `rating_count`, `cost`, `cuisine`, `lic_no`, `link`, `address`, `menu`

Processed Dataset Columns (`cleaned_data.csv`):
- `restaurant_name`, `city`, `cuisine`, `rating`, `votes`, `price`, `city_encoded`, `cuisine_encoded`, `cluster`

---

## ✅ Project Workflow

### 1. 🔍 Data Cleaning
- Removed duplicates
- Handled missing values
- Renamed and reorganized columns
- Output saved as `cleaned_data.csv`

### 2. ⚙️ Data Preprocessing
- One-Hot Encoding applied to `city` and `cuisine`
- Features standardized for clustering
- Saved as `encoder.pkl` and encoded dataset
- K-Means model trained and saved as `kmeans_model.pkl`

### 3. 🔎 Clustering-Based Recommendation
- User inputs are encoded using the saved encoder
- Cluster is predicted using the KMeans model
- Recommendations are selected from the same cluster and filtered using user preferences

### 4. 🎨 Streamlit App Interface
- Interactive UI with:
  - City and Cuisine dropdowns
  - Sliders for rating and price
  - Real-time recommendations
- Clean, styled layout with a homepage banner

---

## 💡 Business Use Cases
- **Personalized Recommendations:** Tailored restaurant discovery.
- **Customer Experience:** Simplifies decision-making for users.
- **Market Insights:** Identifies trends in cuisines and pricing.
- **Operational Planning:** Helps restaurants target popular demand zones.

---

## 🖥️ How to Run

### Requirements:
- Python 3.9 or above
- Streamlit
- Pandas, NumPy, scikit-learn, joblib

### Steps:
```bash
pip install streamlit pandas numpy scikit-learn joblib
streamlit run swiggy_app.py
Ensure cleaned_data.csv, kmeans_model.pkl, and encoder.pkl are in the same folder or update the paths accordingly.

📦 Files and Deliverables
File Name	Description
cleaned_data.csv	Cleaned and processed dataset
encoder.pkl	One-Hot Encoder for Streamlit app
kmeans_model.pkl	Trained K-Means Clustering model
swiggy_app.py	Final Streamlit application code
README.md	Project overview and documentation

📊 Results & Key Insights
Real-time, accurate restaurant suggestions

Responsive and user-friendly interface

Filtered based on practical preferences

Demonstrates scalable recommendation pipeline
