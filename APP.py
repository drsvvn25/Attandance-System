import firebase_admin
from firebase_admin import credentials, db
import streamlit as st

# Initialize Firebase app
cred = credentials.Certificate("serviceAccountKey.json") # replace with your service account key
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://attendance-c065c-default-rtdb.firebaseio.com/'
})

# Function to retrieve data from Firebase
def get_data_from_firebase():
    ref = db.reference('Students/') # replace with your data path
    return ref.get()

# Main Streamlit app
def main():
    st.title('Firebase Data Viewer')

    # Retrieve data from Firebase
    data = get_data_from_firebase()

    # Display data in a table
    if data:
        st.write("### Students Data:")
        st.write("| Key | Name | Present |")
        st.write("| --- | ---- | ------- |")
        for key, value in data.items():
            name = value.get('name', 'N/A')
            total_attendance = value.get('total_attendance', 'N/A')
            st.write(f"| {key} | {name} | {total_attendance} |")
    else:
        st.write("No data available.")

if __name__ == "__main__":
    main()
