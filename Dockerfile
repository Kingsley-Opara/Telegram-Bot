FROM python:3.9.0-slim

COPY . /app

WORKDIR /app

RUN python -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \ 
    /opt/venv/bin/pip install -r requirements.txt

# RUN chmod +x entrypoint.sh &&

EXPOSE 8080


CMD ["/opt/venv/bin/python", "./app/main.py"]

