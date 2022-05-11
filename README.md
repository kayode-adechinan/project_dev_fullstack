# Récupérer le projet

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

# Démarrer le client pour l'envoie de données

```bash

$ python socket_client.py

```

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
