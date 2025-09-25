#db_manager.py 
import os
from supabase import create_client
from dotenv import load_dotenv

#load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url,key)

#Insert logs
def insert_log(driver_name, eye_status, drowsiness_score, alert_triggered, image_path=None):
      return supabase.table("DrowsinessLogs").insert({
        "driver_name": driver_name,
        "eye_status": eye_status,
        "drowsiness_score": drowsiness_score,
        "alert_triggered": alert_triggered,
        "image_path": image_path
    }).execute()

# Get all logs
def fetch_logs(limit=10):
    return supabase.table("DrowsinessLogs").select("*").order("timestamp", desc=True).limit(limit).execute()

#update log
def update_log(log_id, updated_data: dict):
    return supabase.table("DrowsinessLogs").update(updated_data).eq("log_id", log_id).execute()

#Delete log
def delete_log(log_id):
    return supabase.table("DrowsinessLogs").delete().eq("log_id", log_id).execute()
