
# pull official base image
FROM python:3.9


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev

RUN apt-get update && apt-get -y install \
    build-essential libpcre3 libpcre3-dev zlib1g zlib1g-dev libssl-dev wget libpq-dev python-dev

COPY . /usr/src/app
VOLUME ["/usr/src/app"]
WORKDIR /usr/src/app
RUN dir -s 
# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod +x setup.sh

EXPOSE 8000

# run entrypoint.sh
CMD ["sh", "setup.sh"]
