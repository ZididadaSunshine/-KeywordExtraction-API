from unittest import main
from app.main.service.kwe_service import extract_keywords
from test.base.base import BaseTestCase


class KeywordExtractionServiceTest(BaseTestCase):
    def test_kwe_service_success(self):
        response, code = extract_keywords(['I really like this text! It is very nice'])

        self.assertEquals(code, 200)
        self.assertEquals(set(response['keywords']), {'nice'})

    def test_kwe_service_error(self):
        result, code = extract_keywords([])

        self.assertEquals(code, 400)


if __name__ == "__main__":
    main()
