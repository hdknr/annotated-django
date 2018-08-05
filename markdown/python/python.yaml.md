## XMLをYAMLに変換

- [OrderedDict](http://docs.python.jp/2/library/collections.html#ordereddict) を処理できないので

~~~py
import xmltodict                                                                    
import yaml                                                                         
import json                                                                         
import sys                                                                          

doc = xmltodict.parse(open(sys.argv[1]).read())                                     
doc = json.loads(json.dumps(doc))                                                   

print yaml.safe_dump(doc, allow_unicode=True)  
~~~



## OrderedDict の処理(Pyhhon3)

~~~py
from collections import OrderedDict
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from yaml.representer import SafeRepresenter


Dumper.add_representer(
    OrderedDict, 
    lambda dumper, data: dumper.represent_dict(data.items())
)

Dumper.add_representer(
    str, SafeRepresenter.represent_str)

Loader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    lambda loader, node: OrderedDict(loader.construct_pairs(node))
)


def to_yaml(obj, *args, **kwargs):
    if not 'Dumper' in kwargs:
        kwargs['Dumper'] = Dumper
    if isinstance(obj, Model):
        obj = model_to_dict(obj)
    return yaml.dump(obj, *args, **kwargs)
~~~