FROM python:3.6-slim
MAINTAINER atal@localhost

COPY ./ /

WORKDIR /

RUN apt-get update

RUN apt-get install -y default-libmysqlclient-dev gcc default-mysql-server default-mysql-client-core default-mysql-client findutils

RUN pip3 install --no-cache-dir -r requirements/dev.txt

COPY ./docker/dev/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
