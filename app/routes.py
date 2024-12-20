from flask import Blueprint, request, jsonify, send_file
import app.__init__ as dd
from config.settings import tables
import app.models as sp
from flask_cors import CORS
import os

# Khởi tạo Blueprint
api_routes = Blueprint("api_routes", __name__)
CORS(api_routes)

# Tải các mô hình
models = []
for name_mode in tables:
    new_model = sp.load_model(name_mode)
    models.append(new_model)

model_manager = dd.ModelManager()

# API trả về nội dung ChatBot.html trực tiếp trên trình duyệt
@api_routes.route('/chatbot_html', methods=['GET'])
def chatbot_html():
    try:
        # Đường dẫn đến thư mục chứa tệp ChatBot.html
        file_path = os.path.join(os.getcwd(), 'chatbot.html')  # Đảm bảo đường dẫn đúng
        # Trả về tệp HTML
        return send_file(file_path)
    except Exception as e:
        print(str(e))
        return jsonify({"message": str(e)}), 500

# API trả về dự đoán đầu
@api_routes.route('/du_doan', methods=['POST'])
def du_doan():
    try:
        data = request.get_json()
        if 'message' not in data:
            return jsonify({"message": "No 'message' field found"}), 400
        
        message = data['message']
        answer = model_manager.final_du_doan(message, models)
        return jsonify({"message": answer}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# API trả về đường dẫn report
@api_routes.route('/lay_report', methods=['GET'])
def lay_report():
    dd.creater_report(models)
    return jsonify({"message_return": "model/report"})

# API trả về dự đoán có lịch sử
@api_routes.route('/du_doan_co_lich_su', methods=['POST'])
def du_doan_co_lich_su():
    try:
        data = request.get_json()
        if 'message' not in data or 'true_label' not in data:
            return jsonify({"message": "No 'message' or 'true_label' field found"}), 400
        
        true_label = data['true_label']
        message = data['message']
        
        answer = model_manager.final_du_doan(message, models)
        return jsonify({"message": answer}), 200
    except Exception as e:
        print (str(e))
        return jsonify({"message": str(e)}), 500
