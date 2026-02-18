# 🛡 AI Content Moderation System

An end-to-end Machine Learning web application that automatically detects whether a message is **Safe** or **Harmful** using Natural Language Processing (NLP) and classification algorithms.

The system simulates how social media platforms filter abusive or toxic content in comments, caption and chats.

---

## 🚀 Features
- Detects toxic / abusive language
- Real-time prediction through web interface
- Popup warning for harmful content
- Animated AI scanning loader
- Dark themed modern UI
- Multiple ML algorithms tested (SVM, Logistic Regression, Naive Bayes, Random Forest, Decision tree)
- End-to-end ML deployment

---

## 🧠 Machine Learning Pipeline
1. Data Collection (Instagram captions dataset)
2. Text Preprocessing  
   - Lowercasing  
   - URL removal  
   - Emoji removal  
   - Stopword removal  
   - Tokenization  
3. Feature Extraction using **TF-IDF Vectorizer**
4. Model Training & Comparison
5. Best Model Selection (SVM)
6. Flask Deployment

---

## 🛠 Technologies Used
- Python
- Scikit-learn
- Natural Language Processing (NLP)
- Flask
- HTML, CSS, JavaScript
- Pickle (model saving)

---

## 📂 Project Structure

AI-Content-Moderation/
│
├──index.ipynb
├── app.py
├── model.pkl
├── vectorizer.pkl
├── cleaned_dataset.csv
│
├── templates/
│ └── index.html
│
└── README.md
