import psycopg2


class Author:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email


class Article:
    def __init__(self, id, title, topic, content):
        self.id = id
        self.title = title
        self.topic = topic
        self.content = content


class Comment:
    def __init__(self, id, nickname, content, rating):
        self.id = id
        self.nickname = nickname
        self.content = content
        self.rating = rating


class AuthorManager:
    def create_author(self, author):
        connection = psycopg2.connect(user="postgres",
                                      password="123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="lesson_16")
        cur = connection.cursor()
        cur.execute("INSERT INTO author (id_author, name, email) VALUES (%s, %s, %s)",
                    (author.id, author.name, author.email))
        connection.commit()
        cur.close()
        connection.close()

    def get_authors(self):
        connection = psycopg2.connect(user="postgres",
                                      password="123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="lesson_16")
        cur = connection.cursor()
        cur.execute("SELECT * FROM author;")
        authors = cur.fetchall()
        cur.close()
        connection.close()
        return authors


class ArticleManager:
    def create_article(self, article, author):
        connection = psycopg2.connect(user="postgres",
                                      password="123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="lesson_16")
        cur = connection.cursor()
        cur.execute("INSERT INTO article (id_article, title, topic, content, author_id) VALUES (%s, %s, %s, %s, %s)",
                    (article.id, article.title, article.topic, article.content, author.id))
        connection.commit()
        cur.close()
        connection.close()

    def get_articles(self):
        conn = psycopg2.connect(user="postgres",
                                password="123",
                                host="127.0.0.1",
                                port="5432",
                                database="lesson_16")
        cur = conn.cursor()
        cur.execute("SELECT * FROM article;")
        articles = cur.fetchall()
        cur.close()
        conn.close()
        return articles


class CommentManager:
    def create_comment(self, comment, article):
        conn = psycopg2.connect(user="postgres",
                                password="123",
                                host="127.0.0.1",
                                port="5432",
                                database="lesson_16")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO comment (id_comment, nickname, content, rating, aricle_id) VALUES (%s, %s, %s, %s, %s)",
            (comment.id, comment.nickname, comment.content, comment.rating, article.id))
        conn.commit()
        cur.close()
        conn.close()

    def get_comments(self):
        conn = psycopg2.connect(user="postgres",
                                password="123",
                                host="127.0.0.1",
                                port="5432",
                                database="lesson_16")
        cur = conn.cursor()
        cur.execute("SELECT * FROM comment;")
        comments = cur.fetchall()
        cur.close()
        conn.close()
        return comments


author2 = Author(2, 'Sergey', 'sergey@gmail.com')
article2 = Article(2, 'sergey_title', 'sergey_topic', 'sergey_content')
comment2 = Comment(1, 'commenter', 'bla-bla-bla', 4)
author_manager = AuthorManager()
# author_manager.create_author(author2)
print(author_manager.get_authors())
article_manager = ArticleManager()
# article_manager.create_article(article2, author2)
print(article_manager.get_articles())
comment_manager = CommentManager()
# comment_manager.create_comment(comment2, article2)
print(comment_manager.get_comments())
