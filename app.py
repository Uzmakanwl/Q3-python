import streamlit as st
st.set_page_config(page_title =" Growth Mindset project", page_icon="★")
st.title("Welcome to Growth Mindset Project")


st.header ("Welcome to your Growth Journey!" )
st.write("Embrace challenges,learn form mistakes, and unlock your full potential.This AI-powered app helps you build a Growth mindset with reflaction ,challenges and achievements!  ") 

# quote section

st.header(" Today's Growth mindset Quote🌺 ")
st.write ("✨Success is not final , failer is not fatal: it is the courage to continue that counts. -winston churchill")


st.header("💪What's Your Challange Today? ")
user_input = st.text_input("Discribe a Challange you're facing ")

# condition

if user_input:
    st.success(f" you're facing:{user_input} . Keep pushing forward your goal!")

else:  
    st.warning("Tell us about your chllange to get started!")


# reflexing

st.header("🌺Reflect on your Learning ")
reflection = st.text_area ("Write your reflection here: ")

if reflection:
    st.success (f" Great Insight !Your reflection:{reflection}")

else :
   st.info ("Reflecting on past experiance  help you grow ! Share your difficulties")    



# acheivement
st.header ("Celebrate Your Wins!")
acheivement = st.text_input ("Share something you've recently accomplished:")

if acheivement:
    st.success(f" Amazing! You  achieved:{acheivement}")

else:    
    st.info ("Big or small ,acheivement counts! Share on now ")

# footer 

st.write("- - -")
st.write("Keep beleivng in yourself . Growth is a journey , not a destination! ")
st.write("Created by Uzma Kanwal") 

