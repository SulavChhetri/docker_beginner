FROM keinos/sqlite3

LABEL Maintainer="sulavthapa"

WORKDIR /usr/app/

COPY database.db ./