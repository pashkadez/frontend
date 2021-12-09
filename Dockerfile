FROM python:3.9-alpine

RUN pip3 install --upgrade pip
RUN apk add gcc musl-dev build-base

RUN adduser -D worker
USER worker
WORKDIR /home/worker

ENV PATH="/home/worker/.local/bin:${PATH}"
COPY --chown=worker:worker requirements.txt requirements.txt
RUN pip3 install --user -r requirements.txt

COPY --chown=worker:worker . .
ENV FLASK_APP frontend.py

EXPOSE 80

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
