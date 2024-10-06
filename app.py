import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key = st.secrets["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(input,image):
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text


st.set_page_config(
    page_title="VisionIQ",
    page_icon="App Icon.png")
st.header("VisionIQ")
st.markdown("""
The app functions as a visual question answering system. 
It takes an image as input, processes it to extract relevant information, 
and then uses Google Gemini's advanced language model to provide informative responses based on the visual content and your query.
""")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
input=st.text_input("Input Prompt (optional): ",key="input")


submit=st.button("Generate Image Insights!")

if submit or input:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)

st.markdown("""
---

*Built by Mukund Tiwari*

[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/Mtiwari27/VisionIQ)
""")
