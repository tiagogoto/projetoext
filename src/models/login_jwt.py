from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt 


def check_jwt():
    user_id = get_jwt_identity()
    user = user.query.filter_by(id=user_id).first()
    if user:
        return jsonify({'message': 'User found', 'name': user.name})
    else:
        return jsonify({'message':'User not found'}), 404