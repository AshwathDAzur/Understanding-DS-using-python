## Steps to Set Up a Virtual Environment for the Project

Create a Virtual Environment
`PS C:\OrgProjects\SkillUps\Understanding-DS-using-python> python -m venv venv`

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