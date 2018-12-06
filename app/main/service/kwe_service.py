from KeywordExtraction.keyword_graph import TKGExtractor


class KWEServiceResponse:
    Success = 200
    Error = 400


def extract_keywords(data):
    if not data or 'text' not in data:
        return KWEServiceResponse.Error
    else:
        print("Recieved data: ")
        print(f"----\n{data['text']}\n----")
        extractor = TKGExtractor(data['text'])
        return dict(keywords=extractor.extract_n_keywords(n=15)), KWEServiceResponse.Success
