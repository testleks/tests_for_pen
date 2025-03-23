FROM python:3.10-alpine3.19

WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN pip3 install -r requirements.txt

CMD "pytest"