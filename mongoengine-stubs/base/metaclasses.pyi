class DocumentMetaclass(type):
    def __new__(cls, name, bases, attrs): ...
    def add_to_class(self, name, value) -> None: ...

class TopLevelDocumentMetaclass(DocumentMetaclass):
    def __new__(cls, name, bases, attrs): ...
    @classmethod
    def get_auto_id_names(cls, new_class): ...

class MetaDict(dict):
    def merge(self, new_options) -> None: ...

class BasesTuple(tuple): ...
