# Driver Drowsiness Detection 🚗💤

This project detects driver drowsiness in real-time using Computer Vision and Deep Learning.
It monitors eye states (open/closed) via webcam and triggers an alarm if the driver closes eyes for more than a few seconds.

# 📊 Features

1.**Real-time Eye Monitoring** – Detects driver’s face and eyes using webcam.

2.**Eye State Detection** – Classifies eyes as Open or Closed using deep learning model.

3.**Drowsiness Alert** – Triggers alarm sound + red screen warning if eyes remain closed for long.

4.**Live Web App Interface** – Built with Streamlit, shows live video with alerts.

5.**Data Logging** – Stores detection results (timestamp, eye state, alerts) in Supabase database.

# Project Structure 

DRIVER-DROWSINESS-DETECTION-SYSTEM/
|
|---API/                #backend API
│   ├── main.py         #FastAPI endpoints
|--- Frontend/
│   ├── app.py          #Straemlit web interface
|---src/                #core application logic
│   ├── db.py           #Database operations
│   ├── logic.py        #Business Logic and task opeartions
├── .env                #Python variables
├── README.md           #Project Documentation 
├── requirements.txt    #Python dependencies

# Quick Start
# 1.Prerequisites
- Python 3.8 or higher
- A supabase account
- Git(optional,for cloning)

# 2..Clone or Download the project
# Option 1:Clone with git
git clone <your-repo-url>

# Option 2: Download and extract ZIP file

### 3. Install Dependies

# Install all required Python packages
pip install -r requirements.txt

### 3: Setup Supabase Databse

1.Create Supabase Project:

2.Create the tasks table:

- Go to SQL Editor in your Supabase dashboard
- Run this sql command

```sql

CREATE TABLE DrowsinessLogs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    driver_name VARCHAR(50),         -- Driver’s name (optional)
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,  
    eye_status VARCHAR(10),          -- Open / Closed
    drowsiness_score INT,            -- Duration of closed eyes
    alert_triggered BOOLEAN,         -- 1 = Yes (alarm played), 0 = No
    image_path VARCHAR(255)          -- Path to saved snapshot (optional)
);
```
3. **Get Your Credentials:
### 4. Configure Environment variables

1.Create a `.env` file in the project root

2.Add your supabase credentials to `.env`:
SUPABASE_URL=your_projecr_url_here
SUPABASE_KEY=your_anon_key_here

**Example:**
SUPABASE_URL="https://your-project.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

### 5.Run the Application

## Streamlit Frontend
streamlit run Frontend/app.py

The app will open in your browser at `http://localhost:8081`

## FastAPI Backend

cd API
python main.py

The API will be available at `http://localhost:8000`

## How to use

## 1.Launch the Application

Start the backend API first (optional if using only Streamlit frontend):

cd API
python main.py


The API will run at http://localhost:8000.

Start the Streamlit frontend:

streamlit run Frontend/app.py


This opens a browser window showing the live dashboard.

## 2.Using the Dashboard

Allow webcam access when prompted.

The live video feed will appear in the interface.

Your eyes will be monitored in real-time for drowsiness.

## 3. Drowsiness Alerts

If your eyes remain closed beyond the threshold:

An alarm sound will play.

A red warning overlay will appear on the video feed.

## 4.Data Logging

Each detection is logged automatically to Supabase:

Timestamp of detection

Eye status (Open/Closed)

Drowsiness score

Alert triggered (Yes/No)

Optional snapshot image path

## Technical Details

### Technologies used

-**Frontend**: Streamlit(Python web framework)
-**Backend**: FastAPI(Python REST API Framework)
-**Database**: Supabase(PostgreSQL-based backend-as-a-service)
-**Language**: Python 3.8+
-**Computer Vision & Deep Learning**: OpenCV and a pre-trained eye state detection model for real-time monitoring.

### Key Components

1. **`src/db/.py`**:Database operations
    -Handles all CRUD operations with Supabase

2. **`src/login.py`**:Business logic 
    -Task validation and processing.

## Troubleshooting

## Common Issues

1. **"Module not found" error**
    -Make sure you've installed all dependencies:`pip install -r requirements.txt`
    -Check that you're running commands from the correct directory

## Future Enhancements 🚀

1.Integrate with mobile apps for real-time monitoring on smartphones.

2.Implement driver authentication to track individual fatigue history.

3.Enhance alerts with vibrations, voice warnings, or SMS notifications.

4.Improve AI model accuracy for low-light and multiple-angle detection.

5.Use historical data for predictive analytics to prevent fatigue before it happens.

## Support 

If you encounter any issues or have question:
**Email**:harshithanalubala@gmail.com
**Contact**: 8328598014