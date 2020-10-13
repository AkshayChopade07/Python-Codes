# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 14:10:17 2020

@author: Immortal
"""


import psutil 
from plyer import notification
import time

battery=psutil.sensors_battery()
while(True):
        percent = battery.percent()
        notification.notify(
            title="Battery Percentage", message=str(percent)+"%Battery Remaining", timeout=10)
        
        time.sleep(60*60)
        continue