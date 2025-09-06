### Wine Cellar ###



## Wine Cellar - Technology Stack

*Backend :  

    -Django (Python)	: The core web framework for handling application logic, database models, user authentication, and serving HTML templates.

	-Celery : An asynchronous task queue. Used for running background tasks, such as sending reminder emails about wines.

*Frontend :  

    -Django Templates : Used for the main page structure (server-side rendering) like base.html and lists (wine_list.html).

	-React (with TypeScript) : A JavaScript library for building complex and interactive user interface components, like the wine map.

	-Webpack & npm :	Frontend build tools. They compile and bundle the TypeScript/React code into optimized JavaScript files that run in the browser.

	-Plain CSS : Used for the custom styling of the application.

*Database :  

    P-ostgreSQL : A powerful, open-source relational database used to store all application data (wines, users, vineyards, etc.).

*Web Server / Proxy :  

    -unicorn : The WSGI server that runs the Python/Django application in a production environment.

	-Caddy : A modern, powerful web server. In this project, it likely acts as a reverse proxy to handle HTTPS (SSL) and route traffic to the Gunicorn server.

*DevOps / Tooling :  

    -Docker & Docker Compose : Used to create isolated, reproducible development and production environments for all the services (Django, PostgreSQL, etc.).
	
    -Make (Makefile) : A build automation tool used to simplify common commands (e.g., make install, make server).
	
    -MkDocs : (mkdocs.yml)


## Installation

1-Clone the repository:
```bash
git clone https://github.com/GGurol/wine-cellar.git
```

```bash
cd wine-cellar
```

2-Build the docker and it's contens:
```bash
docker compose up --build -d
```

3-Database Operations:
```
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

4-Import Data:
```
docker compose exec web python manage.py loaddata fixtures/classification.json
docker compose exec web python manage.py import_wines_from_csv datasets/XWines_Test_100_wines.csv
```

4-Visit http://localhost:8000

5-Admin Panel : http://localhost:8000/admin

Default admin login :  
    username : admin
    password  :22222222


*** Tip : visit django's admin panel, you will see filled data. If you edit a 'wine' for user admin; you can see on homepage.




**Wine Cellar** is a self-hosted wine management app built with Django, designed for wine enthusiasts to track wines, store tasting notes, rate wines, and manage inventory. Whether you're a casual drinker or a connoisseur, this app helps organize your collection.

<img src="https://github.com/user-attachments/assets/315280b8-9f87-45fd-ab88-507d88aef362" height="150" alt="Landing page showing different statistics about your wines">
<img src="https://github.com/user-attachments/assets/645855e4-3c22-4253-9d59-9fd76f7f4c05" height="150" alt="Wine list view showing all wines in the database">
<img src="https://github.com/user-attachments/assets/dec2345b-e276-43bf-aac9-e667f3a535b3" height="150" alt="wine detail view showing a picture of a wine and it's attributes">

## Features

- **Wine Tracking**: Record and review wines you've tasted.
- **Inventory Management**: Monitor bottle stock levels.
- **Multi-User Support**: Host for yourself and your friends.
- **Barcode Scanning**: Easy adding and removing known wines by scanning their
barcode.
- **Tasting Notes**: Save aroma, flavor, and experience details.
- **Wine Ratings**: Rate wines to track preferences.
- **Food Pairings**: Add recommended food pairings.
- **Self-hosted**: Full control over your data.

