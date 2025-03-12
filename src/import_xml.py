#viraj code

import pandas as pd
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt

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


def create_ramachandran_plot(phi_values, psi_values, title="Ramachandran Plot"):
    """
    Create a Ramachandran plot from phi and psi angles.
    
    Args:
        phi_values: List/array of phi angles in degrees
        psi_values: List/array of psi angles in degrees
        title: Title for the plot
    """
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot the points
    scatter = ax.scatter(phi_values, psi_values, alpha=0.7, s=10)
    
    # Set plot limits for phi and psi angles (-180 to 180 degrees)
    ax.set_xlim(-180, 180)
    ax.set_ylim(-180, 180)
    
    # Add grid lines at 30-degree intervals
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Add lines at x=0 and y=0
    ax.axhline(y=0, color='black', linestyle='-', alpha=0.5)
    ax.axvline(x=0, color='black', linestyle='-', alpha=0.5)
    
    # Label the axes and add title
    ax.set_xlabel('Phi (φ) Angle (degrees)', fontsize=12)
    ax.set_ylabel('Psi (ψ) Angle (degrees)', fontsize=12)
    ax.set_title(title, fontsize=14)
    
    # Add marks at key regions (optional)
    # Alpha-helix region
    ax.add_patch(plt.Rectangle((-80, -60), 40, 40, fill=False, edgecolor='red', 
                              linestyle='--', label='Alpha-helix'))
    # Beta-sheet region
    ax.add_patch(plt.Rectangle((-180, 100), 70, 80, fill=False, edgecolor='blue', 
                              linestyle='--', label='Beta-sheet'))
    
    # Add legend
    ax.legend()
    
    return fig, ax

# Example: If you already have phi and psi values from your XML
# Assuming they're in your DataFrame as 'phi' and 'psi' columns
# df = pd.DataFrame({'phi': phi_data, 'psi': psi_data})

# To test with random data if you don't have actual values yet:
def generate_test_data(n=1000):
    # Generate clustered data to mimic real Ramachandran distributions
    # Alpha-helix cluster
    alpha_n = int(n * 0.4)
    alpha_phi = np.random.normal(-60, 10, alpha_n)
    alpha_psi = np.random.normal(-45, 10, alpha_n)
    
    # Beta-sheet cluster
    beta_n = int(n * 0.3)
    beta_phi = np.random.normal(-120, 20, beta_n)
    beta_psi = np.random.normal(130, 20, beta_n)
    
    # Random points for the rest
    rest_n = n - alpha_n - beta_n
    rest_phi = np.random.uniform(-180, 180, rest_n)
    rest_psi = np.random.uniform(-180, 180, rest_n)
    
    # Combine all data
    phi = np.concatenate([alpha_phi, beta_phi, rest_phi])
    psi = np.concatenate([alpha_psi, beta_psi, rest_psi])
    
    return phi, psi