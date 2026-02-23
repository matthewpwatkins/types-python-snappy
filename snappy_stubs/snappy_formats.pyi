"""Type stubs for snappy.snappy_formats."""

from typing import IO, Callable

DEFAULT_FORMAT: str
ALL_SUPPORTED_FORMATS: list[str]

def uvarint(fin: IO[bytes]) -> int: ...
def check_unframed_format(fin: IO[bytes], reset: bool = ...) -> bool: ...
def guess_format_by_header(
    fin: IO[bytes],
) -> tuple[str, Callable[..., None]]: ...
def get_decompress_function(
    specified_format: str,
    fin: IO[bytes],
) -> Callable[..., None]: ...
def get_compress_function(
    specified_format: str,
) -> Callable[..., None]: ...
