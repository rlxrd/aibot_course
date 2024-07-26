FROM python

WORKDIR /app

COPY reqs.txt .

RUN pip install --no-cache-dir -r reqs.txt

COPY . .

CMD ["python", "run.py"]
