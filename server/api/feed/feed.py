
from flask_restful import Resource, reqparse
from flask_restful_swagger_2 import swagger
from server import db
from server.model import Feeds



post_parser = reqparse.RequestParser()
post_parser.add_argument('user_id', type=int, required=True, location='form')
post_parser.add_argument('lecture_id', type=int, required=True, location='form')
post_parser.add_argument('content', type=str, required=True, location='form')


class Feed(Resource):
    @swagger.doc({
        'tags' : ['feed'],
        'description' : '게시글 등록',
        'parameters' : [
            {
            'name' : 'user_id',
            'description' : '작성자',
            'in' : 'formData',
            'type' : 'integer',
            'required' : True
            },
            {
            'name' : 'lecture_id',
            'description' : '강의',
            'in' : 'formData',
            'type' : 'integer',
            'required' : True
            },
            {
            'name' : 'content',
            'description' : '글 내용',
            'in' : 'formData',
            'type' : 'string',
            'required' : True
            },

        ],
        'responses': {

            '200' : {
                'description' : '게시글 등록 성공'
            },

            '400' : {
                'description' : '게시글 등록 실패'
            }
        }
    })
    def post(self):
        """게시글 등록"""
        args = post_parser.parse_args()
        new_feed = Feeds()
        new_feed.user_id = args['user_id']
        new_feed.lecture_id = args['lectur_id']
        new_feed.content = args['content']

        db.session.add(new_feed)
        db.session.commit()

        return {
            'code' : 200,
            'message' : '게시글 등록 성공',
            'data' : {
                'feed' : new_feed.get_data_object()
            }
        }
    
    @swagger.doc({
        'tags' : ['feed'],
        'description' : '게시글 목록 조회',
        'parameters' : [

        ],
        'responses': {

            '200' : {
                'description' : '게시글 조회 성공'
            },

            '400' : {
                'description' : '게시글 조회 실패'
            }
        }
    })
    def get(self) :
        """게시글 최신순 조회"""
        feed_data_arr = Feeds.query.order_by(Feeds.created_at.desc()).all()
        feeds = [row.get_data_object() for row in feed_data_arr]


        return {
            'code' : 200,
            'message' : '모든 게시글 조회',
            'data' : {
                'feeds' : feeds
            }
        }