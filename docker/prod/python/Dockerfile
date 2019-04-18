FROM python:3.4
MAINTAINER atal@localhost

COPY ./ /

WORKDIR /

RUN pip3 install -r requirements/prod.txt

COPY ./docker/prod/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
