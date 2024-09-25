from datetime import datetime

def fetch_clock():
    try:
        current_time = datetime.now()
        return current_time.strftime("%Y-%m-%dT%H:%M:%S")
    except Exception as e:
        print(f"Error fetching time: {e}")
        return None