FROM python:3.8.1

RUN apt-get update
WORKDIR /home/

RUN git clone --depth 1 https://github.com/noeul1114/vultr_django_test.git

WORKDIR /home/vultr_django_test

RUN pip install -r requirements.txt

EXPOSE 8000
