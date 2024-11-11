PROJECT STRUCTURE 
1. Getting started with Django
2. Models and Admin
3. Testing -> Models(optional)
4. URL's, Views 
5. Templates -> Bootstrap
6. Testing -> Views(optional)
7. PEP's - Python Style Conventions



- models 
create the db (model)
make migrations and migrate 

- media files 
configure the media folder (here we to tell django we are using a media folder)... go to settings in the core directory to set up the media url and the media root at the last part
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

- configure the url
here need we to be able to access the static and the settings.. so we import
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

- admin configuration
Basic admin configuration
Import the models and register them

- testing
An important stage in development to improve the quality of the application
NB: Create a Tests Folder and separate test into separate files (one for models and ther other for views)
pip install coverage
and run 
coverage run manage.py test
to scan all files to check where test is required
or run the command
coverage report
to check what file or files require testing, again
run 
coverage html
this would create a new folder (htmlcov)
(Basically testing is done to ensure that for example, the out we expect our db to produce is actually the outcome being produced we also test to see if the wrong outcome will be produced)
NB: Test is not run on the main db but on a separate db(a copy of the main)
Coomand to testing the application for errors or no errors (excluding scan of the venv directory)
coverage run --omit='*/venv/*' manage.py test


- urls and views configurations
NB: Its always adviceable to manage all urls relating to the application in the application.
NB: The Django templating language (check out)


- Django Templateing Language
After creating the Template we need to inform django where the templates are stored


******************************
<!-- <div class="dropdown text-end">
              <a href="#" class="d-block link-body-emphasis text-decoration-none dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                <img src="https://github.com/mdo.png" alt="mdo" width="32" height="32" class="rounded-circle">
              </a>
              <ul class="dropdown-menu text-small">
                <li><a class="dropdown-item" href="#">New project...</a></li>
                <li><a class="dropdown-item" href="#">Settings</a></li>
                <li><a class="dropdown-item" href="#">Profile</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">Sign out</a></li>
              </ul>
            </div> -->
******************************