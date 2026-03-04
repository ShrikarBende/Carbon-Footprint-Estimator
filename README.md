# 🌱 Carbon Footprint Estimator

> An AI-powered platform to measure, analyze, and reduce your environmental impact using machine learning.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![ML](https://img.shields.io/badge/ML-scikit--learn-yellowgreen?logo=scikitlearn)
![Groq](https://img.shields.io/badge/ML-Groq-orange?logo=groq)
![Linear Regression](https://img.shields.io/badge/ML-Linear%20Regression-blue?logo=python)
![Random Forest Regressor](https://img.shields.io/badge/ML-Random%20Forest%20Regressor-green?logo=python)

---

## 📖 Overview

The **Carbon Footprint Estimator** is an AI-powered platform that helps individuals and organizations measure and reduce their environmental impact. Using machine learning and real-time data, it delivers personalized carbon assessments, identifies emission hotspots, and provides practical strategies to lower emissions and support better decision-making.

---

## ✨ Features

- 🤖 **ML-Powered Estimation** — Trained model (`carbon_model.pkl`) predicts carbon output based on input data
- 📊 **Carbon Factor Dataset** — Uses a real-world dataset of carbon emission factors across different activities and categories
- 🌍 **Personalized Assessments** — Tailored carbon footprint reports based on user inputs
- 🔍 **Emission Hotspot Identification** — Pinpoints which activities contribute most to your footprint
- 💡 **Actionable Recommendations** — Suggests practical strategies to lower emissions
- 🧪 **Exploratory Notebook** — Full model training pipeline documented in `project.ipynb`
- 🖥️ **Web App Interface** — Streamlit-based app (`app.py`) for interactive estimation

---

## 🗂️ Project Structure

```
Carbon-Footprint-Estimator/
│
├── app.py                     # Streamlit web application
├── project.ipynb              # Jupyter Notebook: EDA, model training & evaluation
├── carbon_factor_dataset.csv  # Carbon emission factors dataset
├── carbon_model.pkl           # Trained ML model (pickle file)
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShrikarBende/Carbon-Footprint-Estimator.git
   cd Carbon-Footprint-Estimator
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit scikit-learn pandas numpy matplotlib seaborn
   ```

3. **Run the web app**
   ```bash
   streamlit run app.py
   ```

4. **Or explore the Jupyter Notebook**
   ```bash
   jupyter notebook project.ipynb
   ```

---

## 🧠 How It Works

1. **Data Input** — Users provide details about their lifestyle (transport, energy usage, diet, etc.)
2. **Feature Processing** — Inputs are mapped against the carbon factor dataset
3. **ML Prediction** — The pre-trained model estimates total CO₂ emissions (kg/year)
4. **Insights & Recommendations** — The app highlights emission hotspots and suggests reduction strategies

---

## 📦 Dataset

The `carbon_factor_dataset.csv` contains carbon emission factor values for various activities, energy sources, and consumption categories. These factors are used to convert user inputs into equivalent CO₂ emissions.

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---


## 👤 Author

**Shrikar Bende**
- GitHub: [@ShrikarBende](https://github.com/ShrikarBende)

---

> *"The Earth does not belong to us; we belong to the Earth."* 🌎
