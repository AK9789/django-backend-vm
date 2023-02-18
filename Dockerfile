FROM python:3.8
WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip
RUN python -m pip install pipenv
RUN python -m pip install django
RUN python -m pip install djangorestframework
RUN python -m pip install django-cors-headers
RUN python -m pip install pymysql
RUN python -m pip install PyJWT
RUN python -m pip install cryptography
RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 8000
CMD ["python","manage.py","runserver"]