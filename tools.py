from datetime import datetime
from pathlib import Path 
import os
# from tavily import TavilyClient

def get_current_time() -> str:
    currentTime = datetime.now()
    dateTime = currentTime.strftime("%Y-%m-%d %H:%M:%S")
    print(dateTime)
    return dateTime

TIME_TOOL = {'name': "current time", 'description': "HI, How are you doing today", 'input_schema': {}}


currentTime = get_current_time()
print(currentTime)

