import streamlit as st


st.title("Visual Inspection Machine Learning On MEMs Devices")
st.subheader("""
This Project is a part of Smart Solution Semester as Saxion University of Applied Science in collaboration with the nanotechnology lectorate.
1. **Goal**: Develop a Machine Learning Model
   - The primary objective of the project is to build a machine learning model.

2. **Task**: Classify Defects in MEMs Devices
   - Optimize the existing process of data generation find the best set of parameters for the training process.

""")
st.image("images/ml.png")
st.markdown("""List of Parameters:
- **vertices**: 10
    - Range: 3 to 20 (Assumed to be a discrete value between 3 and 20)
- **angle_variance**: 10
    - Range: 5 to 20 (Assumed to be a discrete value between 5 and 20)
- **size_mean**: 4
    - Range: Not provided (Assumed to be a continuous value)
- **size_stddev**: 3
    - Range: Not provided (Assumed to be a continuous value)
- **curviness**: 10
    - Range: 1 to 15 (Assumed to be a discrete value between 1 and 15)
- **mu_amount**: 10
    - Range: 1 to 20 (Assumed to be a discrete value between 1 and 20)
- **std_amount**: 4
    - Range: 1 to 10 (Assumed to be a discrete value between 1 and 10)
- **size_std**: 3
    - Range: 1.0 to 5.0 (Assumed to be a continuous value between 1.0 and 5.0)
- **opacity**: 0.9
    - Range: 0.0 to 1.0 (Assumed to be within the inclusive range)
""")
c1,c2,c3=st.columns(3)
with c1:
    st.image("images/11.jpg",caption="Image 1")
    
    st.image("images/1.png",caption="Image 1 Evaluation")
with c2:
    st.image("images/22.jpg",caption="Image 2")
    st.image("images/2.png",caption="Image 2 Evaluation")
with c3:
    st.image("images/33.jpg",caption="Image 3")
    st.image("images/3.png",caption="Image 3 Evaluation")