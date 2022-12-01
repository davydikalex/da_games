FROM python

WORKDIR /bot

COPY . .

COPY requirements.txt .
RUN python -m pip install --no-cache-dir --requirement requirements.txt

COPY . .

CMD ["run.py"]

#docker build -t *name* .