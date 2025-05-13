Molecular Docking Workshop
By Peter Margaret, Msc Bioinformatics The University of Nairobi peter.margaret@students.uonbi.ac.ke


## Introduction:
- In this tutorial, we'll walk through a complete molecular docking experiment from scratch. We begin by installing the       necessary software. Mac users may face some installation challenges, but we’ll tackle them together. Let’s get started on   this computational adventure!
## Step 1: Install Required Tools
- Download and install the following software:
- AutoDock: https://autodock.scripps.edu/download-autodock4/
- MGLTools: https://ccsb.scripps.edu/mgltools/downloads/
- OpenBabel: https://sourceforge.net/projects/openbabel/
- PDBFixer: Install via Conda using conda install -c conda-forge pdbfixer
- Once downloaded, move all tools into a designated working directory.

## Install AutoDock and MGLTools:
- Run the MGLTools installer and follow the setup instructions.
- Confirm AutoDock is in your tools directory.

## Step 2: Prepare the Protein Structure
Download PDB File:
- Go to the RCSB Protein Data Bank and download the structure with PDB ID 4EY7, which is the Acetylcholinesterase enzyme      bound with Donepezil.
## Set Up Working Directory:
Create a folder named “Workshop” (e.g., on Desktop) and move the 4ey7.pdb file into this folder. Set this folder as the startup directory in AutoDockTools:
- Launch AutoDockTools > File > Preferences > Set > Paste path of the Workshop folder > Click Set.
- Load and Clean Protein in AutoDockTools:
- Go to File > Read Molecule > Select 4ey7.pdb.
- Expand the file tree and delete chains B, C, and D (Edit > Delete > Delete Selected Atoms).
- Remove water molecules (Edit > Delete Water).
- Delete heteroatoms like EDO605 (Edit > Delete > Delete Selected Atoms).
- Save the cleaned complex (File > Save > Write PDB) as "Clean_AChE_E20.pdb".
- Restart AutoDockTools for stability, then reopen the saved file.

## Hydrogen Addition and Charge Assignment:

- Remove the inhibitor (E20604) before adding hydrogens.
- Add polar hydrogens: Edit > Hydrogens > Add > Choose “Polar Only.”
- Assign charges: Edit > Charges > Add Kollman Charges.
- Check for non-integral charges: Edit > Charges > Check Totals on Residues.
- If residues have non-integral charges, click “Spread Charge Deficit over all atoms in residue.”

## Step 3: Prepare the Ligand
- Extract and Save Ligand:
- Open “Clean_AChE_E20.pdb” in a text editor.
- Copy all lines under HETATM corresponding to the inhibitor (e.g., atoms 8423–8450).
- Paste into a new file and save as “Ligand.pdb” in the Workshop folder.

## Process Ligand in AutoDockTools:

- Ligand > Input > Open > Select Ligand.pdb.
- AutoDockTools will assign charges automatically.
- Set rotatable bonds: Ligand > Torsion Tree > Choose Torsions > Done (for 6 rotatable bonds).
- Save the ligand as "Ligand.pdbqt": Ligand > Output > Save as PDBQT.

## Step 4: Define the Docking Grid
Select Macromolecule:

- Grid > Macromolecule > Choose > Select "Clean_AChE_E20" > Save as "Processed_AChE.pdbqt"
  Select Ligand:
- Grid > Set Map Types > Choose Ligand > Select "Ligand"

## Define Grid Box:

- Open Ligand.pdb in a text editor.
- Calculate centroid of ligand by averaging x, y, and z coordinates.
- Grid > Grid Box > Enter centroid values.
_Optionally adjust grid dimensions._
- File > Close saving current (in Grid Options dialog).
- Grid > Output > Save as “grid.gpf”

## Step 5: Run AutoGrid to Create Grid Maps
- Run > Run AutoGrid > Browse for autogrid4.exe and grid.gpf > Launch

## Step 6: Setup Final Docking Parameters
- Select Macromolecule and Ligand:
- Docking > Macromolecule > Set Rigid Filename > Choose “Processed_AChE.pdbqt”
- Docking > Ligand > Choose > Select “Ligand”
- Set Search Algorithm Parameters:
- Docking > Search Parameters > Genetic Algorithm > Accept Defaults
- Docking > Docking Parameters > Accept Defaults
- Save Docking Parameter File:
- Docking > Output > Lamarckian GA (4.2) > Save as “dock.dpf”

## Step 7: Execute Docking
- Run > Run AutoDock > Browse for autodock4.exe and dock.dpf > Launch

## Step 8: Analyze Results Load and View Docking Log:
- Analyze > Dockings > Open > Select dock.dlg
- Analyze > Macromolecule > Open > Choose "Processed_AChE.pdbqt"
- Analyze > Conformations > Play > Use controls to view different poses
- Enable “Show Info” and “Build H-bonds” options
- Export final complex: Click “Write Complex” > Save as “Complex.pdbqt”

## Convert to PDB Format:
- Open Babel GUI > Input format: pdbqt > Output format: pdb > Convert “Complex.pdbqt” to “Complex.pdb”
- or open using using ChimeraX and save .pdb file

- Repeat for all 10 conformations if needed
- Identify the best binding pose using lowest binding energy from dock.dlg

## Optional Visualization Tools:
- Maestro: https://www.schrodinger.com/freemaestro/
- UCSF Chimera: https://www.cgl.ucsf.edu/chimera/download.html
  
_There is no trophy in doing things the hard way_
_You have successfully accomplished your first CADD experiment!_
