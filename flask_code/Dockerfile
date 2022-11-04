FROM python:alpine

LABEL Maintainer="sulavthapa"

RUN pip install flask

COPY ./src .
COPY . .

EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]

