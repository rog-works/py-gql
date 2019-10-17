FROM python:3.6-alpine

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /opt/app

CMD ["tail", "-f", "/dev/null"]

