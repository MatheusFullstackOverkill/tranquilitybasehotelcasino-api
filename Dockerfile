FROM python:3.8.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN echo $(ls -1 /)
RUN echo $(ls -1 /home)
RUN echo $(ls -1 /app)

EXPOSE 8080

CMD ["flask",  "--app", "main", "run", "--host=0.0.0.0", "--port=8080"]