import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Iris.csv")

# Page Config
st.set_page_config(page_title="Iris Dataset Dashboard", layout="wide")

# Animated CSS Theme
st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #141e30, #243b55, #1f2933, #111827);
    background-size: 400% 400%;
    animation: gradientBG 18s ease infinite;
    color: #f9fafb;
}

@keyframes gradientBG {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.main-title {
    font-size: 2.6rem;
    font-weight: 900;
    text-align: center;
    margin-bottom: 0.5rem;
    background: linear-gradient(90deg, #f97316, #facc15, #22c55e, #38bdf8, #6366f1);
    -webkit-background-clip: text;
    color: transparent;
    animation: titleGlow 3s ease-in-out infinite alternate;
}

@keyframes titleGlow {
    0%   { text-shadow: 0 0 8px rgba(248, 250, 252, 0.2); transform: translateY(0px); }
    100% { text-shadow: 0 0 18px rgba(248, 250, 252, 0.6); transform: translateY(-2px); }
}

.subtitle {
    text-align: center;
    font-size: 1.1rem;
    color: #e5e7eb;
    margin-bottom: 1.3rem;
    opacity: 0;
    animation: fadeInUp 0.9s ease forwards;
    animation-delay: 0.4s;
}

.section-card:hover {
    transform: translateY(-4px) scale(1.01);
    box-shadow: 0 26px 60px rgba(15, 23, 42, 0.9);
    border-color: rgba(248, 250, 252, 0.35);
}

.stTabs [role="tablist"] {
    gap: 0.25rem;
}

.stTabs [role="tab"] {
    background: rgba(15, 23, 42, 0.7);
    padding: 0.5rem 1rem;
    border-radius: 999px;
    font-weight: 600;
    color: #e5e7eb;
    border: 1px solid transparent;
    transition: background 0.2s ease, transform 0.15s ease, border 0.2s ease;
}

.stTabs [role="tab"]:hover {
    transform: translateY(-1px);
    border-color: rgba(248, 250, 252, 0.4);
}

.stTabs [role="tab"][aria-selected="true"] {
    background: linear-gradient(90deg, #f97316, #eab308, #22c55e);
    color: #020617;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.55);
}

[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.95) !important;
    backdrop-filter: blur(14px);
    border-right: 1px solid rgba(148, 163, 184, 0.5);
}

[data-testid="stSidebar"] h1, 
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #e5e7eb;
}

.element-container:has(canvas), 
.element-container:has(svg) {
    animation: fadeIn 0.6s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(4px); }
    to   { opacity: 1; transform: translateY(0px); }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0px); }
}

[data-testid="stMetricValue"] {
    color: #facc15;
}

[data-testid="stMetricDelta"] {
    color: #22c55e;
}

[data-testid="stDataFrame"] {
    background: rgba(15, 23, 42, 0.9) !important;
    border-radius: 0.75rem;
    border: 1px solid rgba(148, 163, 184, 0.35);
}

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: rgba(148, 163, 184, 0.8);
    border-radius: 999px;
}

::-webkit-scrollbar-track {
    background: transparent;
}
</style>
""", unsafe_allow_html=True)

# Titles
st.markdown('<p class="main-title">🌸 Iris Dataset Visualization Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Explore patterns between Sepal & Petal measurements</p>', unsafe_allow_html=True)

# Image
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
st.image(
   "iris flower.png",
    caption="Iris Flower — Sepal & Petal Length & Width",
    width=650
)
st.markdown("</div>", unsafe_allow_html=True)

# Dataset Preview
st.markdown("### 🔍 Dataset Preview")
st.dataframe(df, use_container_width=True)

# Visualization Selection
st.markdown("### 📊 Choose a Visualization")
plot_option = st.selectbox(
    "Select a graph to visualize",
    [
        "Count Plot (Species)",
        "Scatter Plot (Petal)",
        "Scatter Plot (Sepal)",
        "Pairplot",
        "Correlation Heatmap"
    ]
)

st.markdown("### 📌 Visualization Result")

if plot_option == "Count Plot (Species)":
    fig = plt.figure(figsize=(7, 4))
    sns.countplot(data=df, x="Species")
    plt.title("Count of Each Iris Species")
    st.pyplot(fig)

elif plot_option == "Scatter Plot (Petal)":
    fig = plt.figure(figsize=(7, 4))
    sns.scatterplot(data=df, x="PetalLengthCm", y="PetalWidthCm", hue="Species")
    plt.title("Petal Length vs Width")
    st.pyplot(fig)

elif plot_option == "Scatter Plot (Sepal)":
    fig = plt.figure(figsize=(7, 4))
    sns.scatterplot(data=df, x="SepalLengthCm", y="SepalWidthCm", hue="Species")
    plt.title("Sepal Length vs Width")
    st.pyplot(fig)

elif plot_option == "Pairplot":
    st.write("This may take a few seconds...")
    fig = sns.pairplot(df, hue="Species")
    st.pyplot(fig)

elif plot_option == "Correlation Heatmap":
    fig = plt.figure(figsize=(7, 4))
    sns.heatmap(df.iloc[:, 1:5].corr(), annot=True, cmap="coolwarm")
    plt.title("Feature Correlation Heatmap")
    st.pyplot(fig)

# Insights Section
st.markdown("### 📌 Conclusion & Insights")
st.markdown("""
<div class="section-card" style="padding:15px; background:rgba(255,255,255,0.05); border-radius:12px; border:1px solid rgba(148,163,184,0.35);">
<ul>
<li><b>Iris-setosa</b> has the smallest sepal & petal measurements.</li>
<li><b>Iris-virginica</b> has the largest petal dimensions.</li>
<li>Petal features are most important for differentiating species.</li>
<li>Petal length & width show very strong correlation.</li>
</ul>
</div>
""", unsafe_allow_html=True)


