FROM python:3.10-slim

ENV WORKDIR=/app \
    PATH=$PATH:$WORKDIR \
    PYTHONPATH=$PYTHONPATH:$WORKDIR

WORKDIR $WORKDIR

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ $WORKDIR/src

COPY docker-entrypoint.sh .

ENTRYPOINT ["docker-entrypoint.sh"]
