import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time

import os
import pandas as pd


# Initialize Firebase Admin SDK
#cred = credentials.Certificate('firebase-key.json')
app = firebase_admin.initialize_app(credentials.Certificate('firebase-key.json'), name=f"Books{int(time.time())}")
#firebase_admin.initialize_app(cred)

# Get a Firestore client
#db = firestore.client()
db = firestore.client(app=app)

# Streamlit App
def main():
    st.title("Streamlit Firebase Example")

    st.subheader("Data from Firebase")
    #collection_name = "Books"  # Replace with your Firestore collection name

    # Query Firestore
    #docs = db.collection(collection_name).limit(10).get()

    # Display documents
    #for doc in docs:
    #    st.write(doc.id, doc.to_dict())

    # Create a reference to the Google post.
    doc_ref = db.collection("Books").document("1")

    #get the data from UX
    title = st.text_input("Enter Title:")
    isbn = st.text_input("Enter ISBN:")
    author = st.text_input("Enter author:")
    publisher = st.text_input("Enter publisher:")
    country = st.text_input("Enter countyr:")
    price = st.number_input("Enter price:")
    
    if st.button("Add Books"):
        # Add data to Firestore
        data = {
            'title': title,
            'isbn': isbn,
            'author': author,
            'pubisher': publisher,
            'country': country,
            'price': price
        }
        db.collection("Books").add(data)
        st.success("Data added successfully!")


    # Then get the data at that reference.
    doc = doc_ref.get()

    # Let's see what we got!
    #st.write("The id is: ", doc.id)
    #st.write("The contents are: ", doc.to_dict())
    # Display documents
    if st.button("Get Books"):
        users_ref = db.collection('Books')
        docs = users_ref.stream()
    
        data = []
        for doc in docs:
            data.append(doc.to_dict())

        if data:
            df = pd.DataFrame(data)
            #st.table(df)
            df = df[['title', 'isbn','author','pubisher','country','price']] 
            #st.dataframe(df)
            st.write(df)
        else:
            st.write("No data found")
            


if __name__ == '__main__':
    main()
