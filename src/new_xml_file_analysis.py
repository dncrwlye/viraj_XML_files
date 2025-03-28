#wd: /Users/dancrowley/viraj_project/src

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io
import xml.etree.ElementTree as ET

#import sys #(when running interactively)
#sys.path.append('src')  # Add src folder to Python's search path


# Change to the project directory
os.chdir('/Users/dancrowley/viraj_project')
#project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#os.chdir(project_dir)

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Print current working directory to verify
print(os.getcwd())

from src.import_xml import parse_xml_file
from src.import_xml import extract_modelled_subgroups

# Importing Viraj new file 
if __name__ == "__main__":
    #xml_file_path = os.path.join(project_dir, "data", "WarpXML_Example.xml")
    xml_file_path = "/Users/dancrowley/viraj_project/data/WarpXML_Example.xml"
    root_element = parse_xml_file(xml_file_path)
    
    # Add your processing logic here
    if root_element is not None:
        # Example: Find all elements with a specific tag
        # elements = root_element.findall("./some_tag")
        # for element in elements:
        #     print(element.text)
        pass
# Usage (assuming xml_root is your already imported XML)
subgroups_df = extract_modelled_subgroups(root_element)
for child in root_element:
    print(child.tag)
root_element.get("GridLocationWeights")
dose_elem = root_element.find("Dose")
dose_text = dose_elem.text
print(dose_text)
dose_elem = root_element.find("Dose")
if dose_elem is not None and dose_elem.text:
    # Split the text by newlines and convert to numeric values
    values = [float(val) for val in dose_elem.text.strip().split('\n') if val.strip()]
    # Create a DataFrame with these values
    df = pd.DataFrame({'Dose': values})
    print(df)

