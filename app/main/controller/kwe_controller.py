from flask import request
from flask_restplus import Resource

from app.main.dto.kwe_dto import KWEDTO
from app.main.service.kwe_service import extract_keywords
from app.main.decorator.auth_decorator import auth_required

api = KWEDTO.api


@api.route('')
class KWEResource(Resource):
    @api.response(KWEServiceResponse.Success, 'Successfully extracted keywords')
    @api.response(KWEServiceResponse.Error, 'An error occurred')
    @api.doc('Extract Keywords', security='key')
    @api.expect(KWEDTO.extract_keywords, validate=True)
    @auth_required
    def post(self):
        data = request.json
        if not data or not data['text'] or 'text' not in data:
            return dict(message='Invalid text input.'), 400
        else:
            return extract_keywords(data['text'])
