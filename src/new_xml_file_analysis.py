#wd: /Users/dancrowley/viraj_project/src

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Change to the project directory
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
os.chdir(project_dir)

# Print current working directory to verify
print(os.getcwd())

from import_xml import parse_xml_file
from import_xml import extract_modelled_subgroups


# Importing Viraj new file 
if __name__ == "__main__":
    xml_file_path = os.path.join(project_dir, "data", "WarpXML_Example.xml")
    #xml_file_path = "/Users/dancrowley/viraj_project/data/WarpXML_Example.xml"  # Replace with your XML file path
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