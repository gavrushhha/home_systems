FROM python:3.8 AS builder

RUN pip install Flask beautifulsoup4 requests

COPY parser_service.py /app/parser_service.py

WORKDIR /app

FROM python:3.8

RUN pip install Flask pymongo

COPY app/db_service.py /app/db_service.py

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

WORKDIR /app

CMD ["python", "db_service.py"]


#http://127.0.0.1:5000/ 
#http://127.0.0.1:5000/template_example
#http://127.0.0.1:5001/parse
#http://127.0.0.1:5002/save