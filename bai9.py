import streamlit as st

col1,col2,col3,col4,col5=st.columns(5)
col6,col7=st.columns([2,1])

with col1:
    b1=st.button("Cat")
with col2:
    b2=st.button("Dog")
with col3:
    b3=st.button("Pig")
with col4:
    b4=st.button("Cow")
with col5:
    b5=st.button("Chicken")   

if b1: #cat
    with col6:
        st.title("Cat")
        st.write("Sound")
        audio=open()
        st.audio(audio,format='audio/wav')

        st.write('Video')
        video=''
        st.video(video,format='video/mp4')
    with col7:
        imange=''
        st.image(image ,caption='Cat')

if b2: #dog
    with col6:
        st.title("Dog")
        st.write("Sound")
        audio=open()
        st.audio(audio,format='audio/wav')

        st.write('Video')
        video=''
        st.video(video,format='video/mp4')
    with col7:
        imange=''
        st.image(image ,caption='Cat')


if b3: #pig
    with col6:
        st.title("Pig")
        st.write("Sound")
        audio=open()
        st.audio(audio,format='audio/wav')

        st.write('Video')
        video=''
        st.video(video,format='video/mp4')
    with col7:
        imange=''
        st.image(image ,caption='Cat')


if b4: #cow
    with col6:
        st.title("Cow")
        st.write("Sound")
        audio=open()
        st.audio(audio,format='audio/wav')

        st.write('Video')
        video=''
        st.video(video,format='video/mp4')
    with col7:
        imange=''
        st.image(image ,caption='Cat')


if b5: #chicken
    with col6:
        st.title("Chicken")
        st.write("Sound")
        audio=open()
        st.audio(audio,format='audio/wav')

        st.write('Video')
        video=''
        st.video(video,format='video/mp4')
    with col7:
        imange=''
        st.image(image ,caption='Cat')







