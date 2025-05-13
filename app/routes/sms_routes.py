import http
from flask import Blueprint, request, jsonify
from app.services.sms_service import SmsService

sms_bp = Blueprint('sms', __name__)
sms_service = SmsService()


@sms_bp.route('/send_sms', methods=['POST'])
def send_sms():
    try:
        print(f"data for sms: {request.get_json()}")
        sid = sms_service.send_sms(request.get_json())
        return jsonify({"message_sid": sid}), http.HTTPStatus.CREATED

    except ValueError as e:
        return jsonify({"error": str(e)}), http.HTTPStatus.BAD_REQUEST
    except Exception as e:
        return jsonify({"error": "Failed to send SMS", "details": str(e)}), http.HTTPStatus.INTERNAL_SERVER_ERROR
