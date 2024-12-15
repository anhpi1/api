import requests
import time
import hashlib
import hmac
import base64
import json

# Thông tin của bạn từ iFLYTEK
APPID = 'ga56429a'
APIKey = '5e35219aaaba629560bec5cdf9f1b1a5'
APISecret = '6a60eb3b1bf9cc6ba02ab9fedc9b399a'

# Hàm tạo chữ ký (HMAC-SHA256)
def create_signature(text, api_key, api_secret):
    curtime = str(int(time.time()))  # Thời gian hiện tại (unixtimestamp)
    param = {
        "from": "zh",  # Ngôn ngữ nguồn
        "to": "en",    # Ngôn ngữ đích
        "text": text   # Văn bản cần dịch
    }
    param_json = json.dumps(param)  # Chuyển tham số thành chuỗi JSON
    checksum = hashlib.md5((api_key + curtime + param_json).encode('utf-8')).hexdigest()  # Kiểm tra checksum
    return curtime, checksum, param_json

def translate_text(text):
    url = 'https://api.xfyun.cn/v1/service/v1/translator'  # Đảm bảo URL chính xác
    
    # Tạo chữ ký và các tham số
    curtime, checksum, param_json = create_signature(text, APIKey, APISecret)

    # Tạo header yêu cầu
    headers = {
        'X-Param': base64.b64encode(param_json.encode('utf-8')).decode('utf-8'),
        'X-Appid': APPID,
        'X-CurTime': curtime,
        'X-CheckSum': checksum,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
    }

    # Gửi yêu cầu POST
    response = requests.post(url, headers=headers, data={'text': text})

    # Kiểm tra mã trạng thái HTTP
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.text)  # In chi tiết thông báo lỗi
        return None

    # Kiểm tra và phân tích dữ liệu trả về
    try:
        result = response.json()
    except ValueError:
        print("API trả về dữ liệu không phải JSON")
        print(response.text)
        return None

    # Trả về kết quả
    if result['code'] == '0':
        return result['data']['trans_result']
    else:
        return f"Error: {result['desc']}"

# Ví dụ sử dụng
if __name__ == "__main__":
    text_to_translate = "你好，世界"  # Ví dụ: văn bản cần dịch (tiếng Trung)
    translated_text = translate_text(text_to_translate)
    if translated_text:
        print("Translated text:", translated_text)

# Ví dụ sử dụng
if __name__ == "__main__":
    text_to_translate = "你好，世界"  # Ví dụ: văn bản cần dịch (tiếng Trung)
    translated_text = translate_text(text_to_translate)
    print("Translated text:", translated_text)
