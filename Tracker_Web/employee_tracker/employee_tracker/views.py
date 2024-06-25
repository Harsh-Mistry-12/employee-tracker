from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import mysql.connector as mc

today = datetime.now()
formatted_date = today.strftime('%Y%m%d')

db = mc.connect(user='root', password='', host='localhost', database='tracker')
cursor = db.cursor()
cursor.execute("SELECT * FROM `employees`;")
data = cursor.fetchall()

def home(request):
    return render(request, 'home.html')

def screenshot_screener(request):
    return render(request, 'screenshot.html')

def tracker_log(request):
    with open(f'C:\\Users\\Admin\\Documents\\HARSH\\clg_project\\tracker\\track\\track-log\\192.168.56.1\\Admin\\{formatted_date}\\history', 'r', encoding='utf-8') as f:
        log_content = f.readlines()
    
    return render(request, 'tracker-log.html', {'log_content': log_content})

def call(request):
    return render(request, 'call.html')

def employee_screener(request):
    params = {'dataList': data}
    return render(request, 'employee-screener.html', params)

def tracking_ppt(request):
    return render(request, 'tracking-presentation.html')