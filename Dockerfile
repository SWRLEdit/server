FROM python:3.10-slim-buster

WORKDIR ~/swrl-server
ADD . .
RUN python -m pip install -r requirements.txt
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "80"]
