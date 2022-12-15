#python manage.py flush --no-input
python manage.py makemigrations authentication
python manage.py makemigrations hello_world
python manage.py migrate
#python manage.py initadmin
python manage.py runserver 0.0.0.0:8000