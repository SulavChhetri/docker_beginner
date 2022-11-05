FROM python:3.8-slim-buster

LABEL Maintainer="sulavthapa"

WORKDIR /src

RUN pip install flask


COPY . .

CMD ["python3","app.py"]
# EXPOSE 5000
# CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]

