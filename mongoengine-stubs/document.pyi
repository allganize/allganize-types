"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete
from bson import ObjectId
from mongoengine.base import (BaseDocument, DocumentMetaclass,
                              TopLevelDocumentMetaclass)
from mongoengine.queryset import QuerySetManager

class InvalidCollectionError(Exception): ...

class EmbeddedDocument(BaseDocument, metaclass=DocumentMetaclass):
    my_metaclass: Incomplete
    __hash__: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def to_mongo(self, *args, **kwargs): ...
    def save(self, *args, **kwargs) -> None: ...
    def reload(self, *args, **kwargs) -> None: ...

class Document(BaseDocument, metaclass=TopLevelDocumentMetaclass):
    id: ObjectId
    objects: QuerySetManager
    my_metaclass: Incomplete
    @property
    def pk(self): ...
    @pk.setter
    def pk(self, value): ...
    def __hash__(self) -> int: ...
    def to_mongo(self, *args, **kwargs): ...
    def modify(self, query: Incomplete | None = ..., **update): ...
    def save(
        self,
        force_insert: bool = ...,
        validate: bool = ...,
        clean: bool = ...,
        write_concern: Incomplete | None = ...,
        cascade: Incomplete | None = ...,
        cascade_kwargs: Incomplete | None = ...,
        _refs: Incomplete | None = ...,
        save_condition: Incomplete | None = ...,
        signal_kwargs: Incomplete | None = ...,
        **kwargs
    ): ...
    def cascade_save(self, **kwargs) -> None: ...
    def update(self, **kwargs): ...
    def delete(
        self, signal_kwargs: Incomplete | None = ..., **write_concern
    ) -> None: ...
    def switch_db(self, db_alias, keep_created: bool = ...): ...
    def switch_collection(self, collection_name, keep_created: bool = ...): ...
    def select_related(self, max_depth: int = ...): ...
    def reload(self, *fields, **kwargs): ...
    def to_dbref(self): ...
    @classmethod
    def register_delete_rule(cls, document_cls, field_name, rule) -> None: ...
    @classmethod
    def drop_collection(cls) -> None: ...
    @classmethod
    def create_index(cls, keys, background: bool = ..., **kwargs): ...
    @classmethod
    def ensure_index(
        cls, key_or_list, drop_dups: bool = ..., background: bool = ..., **kwargs
    ): ...
    @classmethod
    def ensure_indexes(cls) -> None: ...
    @classmethod
    def list_indexes(cls): ...
    @classmethod
    def compare_indexes(cls): ...

class DynamicDocument(Document, metaclass=TopLevelDocumentMetaclass):
    my_metaclass: Incomplete
    def __delattr__(self, *args, **kwargs) -> None: ...

class DynamicEmbeddedDocument(EmbeddedDocument, metaclass=DocumentMetaclass):
    my_metaclass: Incomplete
    def __delattr__(self, *args, **kwargs) -> None: ...

class MapReduceDocument:
    key: Incomplete
    value: Incomplete
    def __init__(self, document, collection, key, value) -> None: ...
    @property
    def object(self): ...
