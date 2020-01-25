# Enum

## choices -> Enum

~~~python
class Item(models.Model, methods.Item):
    division = models.IntegerField(
        '部門', choices=DIVISION_CHOICES,)

~~~

~~~graphql
query {
  __type(name: "ItemDivision") {
	kind
    enumValues {
      name
      description
    }
  }
}
~~~

~~~json
{
  "data": {
    "__type": {
      "kind": "ENUM",
      "enumValues": [
        {
          "name": "A_10",
          "description": "加工"
        },
        {
          "name": "A_20",
          "description": "デイリー"
        },
        {
          "name": "A_30",
          "description": "菓子"
        },
        {
          "name": "A_40",
          "description": "青果"
        }
      ]
    }
  }
}
~~~
