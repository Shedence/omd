from collections import defaultdict


class CountVectorizer:
    """
    Класс для представления Терм-документная матрицы.
    ...
    Атрибуты
    --------
    self.words : list
    Методы
    ------
    fit_transform (self, corpus)
    Возвращает вектора вхождения слов в различные
    предложения
    get_features_name
    Вовзращает все слова, которые могут вообще
    входить
    """
    def __int__(self) -> None:
        """
        Функция инициализации
        """
        self.words = []

    def fit_transform(self, corpus) -> list:
        """
        Функция преобразования массива в
        матрицу, которая считает слова,
        а так же формирования массива всех слов,
        которые входят.
        Функция вовзращает матрицу подсчета
        """
        count_matrix = []
        text = (' '.join(corpus)).split()
        words = defaultdict(int)
        for names in text:
            names = names.lower()
            words[names] += 1
        self.words = list(words.keys())
        for sentence in corpus:
            counter = dict.fromkeys(self.words, 0)
            for words in sentence.split():
                words = words.lower()
                counter[words] += 1
            count_matrix.append(list(counter.values()))
        return count_matrix

    def get_feature_names(self):
        """
        Функция, которая возвращает
        массив всех слов, которые
        входят
        """
        try:
            input_features = self.words
        except AttributeError:
            return None
        return input_features


if __name__ == '__main__':
    sen = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(sen)
    print(vectorizer.get_feature_names())
    print(matrix)
