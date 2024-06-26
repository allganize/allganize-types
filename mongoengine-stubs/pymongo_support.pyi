"""
This type stub file was generated by pyright.
"""

"""
Helper functions, constants, and types to aid with PyMongo v2.7 - v3.x support.
"""
_PYMONGO_37 = ...
PYMONGO_VERSION = ...
IS_PYMONGO_GTE_37 = ...
def count_documents(collection, filter):
    """Pymongo>3.7 deprecates count in favour of count_documents"""
    ...

def list_collection_names(db, include_system_collections=...): # -> list[Any]:
    """Pymongo>3.7 deprecates collection_names in favour of list_collection_names"""
    ...

