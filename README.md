# TDD Api


1. Activar Python virtualenv

    `cd API` (nombre del virtualenv actual)

    `source bin/activate`

    `(API)$` Debe verse el nombre del virtenv en la terminal


    * Desactivar Python virtualenv

        `(API)$ deactivate`


2. Instala los requisitos

    `pip install -r requirements.txt`

    * Para crear los requirements
        `pip freeze > requirements.txt`

3. Crea una base de datos llamada `puppy_store_drf`

4. Aplica las migraciones

    `python manage.py makemigrations`

    `python manage.py migrate`

5. Corre los test

    `python manage.py test`

6. Corre el server

    `python manage.py runserver`


