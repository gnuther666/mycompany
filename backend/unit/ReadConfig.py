import os
import yaml

def check_conf(f):
    def warps(*argv, **kwargs):
        obj = argv[0]
        if obj.config_path == '':
            obj.config_path = os.path.join(os.path.split(__file__)[0], '..', 'Config', 'local.yaml')
            print(obj.config_path)
            obj.read_file()
        ret = f(*argv, **kwargs)
        print(ret)
        return ret
    return warps


class ReadConfig:
    def __init__(self):
        self.config_path = ''
        self.datas = dict()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(ReadConfig, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def read_file(self):
        with open(self.config_path, 'r') as file:
            data = file.read()
            result = yaml.load(data, Loader=yaml.FullLoader)
            self.datas = result

    @check_conf
    def get_db_config(self):
        tmp = self.datas['DefaultDB']
        return tmp

    @check_conf
    def get_run_server_config(self):
        tmp = self.datas['SysConfig']
        return tmp


