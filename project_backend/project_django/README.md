Django:
i. Its a free and open source Web Application Framework.
ii. A framework is nothing but a collection of components which helps us build websites faster.
iii. Its used to create server based application and not desktop application hence a Backend Framework. 
iv. Django also has an Automatic Interface which supports CRUD thats
it allows you to CREATE -> READ -> UPDATE -> DELETE records

To Install Django, go to terminal and enter the command pip3 install Django
1. Create a folder on desktop and give it a name of your choice
2. Open Terminal, change directory into the new created folder 

CREATING A PROJECT FOLDER
3. Run the command: django-admin startproject project_name(eg. mysite)

NB: Inside a Django Project (the project folder) we can have multiple Apps

CREATING THE DJANGO APP
4. Change directory into the Project Folder (mysite)
5. Run the Command: django-admin startapp app_name(eg. myapp) to create a django application named myapp.

HOW RUN OUR PROJECT
6. Now to TEST THE SERVER, change directory into the project(mysite directory) folder and run this command: 
python3 manage.py runserver 
7. Press command button and click  the url… http://127.0.0.1:8000 
with http://127.0.0.1 being the address and :8000 being the Port Number
8. To stop the server press clt + C on your KeyBoard and the restart the server run: python3 manage.py runserver

9. Django is made up of the following Projects Files:
Files inside Application Directory(myapp):
    a. __init__.python - this signifies that the myapp directory is a python directory
    b. admin.py - this is used to customise the admin pannel which is to manage the website(installation comes with an admin panel)
    c. apps.py - contains the appsConfig
    d. models.py - One of the most import file in django which defines the structure of your database table of our application
    e. test.file - allows us to run certain tests of our application
    f. views.py - this file is used to control what we view on the web page
    g. test.py

Files inside Project Directory(mysite):
    a. The __init__.py file signifying that its a python file 
    b. The Settings file - it shows the database configurations and all other settings for example inside it you can identify that sqlite3 has been set as the default database at the DATABASE SETTINGS SECTION
    c. urls file - This handles all incoming urls (In django you are able to make your own urls to handle requests)
    d. asgi.py file - (Asynchronous Server Gateway Interface) 
    ASGI directly supports WebSockets, allowing developers to build more responsive web applications, and other highly interactive services that are not well suited to HTTP. It can also used to support HTTP long-polling, or HTTP Server Sent Events, which allows for uni-directional server-to-client updates.
    e. wsgi.py file - Web Server Gateway Interface (WSGI) is a mediator responsible for conveying communication between a web server and a Python web application. It explains how the web server communicates with the app and how the app can be chained for processing a request.
    d. manage.py -  provides set of commands to run the server 

10. CREATING VIEWS
    To display anything on the WEBPAGE we need to write VIEWS 
    a. Views are Python functions which accepts incoming REQUEST and returns HttpResponse in other to send a response. For the VIEW or Function to transport and display the page to the user it will need a transporter(car) called HttpResponse, hence we import into the view file --> (from django.http import HttpResponse) and go on to create the funtion for example --> 
    def home(request):
        return HttpResponse('Hello World')
    NB: You have to create a VIEW / FUNCTION for every Page of your Application

    b. Every HttpResponse from the Server(VIEW.py file) is required to have an IDENTITY/ADDRESS technically called a Uniform Resource Locator (URL) before it could display a page for the user. This IDENTITY OR URL is created in the URLs.py file at the urlpartterns section but before that we need to import the views.py file into the urls.py file, example
    --> from myapp import views.
    path('', views.homepage, name='homepage') 
    path('index/', views.home, name='index') 
    NB: An empty path '', means we are pointing to the homepage.

    c. Inside the return HttpResponse we can pass in a bunch of HTML tags but thats can not be a good pratice therefore we create templates and pass them in as context

    
    
11. CREATING MODELS
    Models: Database is an integral part of any backend and therefore if you are building a website and its data intensive, all those data need to be stored in a database. Configuring the web with the database its quite difficult but with django dealing with database is easier as it provides a database called sqlite3 with an Object Relational Mapper (ORM) to skip all the complexities involved in writing sql querries in updating, deleting, inserting and retrieving data.

    By creating a model, Django will automatically create a Table out of our model.
    NB: In Models are defined with python CLASS as compared to Views which uses FUNCTIONS eg. -->
    class Book(models.Model):
        name = models.CharField(max_length = 100)  
        author = models.CharField(max_length=100)
        description = models.CharField(max_length=100)
        price = models.DecimalField(max_digits=10, decimal_places=2)

    CONVERTING MODELS INTO ACTUAL DATABASE TABLEs
    After writing these models we need to convert them into actual database tables.

    NB: Before we could run the command to convert our model to actual database we have to ensure that our Application is INSTALLED or REGISTERED in the settings.py file. (Add to the installed_apps list in the settings file.)
    --Whenever you are developing a new application make sure to add it to the installed_apps list in the settings.file--
    
    The process of converting these models into actual database tables is called MAKINGMIGRATIONS....
    RUN     1. python3 manage.py makemigrations
            2. python3 manage.py migrate

