FROM python:3-alpine

LABEL Maintainer="sulavthapa"

WORKDIR /usr/app/src

RUN pip install flask

COPY . .

EXPOSE 5000

CMD ["flask", "run","--host","0.0.0.0","--port","5000"]