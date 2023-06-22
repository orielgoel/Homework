FROM python:3.7-alpine
ADD . /code
WORKDIR /code
RUN pip install flask
RUN pip install pymysql
CMD ["python", "/code/rest_app.py"]