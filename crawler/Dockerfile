FROM python:3

MAINTAINER kezhenxu94 <kezhenxu94@163.com>

COPY ./scrapyd.conf /etc/scrapyd/

COPY . /house-renting/crawler

VOLUME /etc/scrapyd/ /var/lib/scrapyd/

WORKDIR /house-renting/crawler

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
