import random, os, re
from data_config import Config
from glob import glob

class EntryEnemy():
    def __init__(self) -> None:
        self.enemy_setting_path ='../enemy/info'

    def generate_random_enemy(self):
        
        file_paths = glob(os.path.join(os.getcwd(), self.enemy_setting_path, '*.json'))
        file_names = [os.path.basename(path) for path in file_paths]
        choice = random.choice(file_names)
        id = re.search(r'\d+', choice).group()
        # print(id)
        config = Config(id)
        return config.get_json_info()

if __name__ == '__main__':
    instance = EntryEnemy()
    print(instance.generate_random_enemy())


        