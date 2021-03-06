"""
Simple example with a single Document demonstrating how schema can be managed,
including upgrading with reindexing.

Key concepts:

    * setup() function to first initialize the schema (as index template) in
      elasticsearch. Can be called any time (recommended with every deploy of
      your app).

    * migrate() function to be called any time when the schema changes - it
      will create a new index (by incrementing the version) and update the alias.
      By default it will also (before flipping the alias) move the data from the
      previous index to the new one.

    * BlogPost._matches() class method is required for this code to work since
      otherwise BlogPost will not be used to deserialize the documents as those
      will have index set to the concrete index whereas the class refers to the
      alias.
"""
from datetime import datetime
from fnmatch import fnmatch

from elasticsearch_dsl import Document, Date, Text, Keyword, connections

ALIAS = 'test-blog'
PATTERN = ALIAS + '-*'

class BlogPost(Document):
    title = Text()
    published = Date()
    tags = Keyword(multi=True)
    content = Text()

    def is_published(self):
        return self.published and datetime.now() > self.published

    @classmethod
    def _matches(cls, hit):
        # override _matches to match indices in a pattern instead of just ALIAS
        # hit is the raw dict as returned by elasticsearch
        return fnmatch(hit['_index'], PATTERN)

    class Index:
        # we will use an alias instead of the index
        name = ALIAS
        # set settings and possibly other attributes of the index like
        # analyzers
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

def setup():
    """
    Create the index template in elasticsearch specifying the mappings and any
    settings to be used. This can be run at any time, ideally at every new code
    deploy.
    """
    # インデックステンプレートを作る
    index_template = BlogPost._index.as_template(ALIAS, PATTERN)

    # インデックステンプレートを更新(追加)
    index_template.save()

    # 存在しなければ最初のインデックスを構築
    if not BlogPost._index.exists():
        migrate(move_data=False)

def migrate(move_data=True, update_alias=True):
    """
    Upgrade function that creates a new index for the data. Optionally it also can
    (and by default will) reindex previous copy of the data into the new index
    (specify ``move_data=False`` to skip this step) and update the alias to
    point to the latest index (set ``update_alias=False`` to skip).

    Note that while this function is running the application can still perform
    any and all searches without any loss of functionality. It should, however,
    not perform any writes at this time as those might be lost.
    """
    # 現在のタイムスタンプをつけて新しいインデックスを作成する
    next_index = PATTERN.replace('*', datetime.now().strftime('%Y%m%d%H%M%S%f'))

    # get the low level connection
    es = connections.get_connection()

    # create new index, it will use the settings from the template
    es.indices.create(index=next_index)

    if move_data:
        # move data from current alias to the new index
        es.reindex(
            body={"source": {"index": ALIAS}, "dest": {"index": next_index}},
            request_timeout=3600
        )
        # refresh the index to make the changes visible
        es.indices.refresh(index=next_index)

    if update_alias:
        # repoint the alias to point to the newly created index
        es.indices.update_aliases(body={
            'actions': [
                {"remove": {"alias": ALIAS, "index": PATTERN}},
                {"add": {"alias": ALIAS, "index": next_index}},
            ]
        })

if __name__ == '__main__':
    # initiate the default connection to elasticsearch
    connections.create_connection()

    # 空っぽのインスタンスを作る
    setup()

    # BlogPost を作成
    bp = BlogPost(
        _id=0,
        title='Hello World!',
        tags = ['testing', 'dummy'],
        content=open(__file__).read()           # この .py スクリプトをブログと本文として読み込む
    )
    bp.save(refresh=True)

    # 新しくインデックスを作る
    migrate()
