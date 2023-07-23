import streamlit as st
import PIL.Image as Image
st.set_page_config(page_title="SelfDrivingCar", page_icon="car")
def load_image(image_file):
    return Image.open(image_file)

def main():
    st.title("Autonomous Line-Following Robot Project")
    st.subheader("This is a project for the course Project System Design and Engineering")
    st.subheader("Collaborators:")
    st.subheader("Collaborators:")

    # Collaborator names with LinkedIn links
    collaborators = [
        {"name": "Daniel Tent", "linkedin": "https://www.linkedin.com/in/lalande-lucas-883413216/"},
        {"name": "Mahnaz Zarrinfar", "linkedin": "https://www.linkedin.com/in/mahnaz-zarrinfar-172873106/"},
        {"name": "Hlib Hryshko", "linkedin": "https://www.linkedin.com/in/hlib-hryshko-512107225/"}
    ]
    # Displaying collaborators' names with LinkedIn links
    for collaborator in collaborators:
        st.markdown(f"- [{collaborator['name']}]({collaborator['linkedin']})")
    st.image(load_image("images/selfDrivingCar.jpg"), width=300)
    with st.expander("Project Requirements"):
        st.markdown("""
         To build an autonomous line-following robot, it must have the following features:

    1. [x] **Autonomous Functionality:** The robot should be capable of autonomously navigating the track without human intervention.

    2. [x] **Operation Time:** The robot should operate continuously for at least 30 minutes on a single charge or power source.

    3. [x] **Compact Size:** The robot's design should ensure that it fits within a box with dimensions of 400mm x 250mm x 200mm.

    4. [x] **Line Following Capability:** The robot must be able to accurately follow a white line with a width of 20mm on the track.

    5. [x] **End-of-Track Detection:** The robot should be programmed to detect the end of the track and stop gracefully.

    6. [x] **Obstacle Avoidance:** The robot must have sensors or algorithms to detect and avoid obstacles in its path.

    7. [x] **Line Detection Mechanism:** The robot should be equipped with sensors or vision systems to detect the white line on the track.

    8. [x] **Modular Body Design:** The robot's body should be designed as separate 3D printed parts that can be assembled and disassembled easily.
    """)
    st.title("Demo Video")
    st.video("videos/SDC.mp4")
    st.download_button(
        label="Download Project Report",
        data=open("reports/SDC.pdf", "rb").read(),
        file_name="SelfDrivingCar.pdf",
        mime="application/pdf",
    )
if __name__ == "__main__":
    main()
