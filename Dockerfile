FROM python:3.8.10

WORKDIR /app

RUN echo $(ls -1 /)
RUN echo $(ls -1 /app)

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["flask",  "--app", "main", "run", "--host=0.0.0.0", "--port=8080"]