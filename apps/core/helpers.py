from datetime import datetime

ONLINE_TIME_THRESHOLD = 300

def is_device_online (device_data):
  timestamp_str = device_data[len(device_data) - 1]['timestamp']
  last_timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")
  current_time = datetime.now()
  
  if ((current_time.timestamp() - last_timestamp.timestamp()) > ONLINE_TIME_THRESHOLD):
    return False;
  
  return True;