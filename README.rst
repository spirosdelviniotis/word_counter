
=================
Word Counter
=================

Tutorial (https://realpython.com/flask-by-example-part-1-project-setup/)


How to execute:

.. code-block::

    Creating a Heroku app (app-name=serene-beach-63709)

        ~/repos/zphase -  (master) $ heroku login -i
        ~/repos/zphase -  (master) $ heroku create <<app-name>>
        ~/repos/zphase -  (master) $ heroku config:set APP_SETTINGS=config.DevelopmentConfig --remote heroku
        ~/repos/zphase -  (master) $ heroku run python src/app.py --app serene-beach-63709
        ~/repos/zphase -  (master) $ git push heroku master

.. code-block::

    ~/repos/zphase/src -  (master) $ python src/manage.py db init
    ~/repos/zphase/src -  (master) $python src/manage.py db migrate
    ~/repos/zphase/src -  (master) $python src/manage.py db upgrade

.. code-block::

    Configuring Postgres on Heroku:

        ~/repos/zphase -  (master) $ heroku addons:create heroku-postgresql:hobby-dev --app serene-beach-63709
        ~/repos/zphase -  (master) $ heroku config --app serene-beach-63709
        ~/repos/zphase -  (master) $ heroku run src/python manage.py db upgrade --app serene-beach-63709

.. code-block::

    If you are not getting your jobs done, make sure you have 1) the worker listening 2) the redis server up 3) the manage.py running.

        Terminal 1: redis-server
        Terminal 2: python manage.py runserver
        Terminal 3: python worker.py

.. code-block::

    Configuring Redis on Heroku:

        ~/repos/zphase -  (master) $ heroku addons:create redistogo:nano --app serene-beach-63709
        ~/repos/zphase -  (master) $ heroku config --app wordcount-stage | grep REDISTOGO_URL
        ~/repos/zphase -  (master) $ heroku local
