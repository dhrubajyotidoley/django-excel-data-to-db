django-excel-data-to-db
=======================

Django: Upload an excel sheet file and extract the data to update in the database.

This is an application on Django to upload an excel sheet file and extracts it data to upload in the database.

Here in the demonstration we are using MySQL database.

So one need to create a database before using the application.

Then one have to sync the models on the MySQL database.
Using the command

python manage.py syncdb

Here on the project we created two apps, one is basically to upload the excel sheet and extract the data, and the other is to for the demo purpose to where one can upload the data.

Start the server with this command

python manage.py runserver

Then to browse the upload form one has to use this url

127.0.0.1:8000/upload/list
