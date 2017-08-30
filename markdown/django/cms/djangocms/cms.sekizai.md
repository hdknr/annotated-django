## settings

~~~py
INSTALLED_APPS = [
    ...
    'sekizai'
]

TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]
~~~
