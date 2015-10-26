sudo su - postgres &
sleep 5
python3 manage.py migrate
python3 manage.py runserver