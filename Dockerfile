FROM python:3.10.0-slim-buster

COPY /src .

WORKDIR /src

# Install python packages using `pip`
COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "--server.port", "8501", "main.py"]