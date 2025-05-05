# Pentru fisiere care contine secrete 
- creati un fisier numit '.env' la baza proiectului
- instalati libraria python-dotenv
- apelati functia load_dotenv(), si os.getenv('nume_variabila') --- vezi settings.py

!Atentie: Nu uitati sa adaugati fisierul .env in gitignore. .env NU ar trebui sa fie vizibil public pe github :)


# Pentru a rula testele
- python manage.py test nume_aplicatie
