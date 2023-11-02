#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI
import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

app = FastAPI()

np.random.seed(0)
n = 1000  
max_users = 200  
pages = ['Home', 'Products', 'About', 'Contact', 'Blog', 'Services']

def generate_random_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def generate_page_error():
    return 1 if random.random() < 0.05 else 0

def generate_age():
    return random.randint(18, 70)

def generate_gender():
    return random.choice(['Male', 'Female'])

data = {
    'Timestamp': [datetime.now() - timedelta(minutes=random.randint(1, 60)) for _ in range(n)],
    'UserID': [str(random.randint(1, max_users)).zfill(4) for _ in range(n)],
    'IP': [generate_random_ip() for _ in range(n)],
    'Page': [random.choice(pages) for _ in range(n)],
    'Page_Error': [generate_page_error() for _ in range(n)],
    'Age': [generate_age() for _ in range(n)],
    'Gender': [generate_gender() for _ in range(n)],
}

@app.get("/generate_click_records")
async def generate_click_records():
    # Return the generated data
    return data

