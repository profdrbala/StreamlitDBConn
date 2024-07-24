import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
#cred = credentials.Certificate('firebase-key.json')
app = firebase_admin.initialize_app(credentials.Certificate('firebase-key.json'), name='DB_Conn')
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

    # Then get the data at that reference.
    doc = doc_ref.get()

    # Let's see what we got!
    st.write("The id is: ", doc.id)
    st.write("The contents are: ", doc.to_dict())

    title = st.text_input("Enter Title:")
    isbn = st.number_input("Enter ISBN:")
    author = st.number_input("Enter author:")
    publisher = st.number_input("Enter publisher:")
    country = st.number_input("Enter countyr:")
    price = st.number_input("Enter price:")
    
    if st.button("Add Data"):
        # Add data to Firestore
        data = {
            'title': name,
            'isbn': isbn,
            'author':author,
            'pubisher':publisher,
            'country':country,
            'price':price
        }
        db.collection("Books").add(data)
        st.success("Data added successfully!")
        


if __name__ == '__main__':
    main()
