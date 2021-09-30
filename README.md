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
path('admin/', admin.site.urls), path('projects/', projects, name="projects"), path('project/<str:pk>/', project, name="project"),
]

To make this tidier:

- Add the functions to the views.py file in our projects folder
- Add a urls.py file to projects, which imports those functions and setups a url pattern.
- Then add the include function to the urls.py in devsearch to dynamically include those patterns.

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

to include another html file within our html file, we could add the following, template tag:
{% include 'navbar.html' %}

We could also add the following to a 'main template' file like so:

```  
<body>
  {% include 'navbar.html' %}

  {% block content %}
  
  {% endblock content %}
</body>
```

Then we would only need to include the starting and end block on our other templates to render them within the above
main template:

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
(e.g. projects) within. i.e. projects -> templates -> projects

We then adjust the views.py file like so:
def project(request, pk):
return render(request, 'projects/single-project.html')

### Rendering Data to Templates

Django uses templating engine ginger.

Variables are surrounded by {{ and }}.

Dictionary lookup, attribute lookup and list-index lookups are implemented with a dot notation:
{{ my_dict.key }} {{ my_object.attribute }} {{ my_list.0 }}

Tags:
This is a way of adding python language into the template:
{% %} If using an if statement you need to use a 'closing tag':
{% if user.is_authenticated %}Hello, {{ user.username }}.{% endif %}

Filters: using pipes {{ django | title }}

We can pass in data to our templates via the view.py functions like so:

``` 
def projects(request):
    page = 'projects'
    number = 11
    context = {'page': page, 'number': number}
    return render(request, 'projects/projects.html', context)
```

Using an elseif example:

```
{% if number > 10 %}
<p>Number is greater than 10</p>
{% else %}
<p>Number is less than 10</p>
{% endif %}
```

Using the id:

```
def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
```

Passing in routes:
Instead of passing in a static url to a html tag, we can use django, and use the route name='project'

```
<a href="{% url 'project' project.id %}">
``` 

## Building our Database

### Models and Admin Panel

Django already preps some defaults to setup the database.

To run migrations (not using your own via make migrations) run:

```
python manage.py migrate 
```

You could then go to /admin to access the admin panel.

To create a user run:

```
python manage.py createsuperuser
```

By default, using migrations, will create a Groups and Users table.

Python uses classes and inherits from Django models. When you have created a model, in the models.py file, you then need
to run:

```
python manage.py makemigrations
<!-- Then run the migrations  -->
python manage.py migrate
```

This will add data to the migrations folder.

When accessing via the admin panel, we can access our Products model by first registering the model in the admin.py
file, like so:

```
from django.contrib import admin

# Register your models here.
from .models import Project

admin.site.register(Project)
```

However, you'll notice when we add some projects, the names will not be the names of what we inserted. To change this we
can add a method to the model:

```
def __str__(self):
        return self.title
```

### Database Relationships

drawsql.app is pretty useful for visualizing the relationships.

I know quite a bit about relational databases so I'm going to gloss over this section...

Relationship types:
one-to-one one-to-many many-to-many

on_delete=models.SET_NULL --> if the item is deleted for the foreign table it will set this field to null rather than
cascade delete.

### Database Queries

Again, this is pretty similar to others I have used.

Let's us interact with the database:

```
python manage.py shell
```

We can use it like so:

```
from projects.models import Project
projects = Project.objects.all()
print(projects)
```

To query the children we can use .childmodel_set.all()
e.g. project.review_set.all(), will give the review table too.

For a many-to-many relationship we can use .relationshipname.all()
e.g. project.tags.all()

Querying in our views file: We can query like so:
from .models import Project

def projects(request):
projects = Project.objects.all()

## Create Update Delete (CRUD)

### Model Forms

Django forms use a cdrf_token to ensure the data is clean.

We can make a form template using the table as a reference: (forms.py):

```
from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
```

fields = '__all__' creates fields based on every attribute (except un-editable and auto-generate fields e.g. id and
createdAt)

We can then import this to the views folder and use it like so:

def createProject(request):
form = ProjectForm()
context = {'form': form} return render(request, "projects/project_form.html", context)

We could also do things on the template such as:
{{form.as_p}} Which will wrap each form item in a paragraph tag.

### Create Read Update Delete (CRUD)

we can add to our form a post request:

if request.method == 'POST':
form = ProjectForm(request.POST)
if form.is_valid():
form.save()
return redirect('projects')

Similarly, we can use a similar format for delete etc.

## Static Files and Theme installation

### Static Files

New folder: Static > images, styles, js

If we make some css files for example, we will need to let django know to include them, in our settings folder by
adding 'staticfiles_dirs..':

```
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'static')
    BASE_DIR / 'static'
]
```

```
<link 
  rel="stylesheet" 
  type="text/css" 
  media="screen" 
  href="{% static 'styles/main.css' %}"
>
```

When using a live server, you won't use the static folder, we need to set the static_root in settings, which will define
where our files will go in production.

```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

The 'collect static' command will take all these static files and bundle them for us when in production.

```
python manage.py collectstatic
```

You should run this before deployment after any changes.

### Theme Installation

FORM:
We can add the following to forms.py to dynamically add a class to our form attributes:

```
    widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})

```

## Add More Apps

### Users Apps

Like before we can run the following command to set up a default file:

```
python manage.py startapp users
```

And again we add to our settings file the installed app for users.
