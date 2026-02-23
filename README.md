# types-python-snappy

PEP 561 type stubs for [python-snappy](https://github.com/andrix/python-snappy).

## Installation

```bash
pip install types-python-snappy
# or
uv add --dev types-python-snappy
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

Versions match the stubbed python-snappy release. `0.7.3.0` stubs
python-snappy 0.7.3.

## Coverage

- `compress` / `decompress` / `uncompress`
- `StreamCompressor` / `StreamDecompressor`
- `HadoopStreamCompressor` / `HadoopStreamDecompressor`
- `stream_compress` / `stream_decompress`
- `isValidCompressed` / `UncompressError`
- `snappy.snappy_formats` submodule

If python-snappy adds inline types (`py.typed`), this package will be deprecated.
