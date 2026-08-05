import streamlit as st
from PIL import Image
from predict import predict_image
from disease_info import DISEASE_INFO

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Plant Leaf Disease Detection",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LANGUAGE SELECTION ----------------

language = st.sidebar.selectbox(
    "🌐 Select Language / भाषा चुनें",
    ["English", "हिंदी"]
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main{
    background:#F4FFF4;
}

/* Header */

.header{
    background:linear-gradient(90deg,#1B5E20,#43A047,#66BB6A);
    padding:30px;
    border-radius:18px;
    text-align:center;
    color:white;
    box-shadow:0px 6px 15px rgba(0,0,0,.25);
    margin-bottom:25px;
}

/* Cards */

.card{
    background:white;
    border-radius:15px;
    padding:20px;
    box-shadow:0px 5px 12px rgba(0,0,0,.15);
    margin-bottom:20px;
}

/* Prediction Card */

.result-card{
    background:#E8F5E9;
    border-left:8px solid #2E7D32;
    border-radius:12px;
    padding:20px;
    margin-top:20px;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#E8F5E9;
}

/* Footer */

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

.metric{
    font-size:18px;
    font-weight:bold;
    color:#2E7D32;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

st.sidebar.image(
    "https://img.icons8.com/color/96/leaf.png",
    width=80
)

st.sidebar.title("🌿 Plant AI")

st.sidebar.markdown("---")

st.sidebar.success("Transfer Learning Project")

st.sidebar.markdown("""

### 🧠 Model

**EfficientNetB0**

Transfer Learning

---

### 📊 Performance

Validation Accuracy

**96.72%**

---

### 📂 Dataset

PlantVillage

38 Classes

---

### ⚙ Framework

TensorFlow

Keras

Streamlit

""")

st.sidebar.markdown("---")

# ---------------- HEADER ----------------

st.markdown("""

<div class='header'>

<h1>🌿 Plant Leaf Disease Detection</h1>

<h3>Transfer Learning using EfficientNetB0</h3>

<p>
Artificial Intelligence Based Crop Disease Identification System
</p>

</div>

""", unsafe_allow_html=True)

# ---------------- INFO CARDS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🧠 Transfer Learning")

with col2:
    st.success("📊 Accuracy : 96.72%")

with col3:
    st.warning("🌱 38 Disease Classes")

st.write("")

# ---------------- IMAGE UPLOAD ----------------

st.markdown("---")

st.markdown("## 📷 Upload Leaf Image")

uploaded_file = st.file_uploader(
    "Choose a plant leaf image...",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns([0.7, 1.3])

    with col1:

        st.image(
            image,
            caption="Uploaded Leaf Image",
            width=250
        )

    with col2:

        st.write("### 🤖 AI Analysis")

        st.write(
            "Click the button below to detect the disease using the trained AI model."
        )

        if st.button(
            "🔍 Detect Disease",
            use_container_width=True
        ):

            with st.spinner("Analyzing image..."):

                disease, confidence = predict_image(image)

                info = DISEASE_INFO.get(disease)

            st.session_state["disease"] = disease
            st.session_state["confidence"] = confidence
            st.session_state["info"] = info

# ---------------- PREDICTION RESULT ----------------

if "disease" in st.session_state:

    st.markdown("---")

    st.markdown("## 🌱 Prediction Result")

    disease = st.session_state["disease"]
    confidence = st.session_state["confidence"]
    info = st.session_state["info"]

    # Check healthy class
    is_healthy = "healthy" in disease.lower()

    display_name = disease.replace("___", " - ").replace("_", " ")

    st.markdown(f"""
    <div class="result-card">
        <h3>🤖 AI Prediction</h3>
        <h2 style="color:#2E7D32;">{display_name}</h2>
        <p><b>Confidence:</b> {confidence*100:.2f}%</p>
    </div>
    """, unsafe_allow_html=True)

    st.progress(confidence)


    # ---------------- HEALTHY PLANT ----------------

    if is_healthy:

        st.success("🟢 Healthy Plant")

        st.info("""
No disease was detected.

### Recommendations

✅ Continue regular watering.

✅ Provide proper nutrition.

✅ Maintain good sunlight exposure.

✅ Monitor leaves regularly.

✅ Protect the crop from pests.

Your plant appears healthy.
""")



    # ---------------- DISEASE INFORMATION ----------------

    elif info:

        st.write("")

        st.info(info["description"])

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("🔍 Symptoms")

            for symptom in info["symptoms"]:
                st.write(f"✅ {symptom}")


        with col2:

            st.subheader("🌱 Organic Treatment")

            for treatment in info["organic_treatment"]:
                st.write(f"🌿 {treatment}")


        st.write("")


        col3, col4 = st.columns(2)

        with col3:

            st.subheader("🧪 Chemical Treatment")

            for treatment in info["chemical_treatment"]:
                st.write(f"💊 {treatment}")


        with col4:

            st.subheader("🛡 Prevention")

            for tip in info["prevention"]:
                st.write(f"🟢 {tip}")



    else:

        st.warning("Information for this disease is not available yet.")