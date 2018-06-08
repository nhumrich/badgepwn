from python:alpine

RUN python3 -m pip install paho-mqtt

COPY run.py /app/

CMD python3 -u /app/run.py
