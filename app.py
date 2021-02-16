import streamlit as st

st.title('Streamlit Crash Course')
st.header('Puppy marii is the cutest')
st.subheader('This is a sub-header')
st.text('This is so cool')
st.markdown('# This is markdown')
st.markdown('[Google](https://google.com)')

url_link = "https://www.zomato.com/bangalore"
st.markdown(url_link)

html_page = """
        <div style="background-color:tomato;padding:30px">
            <p style="font-size:30px">Puppy is awesome</p>
        </div>

 """
st.markdown(html_page,unsafe_allow_html=True)

#image
from PIL import Image
img = Image.open("example.jpeg")
st.image(img,width=300,caption="Streamlit Image")

#audio
audio_file = open('example.mp3',"rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes,format="audio/mp3")

#video
video_file = open("example.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)



# st.success('Yipee!!')
# st.info("Information")
# st.warning("This is a warning")
# st.error("This is an error")

# st.exception('NameError()')


# Video URL/YTB
# st.video("https://www.youtube.com/watch?v=_9WiB2PDO7k")


# WIDGET
st.button("Submit")

if st.button("Play"):
	st.text("Hello world")

# Checkbox
if st.checkbox("Show/hide"):
	st.success("Hiding or Showing")

# Radio
gender = st.radio("Your Gender",["Male","Female"])

if gender == 'Male':
	st.info("Is a male")

# Select
location = st.selectbox("Your Location",["UK","USA","India","Accra"])

# Multiselect
occupation = st.multiselect("Your Occupation",["Developer","Doctor","BusinessMan","Banker"])

# TEXT INPUT
name = st.text_input("Your Name","Type Here")
st.text(name)

# NUMBER INPUT
age = st.number_input("Age",5,100)

# TEXT_AREA
message = st.text_area("Your Message","Type here")

# SLider
level = st.slider("Your Level",2,6)

# Balloons
st.balloons()

#DATAFRAME
import pandas as pd 
df = pd.read_csv("iris.csv")

#M1
st.dataframe(df.head())
# #M2
# st.write(df.head())

# TABLES
st.table(df.head())

# Plot Pkgs
import matplotlib.pyplot as plt 
import seaborn as sns 

# Area_chart
st.area_chart(df.head(20))

# Bar_chart
st.bar_chart(df.head(20))

# Line Chart
st.line_chart(df)


# Display JSON,CODE
data = {"name":"John","salar":50000}
st.json(data)


