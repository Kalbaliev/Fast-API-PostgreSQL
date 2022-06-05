FROM python:3.8

WORKDIR /
COPY . .

RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["uvicorn"]
CMD ["main:app","--host=0.0.0.0","--reload"]

