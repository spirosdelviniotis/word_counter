
=================
Word Counter
=================

Tutorial (https://realpython.com/flask-by-example-part-1-project-setup/)


How to execute:

.. code-block::

    ~/repos/zphase -  (master) $ heroku login -i
    ~/repos/zphase -  (master) $ heroku config:set APP_SETTINGS=config.DevelopmentConfig --remote heroku
    ~/repos/zphase -  (master) $ heroku run python src/app.py --app serene-beach-63709
    ~/repos/zphase -  (master) $ git push heroku master

.. code-block::

    ~/repos/zphase/src -  (master) $ python src/manage.py db init
    ~/repos/zphase/src -  (master) $python src/manage.py db migrate
    ~/repos/zphase/src -  (master) $python src/manage.py db upgrade

.. code-block::

    ~/repos/zphase -  (master) $ heroku addons:create heroku-postgresql:hobby-dev --app serene-beach-63709
    ~/repos/zphase -  (master) $ heroku config --app serene-beach-63709
    ~/repos/zphase -  (master) $ heroku run src/python manage.py db upgrade --app serene-beach-63709

