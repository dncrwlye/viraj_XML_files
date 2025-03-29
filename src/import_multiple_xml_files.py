import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io
import xml.etree.ElementTree as ET
import sys #(when running interactively)
from pathlib import Path

# Get the absolute path to the project root directory
# This works regardless of where the script is located within the project
project_root = Path(__file__).resolve().parent.parent
# get the project directory
# Add project root to Python's path if it's not already there
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Now this should work for anyone, anywhere
from src.import_xml import parse_xml_file 
from src.import_xml import extract_modelled_subgroups
from src.import_xml import pull_angle
from src.import_xml import pull_dose

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#print(project_dir)
# Print current working directory to verify

new_xml_folder_path = os.path.join(project_dir, "data", "All_XML_FILES")

print(new_xml_folder_path)

file_list = os.listdir(new_xml_folder_path)

print("Files in folder:")
#for file in file_list:
    #print(file)

#first, try this for the just entry in file_list
dat_dose = pull_dose(xml_file_name = file_list[1], xml_file_path =new_xml_folder_path)
dat_angle = pull_angle(xml_file_name = file_list[1], xml_file_path =new_xml_folder_path)

if dat_dose is not None:  # Always good to check that the function returned data
    print("First 5 entries of the DataFrame:")
    print(dat_dose.head())
else:
    print("No data was returned from pull_dose")

if dat_angle is not None:  # Always good to check that the function returned data
    print("First 5 entries of the DataFrame:")
    print(dat_angle.head())
else:
    print("No data was returned from pull_angle")


#now let'd do this for all the datasets 
# Initialize empty DataFrames to store all results
all_dose_data = pd.DataFrame()
all_angle_data = pd.DataFrame()

for file in file_list:
    print(file)
    dat_dose = pull_dose(xml_file_name = file, xml_file_path =new_xml_folder_path)
    dat_angle = pull_angle(xml_file_name = file, xml_file_path =new_xml_folder_path)

    if dat_dose is not None:  # Always good to check that the function returned data
        print("First 5 entries of the DataFrame:")
        print(dat_dose.head())
        # Concatenate to the combined dataframe
        all_dose_data = pd.concat([all_dose_data, dat_dose], ignore_index=True)
    else:
        print(file, "No data was returned from pull_dose")

    if dat_angle is not None:  # Always good to check that the function returned data
        print("First 5 entries of the DataFrame:")
        print(dat_angle.head())
        # Concatenate to the combined dataframe
        all_angle_data = pd.concat([all_angle_data, dat_angle], ignore_index=True)
    else:
        print(file, "No data was returned from pull_angle")

    dat_dose

dat_dose.head()
dat_angle.head()