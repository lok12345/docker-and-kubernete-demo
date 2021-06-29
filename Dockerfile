FROM python:3.7

RUN mkdir /kubernete_demo
WORKDIR /kubernete_demo
ADD . /kubernete_demo/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/kubernete_demo/demo.py"]