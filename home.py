import streamlit as st
import PIL.Image as Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
st.set_page_config(
    page_title="MainPage",
    page_icon="👋",
    
)

def load_image(image_file):
    return Image.open(image_file)

def main():
    st.title("Personal Information")
    st.subheader("Name: Stelios")
    st.subheader("Surname: Diamantopoulos")
    st.subheader("Age: 28")
    c1,c2 = st.columns(2)
    with c1:
        st.markdown("""
                    $1.01^{365}=37.8$ \n
                    $0.99^{365}=0.03$
                    """)
    with c2:
        st.markdown("""
        "Small Consistent Effort \n
        Lead to Great Results"
        """)
    st.image(load_image("images/profile.png"), width=300)
    st.download_button(
        label="Download CV",
        data=open("reports/Resume___CV.pdf", "rb").read(),
        file_name="StylianosDiamantopoulosCV.pdf"
    )

    st.markdown("""Hey there, I'm Stelios Diamantopoulos, an electrical and electronic engineering student at Saxion University of Applied Science. But that's not all! I'm also into data analytics and business, with a Minor in Business and Data Analytics. Recently, I had an amazing time at Berkeley University too!

Before all this, I studied physics at the University of Thessaloniki. Beyond academics, I've had hands-on experiences with supply chain data, hardware setups, and more.

I'm super pumped about the future, where engineering, data, and business collide! Let's rock this journey together and make a splash in the world! 🚀😄""")
    
    st.title("Sent Me an Email")
    EMAIL_ADDRESS = "testemail@gmail.com"#@ NEED TO BE INTEGRATED PROPERLY
    EMAIL_PASSWORD = 'test123'#@ NEED TO BE INTEGRATED PROPERLY
    # Email form inputs
    recipient_email = st.text_input("Recipient Email", "")
    subject = st.text_input("Subject", "")
    message = st.text_area("Message", "")

    # Send button
    if st.button("Send Email"):
        if not recipient_email or not subject or not message:
            st.error("Please fill in all fields.")
        else:
            try:
                # Connect to the email server
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()

                # Login to the email account
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

                # Create the email message
                msg = MIMEMultipart()
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = recipient_email
                msg['Subject'] = subject
                msg.attach(MIMEText(message, 'plain'))

                # Send the email
                server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())

                # Close the server connection
                server.quit()

                st.success(f"Email sent successfully to {recipient_email}!")
            except Exception as e:
                st.error(f"An error occurred while sending the email: {e}")
if __name__ == "__main__":
    main()