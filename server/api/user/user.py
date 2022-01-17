
from flask_restful import Resource, reqparse
from flask_restful_swagger_2 import swagger
from server.model import Users
from server import db

#파라미터 받기
post_parser = reqparse.RequestParser()
post_parser.add_argument('email', type=str, required=True, location='form')
post_parser.add_argument('password', type=str, required=True, location='form')
put_parser = reqparse.RequestParser()
put_parser.add_argument('email', type=str, required=True, location='form')
put_parser.add_argument('password', type=str, required=True, location='form')
put_parser.add_argument('name', type=str, required=True, location='form')
put_parser.add_argument('phone', type=str, required=True, location='form')


class User(Resource):

    @swagger.doc({
        'tags' : ['user'],
        'description' : '사용자 정보 조회',
        'parameters' : [
            #dict로 파라미터 명시
        ],
        'responses' : {
            '200' : {
                'description' : '사용자 정보 조회 성공'
            },
            '400' : {
                'description' : '사용자 정보 조회 실패'
            }
        }
    })
    def get(self):
        """사용자 정보 조회"""
        return {
            "":""
        }
    


    @swagger.doc({
        'tags' : ['user'],
        'description' : '로그인',
        'parameters' : [
            {
            'name' : 'email',
            'description' : '로그인용 이메일',
            'in' : 'formData',
            'type' : 'string',
            'required' : True
            },
            {
            'name' : 'password',
            'description' : '로그인용 비밀번호',
            'in' : 'formData',
            'type' : 'string',
            'required' : True
            },
        ],
        'responses' : {
            '200' : {
                'description' : '로그인 성공'
            },
            '400' : {
                'description' : '로그인 실패'
            }
        }
    })
    def post(self):
        """로그인""" 
        args = post_parser.parse_args()

        #filter는 성능에 영향을 주지 않음
        login_user = Users.query\
            .filter(Users.email == args['email'])\
            .first()
        
        if login_user == None:
            return{
                'code' : 400,
                'message' : '잘못된 이메일 입니다.',
            }, 400

        
        if login_user.password == args['password']:
            return {
                'code' : 200,
                'message' : '로그인 성공',
                'data' : {
                    'user' : login_user.get_data_object()
                }
            }
        else:
            return {
                'code' : 400,
                'message' : '로그인 실패',
            }, 400

    
    @swagger.doc({
        'tags' : ['user'],
        'description' : '회원가입',
        'parameters' : [
            {
            'name' : 'email',
            'description' : '회원가입용 이메일',
            'in' : 'formData',
            'type' : 'string',
            'required' : True
            },
            {
            'name' : 'password',
            'description' : '회원가입용 비밀번호',
            'in' : 'formData',
            'type' : 'string',
            'required' : True
            },
            {
            'name' : 'name',
            'description' : '회원가입용 이름',
            'in' : 'formData',
            'type' : 'string',
            'required' : True
            },
            {
            'name' : 'phone',
            'description' : '회원가입용 연락처',
            'in' : 'formData',
            'type' : 'string',
            'required' : True
            },
        ],
        'responses' : {
            '200' : {
                'description' : '회원가입 성공'
            },
            '400' : {
                'description' : '회원가입 실패'
            }
        }
    })
    def put(self):
        """회원가입"""
        args = put_parser.parse_args()

        new_user = Users()
        new_user.email = args['email']
        new_user.password = args['password']
        new_user.name = args['name']
        new_user.phone = args['phone']

        db.session.add(new_user)
        db.session.commit()

        return {
            "code" : 200,
            'message' : '회원가입 성공',
            'data' : {
                'user' : new_user.get_data_object()
            }
        }

    # def delete(self):
    #     """회원 삭제"""
    #     pass