import streamlit as st
import PIL.Image as Image
st.set_page_config(page_title="Wireless Power Transfer", page_icon="power")
def load_image(image_file):
    return Image.open(image_file)

def main():
    st.title("Wireless Power Transfer")
    st.subheader("This is a project for the course Project Simulation and Realization")
    st.subheader("Collaborators:")


    # Collaborator names with LinkedIn links
    collaborators = [
        {"name": "Daniel Tent", "linkedin": "https://www.linkedin.com/in/lalande-lucas-883413216/"},
        {"name": "Mahnaz Zarrinfar", "linkedin": "https://www.linkedin.com/in/mahnaz-zarrinfar-172873106/"},
        {"name": "Max Walker", "linkedin": ""},
        {"name": "IJeoma J. Oduche","linkedin":"https://www.linkedin.com/in/jennifrancess-o-05b857227/"}
]

    # Displaying collaborators' names with LinkedIn links
    for collaborator in collaborators:
        st.markdown(f"- [{collaborator['name']}]({collaborator['linkedin']})")
    st.image(load_image("images/selfDrivingCar.jpg"), width=300)
    with st.expander("Project Requirements"):
        st.markdown("""
         ## Project Requirements

**Must Have**
- [x] Reliable connection
- [x] Completion to required timeframe
- [x] Output 12V to autonomous car
- [x] Clear modularity (for rail extension)

**Should Have**
- [x] Adhere to normal EMC standards
- [x] Clean & efficient PCB design
- [x] Within a cost of €75
- [x] Allow extension of the planar area

**Could Have**
- [ ] Power statistic data (for efficiency etc)
- [ ] Output status/statistics

    """)
    st.title("Demo Video")
    st.video("videos/WPT.mp4")
    st.download_button(
        label="Download Project Report",
        data=open("reports/WPT.pdf", "rb").read(),
        file_name="WirelessPowerTransfer.pdf",
        mime="application/pdf",
        key='wireless_power_transfer')
if __name__ == "__main__":
    main()