12. ADDING/SAVING DATA INTO THE DATABASE
    i. To save, monitor, modify or view data you need to create a SUPER USER. You have to go the terminal and run
    python3 manage.py createsuperuser --> enter a longin name --> your email address --> and a password to create a SUPER USER ADMIN ACCOUNT 
    
    ii. Rerun the server, go to the admin section and enter your credentials to enter the ADMIN PANEL

    III. At the entry into the admin panel you will realise theres no model present in the panel (This is bcos we have not included or registered the model(created) in the admin file) and this can be done by importing the model into the admin file --> from .models import Book then after register it in the same admin file --> admin.site.register(Book) and after refreshing the admin panel you will see the model show up.

    iv. From there you will be able to save, modify, monitor, view update and delete data from the data base. 

    NB: (Aside using the DJANGO ADMIN PANEL you can USE the PYTHON SHELL to add data to the DB by running the command --> python3 manage.py shell, to use python shell to add data to the DB first
    i. import... from myapp.models import Book --> Book.objects.all() to see if there are any book available in the Book Model/ DB table
    ii. Create an Object for the Class  and pass in the various parameters as in -->
    a = Book(name='book_name', desc='book_desc', price=book_price) and run a.save() to add this data to the Book Model/DB Table)

13. PASSING OBJECTS / STORED DATA FOR VIEWING
    ***To render the stored data onto the webpage for viewing **
    We need to import model of the data into the VIEWS.py file
    as in --> from .models import Book --> and create define a function for it (VIEW)
    def home(request):
        book_list = Book.objects.all()
        return HttpResponse(book_list) ***** We can pass in the Object of the Book model DIRECTLY into the HttpResponse but thats not a good practise and therefore can not create a proper structure for the webpage so we create what we call TEMPLATES to handle HTML STRUCTURE dynamically for the webpage.
        as in the example below.

    def home(request):
        book_list = Book.objects.all()
        return render(request, 'myapp/home.html', {'book_list': book_list})

14. DJANGO TEMPLATES
    A Template is a HTML code to dynamically structure the webpage.
    To create a TEMPLATE you need to create a separate directory inside the APP Directory. Again create another folder/directory inside the template folder created as in App Directory/Folder --> Template Directory/Folder --> the Last Directory/Folder which will contain all the HTML files (Templates) for example... index.html

    def index(request):
        book_list = Book.objects.all()
        return render(request, 'myapp/index.html')

    def home(request):
        book_list = Book.objects.all()
        context = {'book_list':book_list}
        return render(request, 'myapp/home.html', context)
or
     def home(request):
        book_list = Book.objects.all()
        return render(request, 'myapp/home.html', {'book_list': book_list}) 

NOTE: Inside the HTML file we need write code in a templating manner for example when looping through a LIST or OBJECT of a list when have to write the code in a templating form as in --> 
{% for book in book_list %} and close it in a templating format -->
{% endfor %}
*******************************************************************
for example: {% for book in book_list %}
                {{book.title}}<br>
                {{book.author}}<br>
                {{book.description}}<br>
                {{book.price}}
             {% endfor %}

INSIDE THE VIEW FILE
def home(request):
        book_list = Book.objects.all()
        return render(request, 'myapp/home.html', {'book_list': book_list}) 

INSIDE THE VIEW FILE
def detail(request, book_id):
    return HttpResponse('This is book no %s' % book_list)
*******************************************************************
REMOVING HARDCODED URLS

INSIDE THE URL FILE
path('book/<int:book_id>/', views.detail, name='detail')

DISPLAYING THE CONTENT INSIDE THE HTML TEMPLATE
Here we are turining the displayed titles of the book into an achor tage or a link to visit the detail.html file (to another page)
{% for book in book_list %}
<a href='book/{{book.id}}'>{{book.title}}</a><br> --> HARDCODED URL NOT A BEST PRACTICE

<a href="{% url 'detail' book.id %}">{{book.title}}</a><br> THE RIGHT WAY USING THE FORMAT FROM THE URL.py
{% endfor %}

 URLs
    SEPARATING URLs
    Its important to separate your apps' urls from the project urls to avoid complexities in managing more urls in one file when projects begin to increase.
    Set a seperate url file in your app folder and INCLUDE it in the project url. by importing the INCLUDE method and passing it in the app urls --> from django.urls import path, include --> 
    path('', include('myapp.urls')),
    
    ** NAME SPACING IN URLs
    As the complexities of your project increases, as a good practice its important to pass the name of your app to your urls to avoid conflicts. This can be done by setting a name to your App url partterns --> app_name = 'myapp' then inside your url --> 
    <% for book in book_list %>
    <a href='{% url 'myapp:details' book.id}'> {{book.name}} 
    {% endfor %}

    ** ADDING STATIC FILES **
    STATIC_URL = 'static/'
    MEDIA_ROOT = os.path.join(BASE_DIR,'media')
    MEDIA_URL ='media/'
    
    create two subsequent linked folders in your app and create style.css. 
    Set a link tag in the home.file or index.file with these --> {% load static %} --> 
    <link rel='stylesheet' href='{% static 'myapp/style.css' %}'>
    NB: and restart the server for it take effect

    ** ADDING BOOTSTRAP TO THE WEBSITE **
    Go to the Bootstrap website and copy the css stylesheet link and paste it in the home.file

    ** USING BASE TEMPLATES **
    Helps to share for example navigation bars with several templates hence avoiding repetition of codes and the complexity of changing details on the navbar manually on all templates

    ** DISPLAY IMAGE ON THE PAGE **

    ** CREATING OWN FORMS IN DJANGO
    1. Create a view for the forms in the VIEWS.py file
    2. And set a URL for the for the forms view in the url.py file
    3. Set the form tag in the add_book.htm file to --> <form method='POST', enctype="multipart/form-data>
    NB: Anytime you create a form you need to add {% csrf_token %} which stands for CROSS SITE REQUEST FORGERY

    ** HANDLING FORMS IN DJANGO **



