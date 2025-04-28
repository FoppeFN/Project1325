FROM python:3.9.21-slim

WORKDIR /project3

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]



