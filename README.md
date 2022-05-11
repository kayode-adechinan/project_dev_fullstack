# Récupérer le projet

```bash

$ git clone git@github.com:kayode-adechinan/project_dev_fullstack.git

```

# Configurer la base de données mysql

On peut configurer la base de données en changeant les valeurs suivantes:

```
DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "127.0.0.1"
DB_NAME = "coordinates_db"
```

# Installer les dépendances du projet

```bash
$ pip install -r requirements.txt
```

# initialiser la base de données

```bash

$ python init_db.py

```

# Démarrer le server socket

```bash

$ python socket_server.py

```

![demo](screenshots/server.png)

# Démarrer le client pour l'envoie de données

```bash

$ python socket_client.py

```

![demo](screenshots/client.png)

# Pause de 2 seconds

Le fichier client.py contient à la ligne 15 cette instruction

```python
time.sleep(2)
```

Cela permet d'appliquer la pause de 2 seconds

# Vérifier que l'api renvoi les données au format json

http://localhost:5000/coordinates

```json
{
  "coordinates": [
    {
      "id": 1,
      "latitude": "8.5509906",
      "longitude": "39.3109560"
    },
    {
      "id": 2,
      "latitude": "8.5508500",
      "longitude": "39.3108900"
    },
    {
      "id": 3,
      "latitude": "8.5471500",
      "longitude": "39.3128000"
    }
  ]
}
```

# Démarrer le serveur web pour accéder à la carte et les marqueurs

```bash

$ python app.py

```

# Ouvrir ensuite le navigateur à cette page

http://localhost:5000/

- La carte google map utilise la librairie

leaflet.js

![demo](screenshots/dashboard1.png)

![demo](screenshots/dashboard2.png)

En dessous de la carte se trouve un bouton "refresh" permettant de rafraichir la carte à l'aide d'une requête ajax dont le code se trouve dans le fichier "static/js/app.js"

# Les données en base de données

![demo](screenshots/data.png)

# Note

Il faut une connection internet active pour le projet puisse télécharger les fichiers cdn des librairies suivantes

- leaflet.css
- leaflet.js
- axios.js
