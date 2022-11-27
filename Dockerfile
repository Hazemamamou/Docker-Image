FROM python

WORKDIR /usr/src/application

COPY api_key.py .
COPY bitcoin.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./bitcoin.py"]