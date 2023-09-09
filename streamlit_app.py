
import pandas as pd
import pickle
import streamlit as st
from PIL import Image

#loading the saved model
loaded_model=pickle.load(open('C:/Users/Dell/Desktop/datasets/New folder (2)/trained_model.sav','rb'))
loaded_file=pickle.load(open('C:/Users/Dell/Desktop/datasets/New folder (2)/object.sav','rb'))


#creating a fn for prediction

def netflix_engage_predict(data):

    pred = pd.DataFrame(data)
    pred['Subscription Plan'] = loaded_file[0].transform(pred['Subscription Plan'])
    pred['Genre Preference'] = loaded_file[1].transform(pred['Genre Preference'])
    pred['Frequency of Rating'] = loaded_file[2].transform(pred['Frequency of Rating'])
    new_pred = loaded_model.predict(loaded_file[3].transform(pred))
    if new_pred == 0:
        return 'Engagement level: Low'
    elif new_pred == 1:
        return 'Engagement level: Medium'
    else:
        return 'Engagement level: High'

def main():
    st.header('Know Your Netflix Engagement Level')

    # Adding image
    image_path = Image.open("C:/Users/Dell/Desktop/Netflix.jpg")
    st.image(image_path, use_column_width=True)
    st.write("Welcome to your Netflix engagement level analysis!")
    st.subheader('\nEnter Details:')

    #getting the input data

    # Dropdown for Subscription Plan
    subscription_options = ['select','Premium', 'Standard', 'Basic']
    a = st.selectbox('Subscription Plan', subscription_options)

    b = st.text_input('Monthly Revenue')
    c = st.text_input('Age')

    # Dropdown for Plan Duration
    plan_duration_options = ['select']+list(range(1, 13))
    d = st.selectbox('Plan Duration (Months)', plan_duration_options)

    e = st.text_input('Total Movies/Shows Watched')

    genre_options=['select','Comedy','Drama','Action','Thriller','Sci-Fi','Romance']
    f = st.selectbox('Genre Preference',genre_options)
    g = st.text_input('No. of Recommendations Viewed')
    h = st.text_input('% of Recommendations Acted Upon')

    rating_options=['select','Weekly','Monthly','Never']
    i = st.selectbox('Frequency of Rating',rating_options)
    j = st.text_input('Duration')

    data = {'Subscription Plan': [a], 'Monthly Revenue ($)': [b], 'Age': [c],
            'Plan Duration (Months)': [d],
            'Total Movies/Shows Watched': [e], 'Genre Preference': [f],
            'No. of Recommendations Viewed': [g], '% of Recommendations Acted Upon': [h],
            'Frequency of Rating': [i], 'Duration': [j]}


    output = ''

    if st.button('prediction'):

      output = netflix_engage_predict(data)

    st.success(output)

if __name__=='__main__':
    main()
