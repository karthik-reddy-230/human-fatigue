# 🧠 EEG-Based Human Fatigue Detection System

A simple and interactive web application to detect human fatigue levels using EEG (Electroencephalogram) data. Built with Streamlit and machine learning techniques.

---

## 🚀 Live Demo

👉 **Try the app here:**
https://human-fatigue-csm-d.streamlit.app/

---

## 📌 Features

* 📂 Upload EEG CSV files
* 📊 Visualize raw EEG signals
* 📈 Multi-channel EEG time series graph
* 🧠 Brainwave band power analysis (Delta, Theta, Alpha, Beta)
* ⚠️ Fatigue detection alert system
* 🎯 Fatigue level percentage using gauge chart

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Plotly
* Scikit-learn

---

## 📂 Project Structure

```
├── app.py              # Main Streamlit app
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

---

## ⚙️ Installation & Run Locally

1. Clone the repository:

```
git clone https://github.com/your-username/eeg-fatigue-app.git
cd eeg-fatigue-app
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
streamlit run app.py
```

---

## 📊 How It Works

1. Upload an EEG dataset (CSV format)
2. Extract features like:

   * Delta
   * Theta
   * Alpha
   * Beta
3. Compute fatigue-related ratio
4. Predict fatigue using a machine learning model
5. Display results with:

   * Gauge visualization
   * Alerts
   * Graphs

---

## ⚠️ Note

* Current version uses a **dummy/random prediction model**
* Replace with a trained ML model for real-world use

---

## 🔮 Future Improvements

* ✅ Real-time EEG data integration
* 🤖 Deep learning models (CNN/LSTM)
* 📱 Mobile-friendly UI
* 🔔 Sound alerts for fatigue detection

---

## 👨‍💻 Author

* M Karthikeyan
---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

---
