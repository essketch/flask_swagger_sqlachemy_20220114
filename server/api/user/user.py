import email
from flask_restful import Resource, reqparse
from flask_restful_swagger_2 import swagger

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

        print(f"이메일 : {args['email']}")
        print(f"비밀번호 : {args['password']}")

        return {
            "":""
        }
    
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

        print(f"이메일 : {args['email']}")
        print(f"비밀번호 : {args['password']}")
        print(f"이름 : {args['name']}")
        print(f"연락처 : {args['phone']}")
        
        return {
            "":""
        }