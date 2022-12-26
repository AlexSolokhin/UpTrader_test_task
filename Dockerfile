FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /uptrader_test_task
RUN pip install --upgrade pip


COPY requirements.txt /uptrader_test_task/
COPY menu_tree /uptrader_test_task/menu_tree/

RUN python -m pip install -r /uptrader_test_task/requirements.txt

WORKDIR /uptrader_test_task/menu_tree

RUN python manage.py migrate
RUN python manage.py loaddata fixture.json

EXPOSE 5000

CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
