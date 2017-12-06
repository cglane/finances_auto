Implementation of Google Sheets Api and machine learning techiques to predict a description for a given financial transaction.


## How To
- git https://github.com/cglane/finances_auto.git
- source virt/bin/activate
- pip install -r requirements.txt
- python manage.py runserver

- cd frontend
- npm install
- npm run start

## Tools

- Django
- pygsheets
- Webpack
- React
- Material UI
- Pandas
- CountVectorizer
- Support Vector Machine(SVM)


## Creating Database

- Iterates through personal financial transactions housed in Google Sheet Document
- Adds a Transaction object to DB based on every transaction 

## UI

- React app that runs independently of Django Server
- Allows transaction upload from (American Express, Capitol One, and Bank of America)
- Trains SVM on passed transactions and describes uploaded transactions
- Displays described transactions with editable fields
- Allows user to upload new transactions to Google Sheets
