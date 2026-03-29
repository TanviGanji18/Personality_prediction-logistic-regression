# 🧠 Personality Predictor (Introvert vs Extrovert)

This project is a Machine Learning web application built using **Streamlit** that predicts whether a person is an **Introvert** or an **Extrovert** based on their behavioral traits.

---

## 🚀 Features

* Interactive UI using Streamlit
* Predicts personality instantly
* Uses trained ML model (`model.pkl`)
* Simple and user-friendly inputs

---

## 📊 Input Features

The model uses the following inputs:

* Time spent alone
* Stage fear (Yes/No)
* Social event attendance
* Going outside frequency
* Drained after socializing (Yes/No)
* Friends circle size
* Social media post frequency

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* NumPy
* Pandas

---

## 📂 Project Structure

```
├── app.py                  # Streamlit app
├── model.pkl              # Trained ML model
├── scaler.pkl (optional)  # Scaler (if used)
├── personality_dataset.csv
├── task.ipynb             # Training notebook
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone <your-repo-link>
cd <your-folder>
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```
streamlit run app.py
```

---

## ⚠️ Important Notes

* Ensure `model.pkl` is present in the same folder as `app.py`
* If scaling was used during training, include `scaler.pkl`
* Make sure feature order in app matches training

---

## 🎯 Output

* 🎉 Extrovert
* 🧘 Introvert

---

## 📌 Future Improvements

* Improve model accuracy
* Add more personality features

---

## Live App
* Streamlit Deployment : https://tanviganji18-personality-prediction-logistic-regress-app-ctsxpn.streamlit.app/

---

## 👩‍💻 Author

Tanvi Ganji

---
