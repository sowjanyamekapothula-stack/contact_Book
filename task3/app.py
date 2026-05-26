import streamlit as st

# -------------------- CUSTOM CSS --------------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: black;
    color: white;
}

/* Title */
h1 {
    color: #00ff99;
    text-align: center;
    font-family: Verdana;
    font-size: 40px;
}

/* Subheadings */
h2, h3 {
    color: cyan;
    font-family: Arial;
}

/* Input fields */
.stTextInput input,
.stTextArea textarea {
    background-color: #1e1e1e;
    color: white;
    border-radius: 10px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111111;
}

/* Buttons */
.stButton button {
    background-color: #00c853;
    color: white;
    border-radius: 10px;
    font-size: 16px;
    width: 100%;
}

/* Contact cards */
.contact-box {
    background-color: #1e1e1e;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# -------------------- TITLE --------------------

st.title("📒 Contact Book Management System")

# -------------------- SESSION STORAGE --------------------

if "contacts" not in st.session_state:
    st.session_state.contacts = {}

# -------------------- SIDEBAR MENU --------------------

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Add Contact",
        "View Contacts",
        "Search Contact",
        "Update Contact",
        "Delete Contact"
    ]
)

# -------------------- ADD CONTACT --------------------

if menu == "Add Contact":

    st.subheader("➕ Add New Contact")

    name = st.text_input("Enter Name")
    phone = st.text_input("Enter Phone Number")
    email = st.text_input("Enter Email")
    address = st.text_area("Enter Address")

    if st.button("Save Contact"):

        st.session_state.contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        st.success("✅ Contact added successfully!")

# -------------------- VIEW CONTACTS --------------------

elif menu == "View Contacts":

    st.subheader("📋 Saved Contacts")

    if len(st.session_state.contacts) == 0:
        st.warning("No contacts available.")

    else:

        for name, details in st.session_state.contacts.items():

            st.markdown(f"""
            <div class="contact-box">
                <h3>{name}</h3>
                <p>📞 {details['Phone']}</p>
                <p>📧 {details['Email']}</p>
                <p>🏠 {details['Address']}</p>
            </div>
            """, unsafe_allow_html=True)

# -------------------- SEARCH CONTACT --------------------

elif menu == "Search Contact":

    st.subheader("🔍 Search Contact")

    search = st.text_input("Enter Name")

    if st.button("Search"):

        if search in st.session_state.contacts:

            details = st.session_state.contacts[search]

            st.success("✅ Contact Found!")

            st.markdown(f"""
            <div class="contact-box">
                <h3>{search}</h3>
                <p>📞 {details['Phone']}</p>
                <p>📧 {details['Email']}</p>
                <p>🏠 {details['Address']}</p>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.error("❌ Contact not found.")

# -------------------- UPDATE CONTACT --------------------

elif menu == "Update Contact":

    st.subheader("✏️ Update Contact")

    update = st.text_input("Enter Contact Name")

    if update in st.session_state.contacts:

        phone = st.text_input("New Phone Number")
        email = st.text_input("New Email")
        address = st.text_area("New Address")

        if st.button("Update Contact"):

            st.session_state.contacts[update] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }

            st.success("✅ Contact updated successfully!")

    elif update != "":
        st.error("❌ Contact not found.")

# -------------------- DELETE CONTACT --------------------

elif menu == "Delete Contact":

    st.subheader("🗑️ Delete Contact")

    delete = st.text_input("Enter Contact Name")

    if st.button("Delete Contact"):

        if delete in st.session_state.contacts:

            del st.session_state.contacts[delete]

            st.success("✅ Contact deleted successfully!")

        else:
            st.error("❌ Contact not found.")