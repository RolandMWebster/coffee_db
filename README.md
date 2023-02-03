# Coffee DB

Tool for uploading and storing coffees in a DB.

## Running Locally

In order to run the app locally, it requires you to have postgresql installed on your machine.

Then add a database.ini file in the following location: `coffee_db/database/database.ini`

The file should look like the following:
```
[postgresql]
host=localhost
dbname=your_database
user=your_user
password=your_password
```

Install the requirements

```pip install -r requirements.txt```

Then run the streamlit app from the root directory.

```streamlit run app.py```



## Heroku Commands

### Deploying to Heroku

Once you have merged your updates into `main`, you can call the following command to push to Heroku which will automatically deploy the new code:

```
git push heroku main
```

TODO: Add github actions to automatically deploy to Heroku once code is merged into `main`.


### Heroku PSQL CLI

Use the following command to interact with the deployed psql database:

```
heroku pg:psql
```