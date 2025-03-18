## Steps to Set Up a Virtual Environment for the Project

Create a Virtual Environment
`python -m venv venv`

Activate the Virtual Environment
`venv\Scripts\Activate` - Powershell
`venv\Scripts\activate.bat` - cmd
`source venv/bin/activate` - Linux

Deactivate the Virtual Environment
`deactivate`

To wrap the dependency of the package with in the project
`pip freeze > requirements.txt`

To run in another machine (In the Shell)
`python -m venv venv`
`venv\Scripts\Activate`
`pip install -r requirements.txt`

## Pandas

- Package to manipuate tables
- Built on top of numpy so is efficient
- Two baic Data structures
    - Series - 1D array rep
    - DataFrame - 2D array rep
- 