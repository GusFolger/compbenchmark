# Python Compression Benchmarking
This script benchmarks the compression performance of various formats (`gzip`, `bzip2`, `zstd`, `7z`, and `zip`) for a single file in python. It measures the compressed file size, compression time, and compression efficiency (percentage of the original file size). I needed this for another project but I feel like people may find this useful.

## Features

- Compresses a file into multiple formats:
  - **gzip**
  - **bzip2**
  - **zstd**
  - **7z**
  - **zip**
- Outputs:
  - Compressed file size in MB
  - Time taken for compression in seconds
  - Compression efficiency as a percentage of the original file size
- Easily extendable to support additional formats.

## Requirements
Before using the script, ensure the following dependencies are installed:
- **Python 3.7+**
- Python libraries:
  - `py7zr` (for `.7z` compression): `pip install py7zr`
  - `zstandard` (for `.zst` compression): `pip install zstandard`

## Usage
Define the test file and output directory, then just run the script.
