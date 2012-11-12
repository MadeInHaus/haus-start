HAUS-start installs a script which allows the easy creation of Django
projects and applications.  Based on the red-start project from RED interactive.

How to use
==========

Creating a project
------------------

    pip install pip install git+https://github.com/madeinhaus/haus-start.git
    haus-start project

This will use the default project template, which includes
HAUS's [django-template](https://github.com/madeinhaus/django-template).

Running a project
-----------------

    cd example
    sh scripts/setup.sh
    source env/bin/activate
    cd project
    python manage.py syncdb
    python manage.py runserver


How does it work
================

Creating a project from a template
----------------------------------

Running haus-start does three simple things:

1. Creates a new folder called `<folder_name>`.
2. Copies in that folder all the files included in the project template folder. This can be specified with the `--template-dir` option; the default is `templates/project/django-template`.
3. If a file called `haus_start_settings.py` is present in that folder, and if it contains a function called `after_copy`, then that file is loaded and that function executed.

As an example, in the case of the django-template project template, the [after_copy function](https://github.com/madeinhaus/haus-start/blob/master/haus_start/templates/project/django-template/haus_start_settings.py) downloads an HTML5 boilerplate from GitHub, prompts the user for some variables and substitutes them in the template. This is just an example, other project templates can perform any other operation.


Creating a new project template
-----------------------------------

To add a new project template to haus-start, simply add it in the `templates` folder, under `project`. If you need to perform extra actions after the files have been copied, add a file called `haus_start_settings.py` with an `after_copy` function (take a look at existing templates).

Finally, to use the newly created template, just indicate its path as the `--template-dir` option, for instance:

    haus-start --template-dir=/your/custom/template new_example
