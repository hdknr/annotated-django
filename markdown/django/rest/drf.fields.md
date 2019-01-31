# [フィールド](https://www.django-rest-framework.org/api-guide/fields/)

## ベースフィールド([Field](https://github.com/encode/django-rest-framework/blob/master/rest_framework/fields.py#L309))

| Name             | Default             | メモ            |
| ---------------- | ------------------- | -----------------|
| read_only        | False               |                  |
| write_only       | False               |                  |
| required         | True                |                  |
| default          | True                | [set_context()](https://www.django-rest-framework.org/api-guide/validators/#using-set_context) |
| allow_null       | False               |                  |
| source           |                     | `source='*'`                 |
| validators       |                     | 検証関数(`list`)               |
| error_messages   |                     | メッセージ(`dict`)             |
| label            |                     | (`str`)                      |
| help_text        |                     | (`str`)                      |
| initial          |                     | 初期値                        |
| style            |                     | レンダラパラメータ(`dict`)      |
