from flask import Flask, jsonify, request, session
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from flask_cors import CORS, cross_origin
from models import db, Admin
import bcrypt
from flask_bcrypt import Bcrypt


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

app.secret_key = 'secret key'
app.config['JWT_SECRET_KEY'] = 'this-is-secret-key'


jwt = JWTManager(app)

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
bcrypt = Bcrypt(app)


class Home(Resource):
    def get(self):
        return "Hello world"
    

class AdminRegister(Resource):
    @cross_origin()
    def post(self):
        email = request.json['email']
        company_name = request.json['companyName']
        phone = request.json['phone']
        password = str(request.json['password'])
        confirm_password = str(request.json['confirmPassword'])

        #print(f"Type of password: {type(password)}") 

        admin_exists = Admin.query.filter_by(email=email).first()

        if admin_exists:
            return jsonify({'error': 'Admin already exists'}), 409
        # if email exists, or passwords dont match, do something 
        if password != confirm_password:
            return jsonify({'Error': 'Passwords not matching'})

        hashed_pw = bcrypt.generate_password_hash(password)
        hashed_cpw = bcrypt.generate_password_hash(confirm_password)

        access_token = create_access_token(identity=email)

        new_admin = Admin(
            email=email, 
            company_name=company_name, 
            phone=phone, 
            password=hashed_pw,
            confirm_password=hashed_cpw,
        )
        db.session.add(new_admin)
        db.session.commit()

        return jsonify({
            "id": new_admin.id,
            "email": new_admin.email,
            "company_name": new_admin.company_name,
            'phone': new_admin.phone,
            "access_token": access_token,
            #"user_type":new_admin.user_type
        }),201
    

class AdminLogin(Resource):
    @cross_origin()
    def post(self):
        email = request.json['email']
        password = str(request.json['password'])

        admin = Admin.query.filter_by(email=email).first()

        if admin is None:
            return jsonify({'error': 'Unauthorized'}), 401

        if not bcrypt.check_password_hash(admin.password, password):
            return jsonify({'error': 'Unauthorized, incorrect password'}), 401
        
        access_token = create_access_token(identity=email)
        admin.access_token = access_token


        return jsonify({
            "id": admin.id,
            "email": admin.email,
            "access_token": access_token
            
        }), 201
    

class AdminLogout(Resource):
    def post(self):
        ...

    

api.add_resource(Home, '/')
api.add_resource(AdminRegister, '/adminRegister')
api.add_resource(AdminLogin, '/adminLogin')
api.add_resource(AdminLogout, '/adminLogout')


if __name__ == '__main__':
    app.run(port=5555, debug=True)



