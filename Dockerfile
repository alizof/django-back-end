FROM python:3.12


##ENV G4F_PROXY=http://localhost:8080

WORKDIR /app
COPY . .


RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:7777"]

EXPOSE 8000
