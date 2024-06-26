"""
This type stub file was generated by pyright.
"""

if False: ...
__all__ = [
    "FileMark",
    "StringMark",
    "CommentMark",
    "YAMLError",
    "MarkedYAMLError",
    "ReusedAnchorWarning",
    "UnsafeLoaderWarning",
    "MarkedYAMLWarning",
    "MarkedYAMLFutureWarning",
]

class StreamMark:
    __slots__ = ...
    def __init__(self, name: Any, index: int, line: int, column: int) -> None: ...
    def __str__(self) -> Any: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class FileMark(StreamMark):
    __slots__ = ...

class StringMark(StreamMark):
    __slots__ = ...
    def __init__(
        self, name: Any, index: int, line: int, column: int, buffer: Any, pointer: Any
    ) -> None: ...
    def get_snippet(self, indent: int = ..., max_length: int = ...) -> Any: ...
    def __str__(self) -> Any: ...
    def __repr__(self) -> Any: ...

class CommentMark:
    __slots__ = ...
    def __init__(self, column: Any) -> None: ...

class YAMLError(Exception): ...

class MarkedYAMLError(YAMLError):
    def __init__(
        self,
        context: Any = ...,
        context_mark: Any = ...,
        problem: Any = ...,
        problem_mark: Any = ...,
        note: Any = ...,
        warn: Any = ...,
    ) -> None: ...
    def __str__(self) -> Any: ...
    def check_append(self, lines: list[str], val: Optional[str]) -> None: ...

class YAMLStreamError(Exception): ...
class YAMLWarning(Warning): ...

class MarkedYAMLWarning(YAMLWarning):
    def __init__(
        self,
        context: Any = ...,
        context_mark: Any = ...,
        problem: Any = ...,
        problem_mark: Any = ...,
        note: Any = ...,
        warn: Any = ...,
    ) -> None: ...
    def __str__(self) -> Any: ...
    def check_append(self, lines: list[str], val: Optional[str]) -> None: ...

class ReusedAnchorWarning(YAMLWarning): ...

class UnsafeLoaderWarning(YAMLWarning):
    text = ...

class MantissaNoDotYAML1_1Warning(YAMLWarning):
    def __init__(self, node: Any, flt_str: Any) -> None: ...
    def __str__(self) -> Any: ...

class YAMLFutureWarning(Warning): ...

class MarkedYAMLFutureWarning(YAMLFutureWarning):
    def __init__(
        self,
        context: Any = ...,
        context_mark: Any = ...,
        problem: Any = ...,
        problem_mark: Any = ...,
        note: Any = ...,
        warn: Any = ...,
    ) -> None: ...
    def __str__(self) -> Any: ...
    def check_append(self, lines: list[str], val: Optional[str]) -> None: ...
