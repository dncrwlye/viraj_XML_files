
def read_pdb_file(pdb_file_path):
    """
    Read a PDB file and return the structure object.
    
    Parameters:
    pdb_file_path (str): Path to the PDB file
    
    Returns:
    Bio.PDB.Structure.Structure: Biopython Structure object containing the parsed PDB data
    """
    try:
        from Bio.PDB import PDBParser
        
        # Initialize parser
        parser = PDBParser(QUIET=True)
        
        # Get the file name without extension to use as structure ID
        import os
        structure_id = os.path.basename(pdb_file_path).split('.')[0]
        
        # Parse the PDB file
        structure = parser.get_structure(structure_id, pdb_file_path)
        
        print(f"Successfully read PDB file: {pdb_file_path}")
        print(f"Structure ID: {structure_id}")
        
        # Basic information about the structure
        model_count = len(list(structure.get_models()))
        chain_count = len(list(structure.get_chains()))
        residue_count = len(list(structure.get_residues()))
        atom_count = len(list(structure.get_atoms()))
        
        print(f"Models: {model_count}")
        print(f"Chains: {chain_count}")
        print(f"Residues: {residue_count}")
        print(f"Atoms: {atom_count}")
        
        return structure
    
    except ImportError:
        print("Biopython needs to be installed. Run: pip install biopython")
        return None
    except Exception as e:
        print(f"Error reading PDB file: {e}")
        return None
