FROM python:slim
RUN apt-get update && apt-get -y install cron vim
COPY requirements.txt /req/requirements.txt
RUN pip install -r /req/requirements.txt
WORKDIR /app
COPY crontab /etc/cron.d/crontab
COPY .env /app/.env
COPY main.py /app/main.py
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab
RUN echo $PYTHONPATH

# run crond as main process of container
CMD ["cron", "-f"]