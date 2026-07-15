import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
st.title('FashionPulse_Customer Taste Analyzer')
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
creds = Credentials.from_service_account_file(r'credentials.json.json', scopes=scope)
client = gspread.authorize(creds)
sheet = client.open("FashionPulse_Data").sheet1

print("Connected Successfully")

Name = st.text_input('Enter your name:')
Age = st.number_input('Enter your age:')
Gender = st.selectbox('Select your gender:', ['Male', 'Female'])
City = st.text_input('Enter your city:')
Preference_Category = st.selectbox('Select your preferred clothing category:', ['shirts', 'jeans', 'abayas', 'kurtis', 'suits'])
Size = st.selectbox('Select your size:', ['S', 'M', 'L', 'XL', 'XXL'])
Style_Preference = st.selectbox('Select your style preference:', ['casual', 'formal', 'sporty'])
Color_Preference = st.selectbox('Select your color preference:', ['red', 'blue', 'black', 'white', 'green'])
Cloth_Type = st.selectbox('Select your preferred clothing type:', ['cotton', 'silk', 'denim', 'leather', 'linen'])
Budget_Range = st.selectbox('Select your budget range:', [' 1000 to 3000', '3000 to 5000'])
Needed = st.selectbox('Select the occasion when you need the clothing:', ['Urgently', 'weekly', 'monthly'])
st.write(f'Hello, {Name}! Welcome to FashionPulse.')
st.write(f'Your age is {Age} and your gender is {Gender}.')
st.write(f'You live in {City}.')
st.write(f'Your preferred clothing category is {Preference_Category}.')
st.write(f'Your size is {Size}.')
st.write(f'Your style preference is {Style_Preference}.')
st.write(f'Your color preference is {Color_Preference}.')
st.write(f'Your preferred clothing type is {Cloth_Type}.')
st.write(f'Your budget range is {Budget_Range}.')
st.write(f'The occasion when you need the clothing is {Needed}.')

if Name and Age and Gender and City and Preference_Category and Size and Style_Preference and Color_Preference and Cloth_Type and Budget_Range and Needed:
    sheet.append_row([
        Name,
        Age,
        Gender,
        City,
        Preference_Category,
        Size,
        Style_Preference,
        Color_Preference,
        Cloth_Type,
        Budget_Range,
        Needed
    ])
    st.success('Data saved successfully in Google Sheets ✅')
else:
    st.error("Please fill required fields")
    st.subheader('Saved Data:')