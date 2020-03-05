FROM python:3.6

ADD ./ /usr/local/docker_text/
RUN pip install -r /usr/local/docker_text/requirements.txt -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com

CMD python /usr/local/docker_text/app.py