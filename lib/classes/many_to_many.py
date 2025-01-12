class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

        if isinstance(author, Author) and self not in author._articles:
            author._articles.append(self)
        if isinstance(magazine, Magazine) and self not in magazine._articles:
            magazine._articles.append(self)
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            print("It already has the title attribute")
        elif isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        self._magazine = value


class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            print("It already has an attribute name")
        elif isinstance(value, str) and len(value) > 0:
            self._name = value

    def articles(self):
        return self._articles.copy()

    def magazines(self):
        magazines = set()
        for article in self._articles:
            if isinstance(article.magazine, Magazine):
                magazines.add(article.magazine)
        return list(magazines)

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return self._articles.copy()

    def contributors(self):
        authors = set()
        for article in self._articles:
            if isinstance(article.author, Author):
                authors.add(article.author)
        return list(authors)

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            if isinstance(article.author, Author):
                author_counts[article.author] = author_counts.get(article.author, 0) + 1

        frequent_authors = [author for author, count in author_counts.items() if count > 2]
        return frequent_authors if frequent_authors else None
