
# **Smart Flight Assistant ✈️** 
This is an end-to-end ML-powered web application to predict flight delays based on parameters input by user, compare airlines performance by analyzing past flight records and estimating CO2 emissions. It is a useful travel-planning assistant for air commuters. 

## **📌 Features**  
✅ Implemented an FT-Transformer model using PyTorch Tabular, achieving a normalized MAE of 0.0023 for delay prediction, outperforming traditional models like Random Forest and XGBoost.

✅ Built a Django-based web app with HTML, CSS, JavaScript, and Plotly.js for interactive visualizations, enabling users to
 predict delays, compare airlines, and calculate CO2 footprints

✅  Deployed a scalable, user-friendly interface with MVC architecture, integrated with GPU-accelerated training (Kaggle
 P100) and exportable model pipelines (TorchScript/ONNX).

✅ Enhanced operational efficiency and passenger experience by providing actionable insights for airlines and travelers, with
 future plans for real-time data integration and global scalability
 

## **📂 Project Structure** 
```
webapp/
├── .pt_tmp
├── .myp
├── myapp/

   ├── __pycache__/
       ├── __init__.cpython-311.pyc
       ├── admin.cpython-311.pyc
       ├── apps.cpython-311.pyc
       ├── models.cpython-311.pyc
       ├── urls.cpython-311.pyc
       ├── views.cpython-311.pyc
   ├── migrations/
       ├── __pycache__/
           ├── __init__.cpython-311.pyc
           ├── 0001_initial.cpython-311.pyc
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── static/
│   │   ├── styles.css
│   ├── init_.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│   └── static/
│       ├── images/
│       ├── images2/
│       ├── images3/
│       ├── co2_footprint.css
│       ├── compare_airlines.css
│       ├── delay_analysis.css
│       ├── delay_predictor.css
│       ├── live_tracking.css
│       ├── statistics.css
│       ├── style.css
│       └── styles.css
    └── templates/
│       ├── about.html
│       ├── co2_footprint.html
│       ├── compare_airlines.html
│       ├── delay_analysis.html
│       ├── delay_predictor.html
│       ├── home.html
│       ├── live_tracking.html
│       ├── statistics.html

├── webapp/
│   ├── __pycache__/
        ├── __init__.cpython-311.pyc
        ├── settings.cpython-311.pyc
        ├── urls.cpython-311.pyc
        ├── wsgi.cpython-311.pyc
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitattributes
├── db.sqlite3
├── manage.py
└── README.md
```


## **🚀 Installation & Setup**
### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/your-username/Smart-Flight-Assistant.git
cd task_optimizer
```

### **2️⃣ Create a Virtual Environment**  
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **4️⃣ Run Migrations & Start Server**  
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### **5️⃣ Access the Web App**  
Open **http://127.0.0.1:8000/** in your browser.

---

## **🖥️ Usage**

### ** Flight Delay Predictions**  
1️⃣ Navigate to ``  
2️⃣  
3️⃣  
4️⃣  

### ** Airlines Performance Comparison**  
1️⃣ Navigate to ``  
2️⃣ **Bar Chart**
3️⃣ 
4️⃣ 

### ** Estimate CO2 emissions**  
1️⃣ Navigate to ``  
2️⃣  
3️⃣  


## **📌 Key Technologies Used**
✅ **Backend:** Django (Python)  
✅ **Frontend:** HTML, CSS, JavaScript  
✅ **Machine Learning:** FT Transformer, Pytorch Tabular 
✅ **Data Visualization:** Plotly.js  
✅ **Database:** SQLite  


## **🛠️ Useful Git Commands**
### **Initialize a New Repository**  
```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/Smart-Flight-Assistant.git
git push -u origin main
```

### **Common Git Commands**  
```sh
git status               # Check changes
git add .                # Stage all changes
git commit -m "Message"  # Commit changes
git pull origin main     # Pull latest changes
git push origin main     # Push changes
```
---

## **🚀 Future Enhancements**  

## **📌 Contributors** 
👤 **Param Parekh**   
📧 Email: parammparekh13@gmail.com
👤 **Mihir Gore** 
📧 Email: 



