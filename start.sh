# !/bin/bash

source virt/bin/activate

python manage.py runserver &

cd frontend

npm run start