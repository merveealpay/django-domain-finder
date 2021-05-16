
FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
EXPOSE 8000
#CMD ["python","manage.py","runserver","--settings=config.settings.docker"]
ENTRYPOINT ["sh", "docker-entrypoint.sh"]
