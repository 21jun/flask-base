FROM python3.6

ADD . /www
WORKDIR /www

RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi

CMD uwsgi uwsgi.ini