FROM python:3.6

COPY . /house-renting/crawler

VOLUME /etc/scrapyd/ /var/lib/scrapyd/

WORKDIR /house-renting/crawler

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
