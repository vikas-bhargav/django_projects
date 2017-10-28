# django_projects
Maintain the records of projects and expose api.


# Steps for run the project:

1. Clone the branch using the command 'https://github.com/vikas-bhargav/django_projects.git'

2. Got to project root directory

3. Form python shell run following commands:
	- python manage.py migrate 
	- python manage.py makemigrations

4. Now run you local server and in  browser type the following link for run the project:
	- http://127.0.0.1:8000/
5. Expose api for project example:
    - http://127.0.0.1:7000/api/project/?format=json
    - http://127.0.0.1:7000/api/project/1/
    - http://127.0.0.1:7000/api/project/?project_name=FMP

5. Extra libraries need to install: TastyPie 
