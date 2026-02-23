# snappy-stubs

PEP 561 type stubs for [python-snappy](https://github.com/andrix/python-snappy).

## Installation

```bash
pip install snappy-stubs
# or
uv add --dev snappy-stubs
```

## Usage

Install alongside `python-snappy`. Type checkers (mypy, pyright) will pick up
the stubs automatically via PEP 561.

```python
import snappy

data: bytes = snappy.compress(b"hello world")
result: bytes = snappy.decompress(data)
```

## Versioning

Versions follow `{python_snappy_version}.{stub_revision}`. For example,
`0.7.3.0` provides stubs for python-snappy 0.7.3, stub revision 0.

## Contributing

Stubs cover the full public API:
- `compress` / `decompress` / `uncompress`
- `StreamCompressor` / `StreamDecompressor`
- `HadoopStreamCompressor` / `HadoopStreamDecompressor`
- `stream_compress` / `stream_decompress`
- `isValidCompressed` / `UncompressError`
- `snappy.snappy_formats` submodule

If python-snappy adds inline types (`py.typed`), this package will be deprecated.
