FROM woahbase/alpine-python2

RUN pip install pudb

COPY app/ /app
WORKDIR /app

EXPOSE 6900

CMD ["python", "example.py"]
