class Evaluator:

    @staticmethod
    def zip_evaluate(coefs: list[float], words: list[str]) -> float:
        try:
            return sum(len(word) * coef for word, coef in zip(words, coefs, strict=True))
        except (ValueError, TypeError):
            return -1

    @staticmethod
    def enumerate_evaluate(coefs, words: list[str]):
        try:
            if len(words) != len(coefs):
                return -1
            result = 0
            for i, word in enumerate(words):
                result += len(word) * coefs[i]
            return result
        except (ValueError, TypeError):
            return -1