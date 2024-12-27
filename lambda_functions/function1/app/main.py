import json
from database.utils.user_model_helper import get_users, create_user


def lambda_handler(event, context):
    email = event.get('email')
    name = event.get('name')

    try:
        user = create_user(email, name)
        users = get_users()
        result = [{
            'id': user.id,
            'email': user.email,
            'name': user.name
        } for user in users]
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }