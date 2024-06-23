import os

def check_for_null_bytes_in_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            for line_number, line in enumerate(f, start=1):
                if b'\x00' in line:
                    print(f'Null byte found in file {file_path} at line {line_number}')
    except Exception as e:
        print(f'Could not read file {file_path}: {e}')

if __name__ == "__main__":
    file_path = 'app_software/models.py'  # Reemplaza con la ruta a tu archivo específico
    check_for_null_bytes_in_file(file_path)

