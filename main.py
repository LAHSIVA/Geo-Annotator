import streamlit as st
import subprocess
import sys

# Specify the Python executable path
PYTHON_PATH = sys.executable

# Define paths to scripts
getmap_script = "F:\CG PACKAGE\Getcornerpoints\Getmap.py"
getpolygon_script = "F:\CG PACKAGE\Getcountrypolygon\Getcountries.py"
getcountry_script = "F:\CG PACKAGE\Countryname\Countryname.py"

# Function to run a script and capture output
def run_script(script_path):
    process = subprocess.Popen([PYTHON_PATH, script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()

# Function to stop a running process
def stop_process(process):
    if process and process.poll() is None:
        process.terminate()
        return True
    return False

# Streamlit app
def main():
    st.title("Interactive Mapping and Region Annotation")
    st.write("This application allows you to interactively mark points on a map or image, define custom polygons for regions of interest, and dynamically annotate regions using hand gestures.")

    # Sidebar menu to select the operation
    operation = st.sidebar.selectbox("Select Operation", ["Get Map", "Get Country Polygon", "Get Polygon"])

    process = None  # Initialize subprocess variable

    # Execute the selected operation
    if operation == "Get Map":
        st.write("Use this option to mark points on a map or image.")
        if st.button("Run Get Map"):
            process = subprocess.Popen([PYTHON_PATH, getmap_script])
        if st.button("Stop Get Map"):
            if stop_process(process):
                st.success("getmap.py stopped.")
            else:
                st.warning("No process running.")
    elif operation == "Get Country Polygon":
        st.write("Use this option to define custom polygons for countries or regions.")
        if st.button("Run Get Country Polygon"):
            process = subprocess.Popen([PYTHON_PATH, getpolygon_script])
        if st.button("Stop Get Country Polygon"):
            if stop_process(process):
                st.success("getpolygon.py stopped.")
            else:
                st.warning("No process running.")
    elif operation == "Get Polygon":
        st.write("Use this option for real-time hand tracking and dynamic region annotation.")
        if st.button("Run Get Polygon"):
            process = subprocess.Popen([PYTHON_PATH, getcountry_script])
        if st.button("Stop Get Polygon"):
            if stop_process(process):
                st.success("getcountry.py stopped.")
            else:
                st.warning("No process running.")

if __name__ == "__main__":
    main()
