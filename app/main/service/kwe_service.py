from KeywordExtraction.keyword_graph import TKGExtractor


def extract_keywords(corpus):
    print("Recieved data: ")
    print(f"----\n{corpus}\n----")
    extractor = TKGExtractor(corpus)
    return dict(keywords=extractor.extract_n_keywords(n=15)), 200
