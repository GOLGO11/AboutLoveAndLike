import os
import re

# get root path
def root_path():
    file_address = os.path.dirname(os.path.realpath(__file__)).replace('\\','/')
    root_path = re.search(r'(.*)common', file_address)
    print(root_path.group(1))
    return root_path.group(1)

def std_yaml_path():
    yaml_path = os.path.join(root_path(), 'data/std/data.yaml')
    if not os.path.exists(yaml_path):
        os.mkdir(yaml_path)
    return yaml_path

def std_crg_path():
    crg_path = os.path.join(root_path(), 'data/std/config.ini')
    if not os.path.exist(crg_path):
        os.mkdir(crg_path)
    return crg_path

def log_path():
    log_path = os.path.join(root_path(), 'log/')
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    return log_path


#if __name__ == '__main__':
 #   root_path()
