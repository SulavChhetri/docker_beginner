FROM python:alpine

LABEL Maintainer="sulavthapa"

RUN pip install flask

WORKDIR /src

COPY . /src/

EXPOSE 5000

CMD ["python","app/app.py"]
# CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]

