FROM python:3.12.2
WORKDIR /app
ENV ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get -y update
RUN apt-get -y upgrade
CMD ["python3", "Mtumaji.py"]
