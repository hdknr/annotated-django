# callableなどが指定されたマイグレーション

- [Django の deconstruct と deconstructible について](http://qiita.com/tell-k/items/73bcfdf22badf1cfa04a)

- [Field deconstruction](https://docs.djangoproject.com/ja/1.9/howto/custom-model-fields/#field-deconstruction) - Fieldでは `deconstruct` メソッドの実装が必要
- Validator では deconstructible デコレータの付与と、 `__eq__` メソッドの実装が必要

## deconstruct

- [deconstructible](https://github.com/hdknr/annotated-django/commit/a8963f3b9a3bbcc49ab4390cad7b920f33f6adbc)

- [Adding a deconstruct() method](https://docs.djangoproject.com/ja/1.9/topics/migrations/#custom-deconstruct-method)

- `deconstruct` がないとクラスをシリアライズできない
- `deconstruct` は  `(path, args, kwargs)` タプルを返す

- path:  `myapp.custom_things.MyClass`
- args, kwargs: `__init__(*args, **kwargs)`
