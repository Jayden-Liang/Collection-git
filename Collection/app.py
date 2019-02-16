from initial import app, moment
from models import User, Blog

# from itsdangerous import URLSafeSerializer as Serializer
# s = Serializer(app.config['SECRET_KEY'])
# token = s.dumps({'confirm':23})
# print(token)


if __name__ == '__main__':
    app.run(debug=True, port=5000)


