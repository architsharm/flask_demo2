FROM python:3.9-slim-bookworm

WORKDIR /flask-docker

COPY requirements.txt requirements.txt 
COPY . .


RUN python3 -m pip install --upgrade pip 
RUN pip3 install -r requirements.txt
RUN pip3 install pandas

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
