#viraj code

import pandas as pd
import xml.etree.ElementTree as ET

def parse_xml_file(file_path):
    """
    Parse an XML file and return the root element.
    
    Args:
        file_path (str): Path to the XML file
        
    Returns:
        xml.etree.ElementTree.Element: Root element of the XML tree
    """
    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        
        # Get the root element
        root = tree.getroot()
        
        print(f"Successfully parsed XML file: {file_path}")
        print(f"Root tag: {root.tag}")
        
        # Example of accessing elements
        print("\nExamples of accessing data:")
        
        # Print first-level child elements
        print("First-level elements:")
        for child in root:
            print(f"- {child.tag}")
        
        return root
        
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return None
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


def extract_modelled_subgroups(xml_root):
    """
    Extract ModelledSubgroup elements from an already parsed XML tree into a DataFrame.
    
    Args:
        xml_root: The root element of the already parsed XML
        
    Returns:
        pandas.DataFrame: DataFrame containing the ModelledSubgroup data
    """
    # Find all ModelledSubgroup elements
    subgroups = xml_root.findall(".//ModelledSubgroup")
    
    if not subgroups:
        print("No ModelledSubgroup elements found in the XML.")
        return None
    
    print(f"Found {len(subgroups)} ModelledSubgroup elements.")
    
    # Extract all attributes into a list of dictionaries
    data = []
    for subgroup in subgroups:
        data.append(subgroup.attrib)
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    print(f"DataFrame created with shape: {df.shape}")
    
    return df
