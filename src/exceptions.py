class JsonReplaceException(Exception):
    pass


class ExcelReadException(JsonReplaceException):
    pass


class JsonReadException(JsonReplaceException):
    pass


class MappingException(JsonReplaceException):
    pass
