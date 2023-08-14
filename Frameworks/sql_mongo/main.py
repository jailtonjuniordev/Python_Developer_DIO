def sqlite():
    from sqlalchemy.orm import declarative_base
    from sqlalchemy import Column, Integer, String, ForeignKey

    Base = declarative_base()

    __table_name__ = 'user_account'

    id = Column(Integer, primary_key = True)


def mongodb():
    import pymongo as pyM
    import datetime
    import pprint


    # Criação da Conexão
    client = pyM.MongoClient('mongodb+srv://JailtonDEV:iARRJiNpsj3FjA27@jjdev.blzgune.mongodb.net/?retryWrites=true&w=majority')


    # Criação do Banco de dados
    db = client.blog

    # Criação da Tabela/Coleção
    posts = db.posts

    # Criação dos dados para inserção no estilo insert_many
    new_posts = [
        {
            "author": "Jailton",
            "text": "minha primeira aplicação mongoDB com python",
            "tags": ["mongodb", "python3", "intelliJ IDEA", "pymongo"],
            "date": datetime.datetime.utcnow()
        },
        {
            "author": "Lohayne",
            "text": "Outro Post",
            "title": "um titulo",
            "tags": ["mongodb", "python3", "intelliJ IDEA", "pymongo"],
            "date": datetime.datetime.utcnow()
        }
    ]

    # Inserção dos dados da lista acima
    posts.insert_many(new_posts)

    # For para impressão dos dados na tabela/coleção posts
    for post in posts.find():
        pprint.pprint(post)


if __name__ == '__main__':
    mongodb()
