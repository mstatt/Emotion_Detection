import os
import cv2
import datetime
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
from tensorflow import keras 
from streamlit import caching
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array

#//---------------------Special Vars-----------------------------------
#Change to False to disable image write
switch = True
#Change to False to disable log write
log_switch = True
#//--------------------------------------------------------------------
##
#//-----------------User Defined Functions-----------------------------

def write_report(log_switch,label):
    """
    Write to the .csv log
    """
    if log_switch == True:
        with open('camera-log.csv',mode ='a') as file:
                        file.write(str(label) +" , "+str(datetime.datetime.now())+ '\n')

#//--------------------------------------------------------------------
def render_report(log_switch):
    """
    Read the .csv and write the results to the page in a table
    """
    if log_switch == True:
        st.write('log_switch = '+str(log_switch))
        write_report(log_switch,"Emotion Detection has stopped")
        df = pd.read_csv ('camera-log.csv')
        df.columns = ['Emotion','Date and Time']
        df.sort_values(by=['Date and Time'], inplace=True, ascending=False)
        st.write(df)

#//--------------------------------------------------------------------
def write_Image(ctr,frame,label,label_position,switch):
    """
    Write the image with label to the corresponding directory
    """
    if switch:
        # If folder doesn't exist, then create it.
        CHECK_FOLDER = os.path.isdir(label)
        if not CHECK_FOLDER:
            os.makedirs(label)
        cv2.imwrite(label +'\\'+ str(ctr) +'.jpg', cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2))
#//--------------------------------------------------------------------



#Setting Title, Logo and favicon of the Application
logo = 'assets/falcons-logo2.png'
favicon = 'assets/favicon.ico'
st.set_page_config(page_title="Emotion Detection", page_icon = favicon)
image = Image.open(logo)
st.image(image, caption='Hospitality Emotion Detection by FALCON.AI', width = 350)
#Checkbox to turn off/on camera for detection
run = st.checkbox('Check to Run Emotion Detection')

#Font: Montserrat 
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            img {display: flex;
            justify-content: center;}
            code {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
#Set Frame window to camera
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
#Load emotion classification model
face_classifier = cv2.CascadeClassifier(r'assets/haarcascade_frontalface_default.xml')
classifier =load_model(r'assets/model.h5')
emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad','Surprise']
ctr = 0

while run: # While checkbox is checked
    _, frame1 = camera.read()
    frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #FRAME_WINDOW.image(frame)
    labels = []
    
    faces = face_classifier.detectMultiScale(gray)
    for (x,y,w,h) in faces:
            ctr = ctr + 1
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            roi_gray = gray[y:y+h,x:x+w]
            roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray])!=0:
                roi = roi_gray.astype('float')/255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi,axis=0)

                prediction = classifier.predict(roi)[0]
                label=emotion_labels[prediction.argmax()]
                label_position = (x,y)
                # Show analysis in window
                FRAME_WINDOW.image(cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2))

                if "Angry" in label: #Write only Angry
                    write_Image(ctr,frame,label,label_position,switch)
                    write_report(log_switch,label)
                elif "Sad" in label: #Write only Sad
                    write_Image(ctr,frame,label,label_position,switch)
                    write_report(log_switch,label)
                elif "Happy" in label: #Write only Happy
                    write_Image(ctr,frame,label,label_position,switch)
                    write_report(log_switch,label)

else:
    st.write('Emotion Detection has stopped')
    render_report(log_switch)
    if not log_switch:
        st.write('Logging is turned off')
