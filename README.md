# Django-forum-site
Actually i didn't purchased any domain. So, below is the public IP address.

You can access this website by clicking this: http://15.206.170.238

I deployed this website on EC2 instance provided by AWS. And used SQLlite as default database used by Django. 

Also used GUNICORN as the WSGI server which takes care of everything which happens in-between the web server and my web application & NGINX as a reverse proxy for a GUNICORN server.


# About this project:

Made a website which has login, logout, signup feature.
Also you can do post on it, delete that post also.

We've "default" user. He can do post and able to delete its own post only!

We've "mod" user. He can delete anyones post, but not able to ban anyone.

We also have a "superuser". He can BAN user, after which that user will not able to do post. And delete anyones post also.

I've use Django for backend and HTML, CSS, very little JavaScript.

🙏
