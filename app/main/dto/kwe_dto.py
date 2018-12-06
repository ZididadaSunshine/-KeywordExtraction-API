from flask_restplus import fields, Namespace


class KWEDTO:
    api = Namespace('Keyword-Extraction', description='Keyword Extraction operations.')
    extract_keywords = api.model('Extract Keywords', {
                                 'posts': fields.List(cls_or_instance=fields.String, required=True,
                                                      description='List of posts to get keywords from.')})
