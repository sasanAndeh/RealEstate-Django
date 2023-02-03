import os , time
os.system('python manage.py migrate --run-syncdb')
time.sleep(2)
os.system('python manage.py makemigrations')
time.sleep(2)
os.system('python manage.py migrate ')
