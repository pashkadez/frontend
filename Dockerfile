FROM python:3.9-slim

RUN useradd serve

WORKDIR /home/serve

COPY requirements.txt requirements.txt
RUN python -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY frontend.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP frontend.py

RUN chown -R serve:serve ./
USER serve

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
