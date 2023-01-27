import yaml
import sys


def config_read(config_path):
    with open(config_path) as file:
        try:
            config = yaml.safe_load(file)
            print('YML read | Completed')
            return config
        except yaml.YAMLError:
            print('YML read | Error')


def config_dump(config_data, config_path):
    with open(config_path, 'w') as file:
        try:
            yaml.safe_dump(config_data, file)
            print('YML dump | Completed')
        except yaml.YAMLError:
            print('YML dump | Error')
