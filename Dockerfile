FROM python:3.12.4
WORKDIR /app

COPY requirements.txt .
RUN pip install requirements.txt
COPY . .
EXPOSE 5001
CMD [ "python","app.py" ]