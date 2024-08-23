import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

# def query(filename):
#     with open(filename, "rb") as f:
#         data = f.read()
#     response = requests.post(API_URL, headers=headers, data=data)
#     return response.json()

# st.title("Text Generation from Image")

# file = st.file_uploader("Upload an image", type="jpg")

# if file is not None:

#     st.image(file, caption="Uploaded Image", use_column_width=True)
#     output = query(file.read())

#     st.write(output)

def query(file_content):
    response = requests.post(API_URL, headers=headers, data=file_content)
    return response.json()

st.title("Text Generation from Image!")

file = st.file_uploader("Upload an image", type="jpg")

if file is not None:
    st.image(file, caption="Uploaded Image", width=200)
    
    output = query(file.read())
    
    st.write("Generated Caption:")
    st.write(output[0]['generated_text'])

