import streamlit as st
import os
import google.generativeai as genai

# Configure API key
os.environ['GEMINI_API_KEY'] = 'AIzaSyDOXTszxFGafR7yjHbhvHqEjC7PuIH__xU'
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# Add custom CSS for background image
def add_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://www.itcinfotech.com/wp-content/uploads/2023/11/How-to-Maximize-Business-Productivity-with-Gen-AI.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Streamlit UI
background_image_url = "https://media-exp1.licdn.com/dms/image/C4D1BAQGzJlfg8R7IZA/company-background_10000/0/1584557830477?e=2147483647&v=beta&t=EB3arS55UlCQY5pft1Hd1c0SrJSKcrCuBnV8LkspQYc"  # Replace with your image URL
add_background_image(background_image_url)

# Streamlit App Title
st.title("GENAI: Text Content Generation🤖✨")
#st.sidebar.title("GENAI Project")

# Tab Selection
tab_choice = st.radio("Choose an operation", ["Answering Questions❓"])

# Text-to-Text Generation
if tab_choice == "Answering Questions❓":
    st.header("Answering questions: Given a question, the AI provides a detailed response❓🤖💬")
    user_input = st.text_area("Enter your prompt", placeholder="Type something like 'What is the meaning of life?'")
    model_option = st.selectbox("Select Model", [
        'models/gemini-1.5-pro-latest',
        'models/gemini-1.5-flash-latest'
    ])

    if st.button("Model Response"):
        if user_input:
            model = genai.GenerativeModel(model_option)
            response = model.generate_content(user_input)  # Pass the input as the 'text' parameter
            st.subheader("Generated Response :")
            st.write(response.text)
        else:
            st.error("Please enter a prompt!")
