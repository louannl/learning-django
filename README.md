# learning-django
Udemy course on Django 2021 - https://github.com/divanov11/Django-2021 -
https://www.udemy.com/course/python-django-2021-complete-course/

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

### Templates and Template inheritance
1. Add a templates folder in the main directory.
2. Add template htmls files.
3. Add to settings the following: 
   TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            <!-- insert this line -->
            os.path.join(BASE_DIR, 'templates'),
        ],
    <!-- ... -->
*note: In theory we don't need to import os with Django

This then allows us to read the html files via the views file: 

def projects(request):
    return render(request, 'projects.html')

Our HTML templates: 

to include another html file within our html file, we could add the following,
template tag:
    {% include 'navbar.html' %}

We could also add the following to a 'main template' file like so:

```  
<body>
  {% include 'navbar.html' %}

  {% block content %}
  
  {% endblock content %}
</body>
```

Then we would only need to include the starting and end block on our other 
templates to render them within the above main template:
```
{% extends 'main.html' %}

{% block content %}

<h1>Projects Template</h1>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis repudiandae 
  odio quas accusamus quod neque officiis atque doloribus eaque? Fugiat 
  accusamus beatae, aliquid assumenda nam tempore voluptatem magnam enim 
  voluptate.
</p>

{% endblock content %}
```

Built-in Django way of separating apps: 
Create within an app file (e.g. projects folder) a templates file, and then 
(for some reason) create a folder with the same file name as the app folder
(e.g. projects) within.
i.e. projects -> templates -> projects

We then adjust the views.py file like so: 
def project(request, pk):
        return render(request, 'projects/single-project.html')


