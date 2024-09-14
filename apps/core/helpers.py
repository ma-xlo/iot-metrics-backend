from datetime import datetime
from dateutil import parser

ONLINE_TIME_THRESHOLD = 300

def is_device_online(device_data):
    # Get the timestamp string from the last entry
    timestamp_str = device_data[-1]['timestamp']
    
    # Parse the timestamp string into a datetime object using dateutil.parser
    last_timestamp = parser.parse(timestamp_str)
    current_time = datetime.now()
    
    # Calculate the time difference in seconds
    if (current_time.timestamp() - last_timestamp.timestamp()) > ONLINE_TIME_THRESHOLD:
        return False

    return True