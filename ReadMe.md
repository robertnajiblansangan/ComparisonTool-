To Install Dependencies:
1. Make sure you already have Python and Pip Installed to your Machine
2. Open CMD
3. Type: `pip install -r requirements.txt`
4. Hit Enter to install required dependencies
5. Type `setx PYTHONPATH  "%cd%" /m` NOTE: you should be on the directory where this project stored. 
4. Hit Enter to set your PYTHONPATH in path variable.


To Use the tool
1. Fill the XMLSource1 and XMLSource2 Folder of XMLs to compare
2. Run the CompareItV2.bat 

Before Pushing codes, go to src/py directory
1. Run CMD
2. Type and Enter: `pip install pipreqs` (if not yet installed)
3. then type and enter: `pipreqs .`