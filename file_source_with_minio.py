#!/usr/bin/env python
# coding: utf-8

# In[8]:


pip install minio


# In[4]:


pip install pulsar-client minio


# In[4]:


from minio import Minio
from minio.error import S3Error

# Initialize Minio client with the complete endpoint URL
minio_client = Minio(
    "127.0.0.1:9000",  # Include the IP address and port in the URL
    access_key="5QXDQgNpRpaQGoZnIqTO",
    secret_key="6ciZe6CEapuhXloljqY8CtutN1Y1gd6zwRfscOKm",
    secure=False  # You can set it to True if you use HTTPS
)


# In[5]:


found = minio_client.bucket_exists("assignment1")
if not found:
    minio_client.make_bucket("assignment1")
else:
    print("Bucket 'assignment1' already exists")


# In[7]:


minio_client.fput_object("assignment1", "file_source.csv", "C:/Users/90545/Documents/Data engineering/Assignment 1/file_source.csv")

