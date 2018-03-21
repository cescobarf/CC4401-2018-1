Para correr el servidor antes se deben correr los siguientes comandos:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

La interfaz de administración se encuentra en `localhost:8000/admin` y la vista que creamos en `localhost:8000/tareas`