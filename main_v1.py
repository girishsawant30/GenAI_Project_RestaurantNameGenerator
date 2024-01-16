import streamlit as st
import Langchain_helper

# Set a background image URL
background_image_url = "https://www.wallpaperup.com/uploads/wallpapers/2014/11/09/511936/0ba8d8f9ae54e55ade549ba9dc92f38c.jpg"

# Create a custom HTML template
custom_html = f"""
    <style>
        body {{
            background-image: url('{background_image_url}');
            background-size: cover;
        }}
    </style>
"""

# Set the Streamlit app to use the custom HTML template
st.markdown(custom_html, unsafe_allow_html=True)
# Streamlit app content starts here
st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

if cuisine:
    response = Langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)
