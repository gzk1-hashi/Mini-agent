from datetime import datetime
from pathlib import Path 
import os
# from tavily import TavilyClient

def get_current_time() -> str:
    currentTime = datetime.now()
    dateTime = currentTime.strftime("%Y-%m-%d %H:%M:%S")
    print(dateTime)
    return dateTime

TIME_TOOL = {'name': get_current_time, 'description': "HI, How are you doing today", 'input_schema':{"type": "object":, "properties"{}}}


currentTime = get_current_time()
print(currentTime)

