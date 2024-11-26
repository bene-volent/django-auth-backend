@echo off

:: Remove the db.sqlite3 file
if exist db.sqlite3 (
    del db.sqlite3
    echo Removed db.sqlite3
) else (
    echo db.sqlite3 does not exist
)

:: Make migrations
python manage.py makemigrations
echo Made migrations

:: Apply migrations
python manage.py migrate
echo Applied migrations