import streamlit as st
import PIL.Image as Image
from scripts.spellcheck import listCheck
from scripts.geoLoc import get_longitude_latitude
def main():
    st.title("Rosen Internship")
    st.subheader("""This was a multidisciplinary project for the company Rosen. \n The goal was to evaluate the quality of the supply chain data, fix some data quality issues and finally create a dashboard to visualize the data. The project was done in collaboration with 3 other students.""")
    st.subheader("Collaborators:")


    # Collaborator names with LinkedIn links
    collaborators = [
        {"name": "Jelmer Eeftink", "linkedin": "https://www.linkedin.com/in/jelmer-eeftink-52a664179/"},
        {"name": "Saif Al-Salmi", "linkedin": ""},
        {"name": "Gijs Ophuis", "linkedin": "https://www.linkedin.com/in/gijs-ophuis-60bbb613b/"},
        
        ]
    for collaborator in collaborators:
        st.markdown(f"- [{collaborator['name']}]({collaborator['linkedin']})")
    with st.expander("SpellCheck Algorythm"):
        st.write('The Problem')
        st.image(Image.open("images/spellcheck.jpg"))
        

        st.subheader("Enter Management List:")
        management_list = st.text_area("Enter each word on a new line", "Greece\nNetherlands\nItaly\nGermany\norange")
        management_list = management_list.strip().split('\n')

        # User input for the data list
        st.subheader("Enter Data List:")
        data_list = st.text_area("Enter each word on a new line", "Greeece\nThe Netherlands\nNetherlandsas\nNeeetherkabds\nItalia\nGermany")
        data_list = data_list.strip().split('\n')

        # User input for cutoff_score
        cutoff_score = st.slider("Select Cutoff Score", min_value=0, max_value=100, value=50)

        if st.button("Run Spell Check"):
            result = listCheck(data_list, management_list, cutoff_score=cutoff_score)

            st.subheader("Results:")
            for item, confidence in result:
                st.write(f"Input: {item}, Corrected: {confidence}")
    with st.expander("Geolocation Api Call"):
        st.title("Address Geocoding")

        # Get the address from the user
        address = st.text_input("Enter the address:")

        if st.button("Geocode"):
            if address:
                latitude, longitude = get_longitude_latitude(address)
                if latitude is not None and longitude is not None:
                    st.success("Geocoding successful!")
                    st.write(f"Latitude: {latitude}")
                    st.write(f"Longitude: {longitude}")
                    st.markdown(f"[Google Maps Location](https://www.google.com/maps/search/{latitude},{longitude})")
                else:
                    st.error("Geocoding failed. Please check the address.")      
            else:
                st.warning("Please enter an address to geocode.")
    with st.expander("Supply Chain DashBoard"):
        st.title("Supply Chain DashBoard")
        st.video("videos/SCD.mp4")
        st.markdown(f"[Supply Chain DashBoard](https://github.com/SteDiamant/SupplyChainDashboard)")


if __name__ == "__main__":
    main()