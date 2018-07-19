# Django practice nº 4

### Setup Instruction

```bash
$ mkvirtualenv -p $(which python3) django_practice_4
$ pip install -r requirements.txt
$ make migrate
```

You can now run the development server and point the browser to the correct URL:

```bash
$ make runserver
```


### Your Tasks

The goal for this practice is to keep working with forms, but in this case we'll make usage of the tools provided by Django instead of writing them by hand in HTML. As always, the structure of the Django project is built for you and you'll have your work divided in a couple of tasks.

If you run the development server with `$ make runserver`, you'll be able to test the project in the browser pointing to the URL that Cloud9 provides to you.

You can load some initial data into your database by running this script:

```bash
$ make load_initial_data
```

You should see an `Imported!` message when the command execution finishes. That means all initial data was imported successfully. You'll now have a superuser created with username `admin` and password `admin` credentials.


#### Part 0 - Authentication

This part is all provided to you as an example, you won't need to do anything at all. We'll use [Django built-in authentication views](https://docs.djangoproject.com/en/2.0/topics/auth/default/#module-django.contrib.auth.views) to implement a simple Login/Logout functionality.

If you take a look at `django_practice_4/urls.py` you'll see two URLs related with authentication, that use this views imported from Django. All the logic is implemented for you. Only by adding this URLs and a login form inside `registration/login.html` is enough. There are also two new settings that you can set to specify where you want to redirect the user after login or logout.

For the following two parts you'll be working on `artist` view, inside `artists/views.py` module. We want this view to be login required. This means that the user must be logged in to have access to this URL. This validation is implemented for you at the very beginning of the view. It just checks if `request.user.is_authenticated`, and if not, it redirects to `/login` URL where a login form will be rendered.

You can use the user with username `admin` and password `admin` credentials that you created in the initial data, or create a brand new user with any credentials that you want.


#### Part 1 - Working with Basic Django Forms

We'll keep using the `Artist` and `Song` models from previous practices, and our template with the list of Artists and forms for creating proper objects.
For this part, you'll have to reply the "Add a new Artist" form like in the last practice but in this case, you must use a [Django basic Form](https://docs.djangoproject.com/en/2.0/topics/forms/).

There's a `forms.py` module inside `artists` app where the Form needs to be implemented. The rest of the logic must be done inside `artists` view in `artists/views.py` and in the `index.html` template.

You will have to handle both `GET` and `POST` requests in the same `artists` view, analysing what value comes in `request.method`.
- If 'request.method == GET', you just have to make an instance of the form and return it as context to the template for later rendering, along with the list of all artists stored in the database
- If 'request.method == POST', you make an instance of the form with the data that comes in request.POST, and then, if the form is valid, create the proper Artist object with the provided values.

In `templates/index.html` you'll have to render the form that you sent as context in the same way you render any other object (with `{{ form_name }}`). This will build for you all the inputs related to the form and render them as HTML code.


#### Part 2 - ORM exercises

For this part of the practice you will work inside the `artists/orm_exercises.py` file. You'll find there a couple of functions that are the tasks you have to implement, using the different ORM methods that are provided by the Django `objects` manager.
Each of the task has its instructions as a docstring, so use them as a guide to know what you have to do.

In order to check if you implemented them correctly, there are tests associated to each task inside the `artists/tests.py`. You can run the tests like this:

```bash
$ make test
```
