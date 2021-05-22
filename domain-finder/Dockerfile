
FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN chmod +x /app/docker-entrypoint.sh
COPY docker-entrypoint.sh /
EXPOSE 8000

