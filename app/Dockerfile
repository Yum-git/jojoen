FROM python:3.8

ENV PYTHONBUFFERED 1

RUN mkdir /var/www
# workdirの指定
WORKDIR /var/www
COPY ./ /var/www/

# 依存Pythonライブラリ一覧コピー
COPY requirements.txt ./

# 依存Pythonライブラリインストール
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

 CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]