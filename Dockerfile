# Bắt đầu từ image Python 3.10
FROM python:3.10-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /


# Sao chép tệp yêu cầu và mã nguồn vào container
COPY app app
COPY config config
COPY chatbot.html chatbot.html
COPY main.py main.py
COPY requirements.txt requirements.txt

# Cài đặt các thư viện Python từ requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Mở cổng mà ứng dụng sẽ chạy (giả sử ứng dụng sử dụng cổng 5000)
EXPOSE 5000

# Lệnh để chạy ứng dụng (Giả sử bạn đang sử dụng Flask)
CMD ["python", "main.py"]
