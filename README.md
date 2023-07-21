# Django-forum-site
Actually i didn't purchased any domain. So, below is the public IP address.

You can access this website by clicking this: http://13.126.102.215

I deployed this website on EC2 instance provided by AWS. And used SQLlite as default database used by Django. 

And also used NGINX which acts as a reverse proxy for a Gunicorn server, passing all dynamic requests to Gunicorn, and as a regular server for static files, handling this task on its own.

Also used GUNICORN which takes care of everything which happens in-between the web server and my web application.

# About this project:

Made a website which has login, logout, signup feature.
Also you can do post on it, delete that post also.

We've "default" user. He can do post and able to delete its own post only!

We've "mod" user. He can delete anyones post, but not able to ban anyone.

We also have a "superuser". He can BAN user, after which that user will not able to do post. And delete anyones post also.

I've use Django for backend and HTML, CSS, very little JavaScript.

🙏
