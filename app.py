import re
import streamlit as st 

# This is page design
st.set_page_config(page_title="Password Strength By Jawad Unar ",
                   page_icon="🔑",
                   layout="centered")

# Styling for CSS

st.markdown("""
<style>
  .main{text-align:center;} /* Center align text*/
            .stTextInput{:70% ! important:
            margin:auto;} /*Center password input/*
            .stButton{text-align:center;} /*Center button/*
            .stButton button {width :60 %;
    background-color:blue;blue;color:white;
            font-size:20px;border-redius:6px;}
            .stButton button:hover
    {background-color:purplegreen;color:white}
            
</style>
""", unsafe_allow_html=True
)

# Page title and description
st.title("🔐 Passward Strength Generation")
st.write("Enter your password below to check its security level.🚀")

# Password input field
password = st.text_input("Enter your password:", type="password")

# Function to check password 
def check_password_strength(password):
        score = 0 # intial password strength score
        feedback = [] # List to store feedback message 
        # Ceck password length

        if len(password) >= 7:
                score += 1 # Increase score if password is at least 7 characters
        else:
                feedback.append("❌Password should be at least 7 characters long.")

        # Check uppercase and lowercase letters.
        if re.search(r"[A-Z]", password):
                score += 1
        else:
                feedback.append("❌Password should contain at least one uppercase letter.")

        # Check lowercase letters.
        if re.search(r"[a-z]", password):
                score += 1
        else:
                feedback.append("❌Password should contain at least one lowercase letter.")

        # Check digits.
        if re.search(r"[0-9]", password):
                score += 1
        else:
                feedback.append("❌Password should contain at least one digit.")

        # Check special characters.
        if re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\]", password):
                score += 1
        else:
                feedback.append("❌Password should contain at least one special character.")

        # Display password strength message


        if score ==3:
                st.info("🚸 *Moderate Password* -Consider  improving security by adding more features")
        elif score ==4 :
                st.success("✅ *Strong password* - your passwordis secure")
        else:
                st.error("❌ * Weak Password* -Follow the suggestion below to strength it")
        # Feedback Suggestion 

        if feedback:
                with st.expander("🏐 * Improve uor Password "):
                        for item in feedback:
                                st.write(item)
  # Password Input Field 
        password= st.text_input("Enter your password:",type="password",help="Ensure your Password is Strong 🔓")

# Button to Check Password Strength
        if st.button("Check Strength"):
                if password:
                        check_password_strength(password) # Call Function to check strength 

        st.warning("⚠ Please Enter a Password first") #