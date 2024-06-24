import os
import subprocess


def download_files(config_file, file_dir):
    with open(config_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        line = line.split(maxsplit=1)
        url = line[0]
        filename = None if len(line) <= 1 else line[1]

        extensions = {'checkpoints': '.safetensors',
                      'loras': '.safetensors'}
        path = '/workspace/ComfyUI/models/'
        absolute_path = path + file_dir + '/'
        if filename:
            absolute_path += filename + extensions[file_dir]
            command = f'wget -c {url} -O {absolute_path}'
        else:
            command = f'wget -c {url} -P {absolute_path}'
        subprocess.run(command, shell=True)
        print(f"Downloaded {url} to {absolute_path}")


if __name__ == "__main__":
    config_dir = 'models'
    for config_file in os.listdir(config_dir):
        if config_file.endswith('.txt'):
            config_path = os.path.join(config_dir, config_file)
            download_files(config_path, config_file[0:-4])