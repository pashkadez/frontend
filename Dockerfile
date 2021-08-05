FROM python:3.9-slim

RUN useradd serve

WORKDIR /home/serve

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app app
COPY frontend.py config.py ./

ENV FLASK_APP frontend.py

RUN chown -R serve:serve ./
USER serve

EXPOSE 55000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
