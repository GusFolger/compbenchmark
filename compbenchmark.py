import os
import time
import gzip
import bz2
import py7zr
import zstandard
import zipfile

# Set file paths
original_file = fr""
output_dir = fr""
original_file_size = os.path.getsize(original_file)
os.makedirs(output_dir, exist_ok=True)
results = []

# Benchmark Function
def benchmark_compression(format_name, compression_function):
    start_time = time.time()
    compressed_file = compression_function()
    end_time = time.time()
    file_size = os.path.getsize(compressed_file)
    compression_time = end_time - start_time
    results.append((format_name, file_size, compression_time))
    return compressed_file

# ZIP compression
def compress_zip():
    output_path = os.path.join(output_dir, "test_file.zip")
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.write(original_file, arcname=os.path.basename(original_file))
    return output_path

# GZIP compression
def compress_gzip():
    output_path = os.path.join(output_dir, "test_file.gz")
    with open(original_file, 'rb') as f_in:
        with gzip.open(output_path, 'wb') as f_out:
            f_out.write(f_in.read())
    return output_path

# BZIP2 compression
def compress_bzip2():
    output_path = os.path.join(output_dir, "test_file.bz2")
    with open(original_file, 'rb') as f_in:
        with bz2.open(output_path, 'wb') as f_out:
            f_out.write(f_in.read())
    return output_path

# Zstandard compression
def compress_zstd():
    output_path = os.path.join(output_dir, "test_file.zst")
    cctx = zstandard.ZstdCompressor()
    with open(original_file, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            f_out.write(cctx.compress(f_in.read()))
    return output_path

# 7z compression
def compress_7z():
    output_path = os.path.join(output_dir, "test_file.7z")
    with py7zr.SevenZipFile(output_path, 'w') as archive:
        archive.write(original_file, arcname=os.path.basename(original_file))
    return output_path

if __name__ == "__main__":
    print("")
    print("Compression Benchmarks")
    original_file_size_mb = original_file_size / (1024 * 1024)
    print(f"Original File Size: {original_file_size_mb:.2f} MB")
    print("")
    benchmark_compression("ZIP", compress_zip)
    benchmark_compression("GZIP", compress_gzip)
    benchmark_compression("BZIP2", compress_bzip2)
    benchmark_compression("Zstandard", compress_zstd)
    benchmark_compression("7z", compress_7z)

    print(f"{'Format':<10} {'Size (MB)':<15} {'Time (seconds)':<15} {'% of Original':<15}")
    for format_name, file_size, compression_time in results:
        file_size_mb = file_size / (1024 * 1024)  # Convert bytes to megabytes
        percentage = (file_size / original_file_size) * 100  # Calculate percentage
        print(f"{format_name:<10} {file_size_mb:<15.2f} {compression_time:<15.3f} {percentage:<15.2f}")
    print("")


