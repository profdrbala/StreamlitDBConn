import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

# Streamlit App
def main():
    st.title("Streamlit Firebase Example")
    
    # Example: Display data from Firebase
    st.subheader("Data from Firebase")
    #collection_name = "Books"  # Replace with your Firestore collection name

    # Query Firestore
    #docs = db.collection(collection_name).limit(10).get()

    # Display documents
    #for doc in docs:
    #    st.write(doc.id, doc.to_dict())

    # Create a reference to the Google post.
    doc_ref = db.collection("Books").document("1")

    # Then get the data at that reference.
    doc = doc_ref.get()

    # Let's see what we got!
    st.write("The id is: ", doc.id)
    st.write("The contents are: ", doc.to_dict())


if __name__ == '__main__':
    main()
