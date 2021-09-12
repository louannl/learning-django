# learning-django
Udemy course on Django 2021 - https://github.com/divanov11/Django-2021

## Getting started 
1. Environment setup
  ```
  virtualenv env
  source ..activate
  <!-- Can check packages and versions with pip list -->
  ```
2. Boiler template for Django
  ```
  django-admin startproject <-project name->
  ```
3. You can run the server within the folder by: 
  ```
  python manage.py runserver
  ```
  
  ```
  <!-- OUTPUT -->
  September 12, 2021 - 11:21:54
  Django version 3.2.7, using settings 'devsearch.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.
  ```

## Starting app 
1. Creating app 
  ```
  python manage.py startapp projects
  ```
2. Adding to settings.py file 
  ```
  INSTALLED_APPS = [
    'django.contrib.admin',
    <!-- ... -->

    'projects.apps.ProjectsConfig',
  ]
  ```

## The Basics
### URLS

urls.py had a list of paths: urlpatterns, which we can edit and add functions to: 

def project(request, pk):
    return HttpResponse('SINGLE PROJECT' + ' ' + str(pk))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects, name="projects"),
    path('project/<str:pk>/', project, name="project"),
]

To make this tidier: 
- Add the functions to the views.py file in our projects folder
- Add a urls.py file to projects, which imports those functions and setups a 
  url pattern. 
- Then add the include function to the urls.py in devsearch to dynamically 
  include those patterns.