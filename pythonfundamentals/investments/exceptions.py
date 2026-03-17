#Custom Exceptions
class AssetNotFoundException(Exception):
    pass

class InsufficientUnitsException(Exception):
    pass

class DuplicateAssetException(Exception):
    pass