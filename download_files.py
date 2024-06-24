import os
import subprocess


def download_files(config_file):
    with open(config_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        line = line.split(maxsplit=1)
        url = line[0]
        file_dir = line[1]
        filename = None if len(line) <= 2 else line[2]

        extensions = {'c': '.safetensors'}
        directories = {'c': 'checkpoints'}
        path = '/workspace/ComfyUI/models/'
        absolute_path = file_dir + directories[file_dir]
        if filename:
            absolute_path += filename + extensions[file_dir]
            command = f'wget -c {url} -O {absolute_path}'
        else:
            command = f'wget -c {url} -P {absolute_path}'
        subprocess.run(command, shell=True)
        print(f"Downloaded {url} to {absolute_path}")


if __name__ == "__main__":
    config_file = 'download_config.txt'
    download_files(config_file)
