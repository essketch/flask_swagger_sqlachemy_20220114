from flask_restful import Resource
from flask_restful_swagger_2 import swagger

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
            #dict로 파라미터 명시
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
        return {
            "":""
        }
    
    @swagger.doc({
        'tags' : ['user'],
        'description' : '회원가입',
        'parameters' : [
            #dict로 파라미터 명시
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
        return {
            "":""
        }