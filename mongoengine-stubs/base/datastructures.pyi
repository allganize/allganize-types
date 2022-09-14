from _typeshed import Incomplete
from bson import DBRef
from collections.abc import Generator

class BaseDict(dict):
    def __init__(self, dict_items, instance, name) -> None: ...
    def __getitem__(self, key, *args, **kwargs): ...
    def __setitem__(self, key, value, *args, **kwargs): ...
    def __delete__(self, *args, **kwargs): ...
    def __delitem__(self, key, *args, **kwargs): ...
    def __delattr__(self, key, *args, **kwargs): ...
    def clear(self, *args, **kwargs): ...
    def pop(self, *args, **kwargs): ...
    def popitem(self, *args, **kwargs): ...
    def setdefault(self, *args, **kwargs): ...
    def update(self, *args, **kwargs): ...

class BaseList(list):
    def __init__(self, list_items, instance, name) -> None: ...
    def __getitem__(self, key, *args, **kwargs): ...
    def __iter__(self): ...
    def __setitem__(self, key, value, *args, **kwargs): ...
    def __delitem__(self, key, *args, **kwargs): ...
    def __setslice__(self, *args, **kwargs): ...
    def __delslice__(self, *args, **kwargs): ...
    def __iadd__(self, other): ...
    def __imul__(self, other): ...
    def append(self, *args, **kwargs): ...
    def extend(self, *args, **kwargs): ...
    def insert(self, *args, **kwargs): ...
    def pop(self, *args, **kwargs): ...
    def remove(self, *args, **kwargs): ...
    def reverse(self, *args, **kwargs): ...
    def sort(self, *args, **kwargs): ...

class EmbeddedDocumentList(BaseList):
    def __init__(self, list_items, instance, name) -> None: ...
    def filter(self, **kwargs): ...
    def exclude(self, **kwargs): ...
    def count(self): ...
    def get(self, **kwargs): ...
    def first(self): ...
    def create(self, **values): ...
    def save(self, *args, **kwargs) -> None: ...
    def delete(self): ...
    def update(self, **update): ...

class StrictDict:
    def __init__(self, **kwargs) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def __contains__(self, key): ...
    def get(self, key, default: Incomplete | None = ...): ...
    def pop(self, key, default: Incomplete | None = ...): ...
    def iteritems(self) -> Generator[Incomplete, None, None]: ...
    def items(self): ...
    def iterkeys(self): ...
    def keys(self): ...
    def __iter__(self): ...
    def __len__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    @classmethod
    def create(cls, allowed_keys): ...

class LazyReference(DBRef):
    def fetch(self, force: bool = ...): ...
    @property
    def pk(self): ...
    document_type: Incomplete
    passthrough: Incomplete
    def __init__(self, document_type, pk, cached_doc: Incomplete | None = ..., passthrough: bool = ...) -> None: ...
    def __getitem__(self, name): ...
    def __getattr__(self, name): ...
