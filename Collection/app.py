from initial import app

# from itsdangerous import URLSafeSerializer as Serializer
# s = Serializer(app.config['SECRET_KEY'])
# token = s.dumps({'confirm':23})
# print(token)


if __name__ == '__main__':
    app.run(debug=True, port=5000)


