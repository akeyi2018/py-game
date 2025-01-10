import os,json

class Config():
    
    def __init__(self, info_id, **kwargs) -> None:
        self.info_id = info_id 
        # 敵情報を管理するJson
        self.enemy_info = os.path.join(os.getcwd(),'../enemy/info', f'enemy_info_{self.info_id}.json')

        self.name = kwargs.get('name', '未登録')  # 'name'
        self.HP = kwargs.get('HP', 0)  # HP
        self.MP = kwargs.get('MP', 0)  # MP
        self.str = kwargs.get('STR',0)  # 強さ
        self.defe = kwargs.get('DEF',0) # 防御
        self.image = kwargs.get('IMG', 'e_001.png') # image

    def get_json_info(self):
        with open(self.enemy_info, mode='r', encoding='utf-8') as json_file:
            return json.load(json_file)
    
    def set_json_info(self, category_key, category_value):
        try:
            # jsonファイルの読み込み
            with open(self.enemy_info,'r', encoding='cp932') as json_file:
                json_data = json.load(json_file)
                json_data[category_key] = category_value
            # jsonファイルの更新
            with open(self.enemy_info, 'w', encoding='cp932') as json_file:
                json.dump(json_data, json_file, indent=4)
        except:
            print('jsonファイル更新失敗しました。')

    def del_json_info(self, category_value):
        try:
            # jsonファイルの読み込み
            with open(self.enemy_info,'r', encoding='cp932') as json_file:
                json_data = json.load(json_file)
                keys = [k for k, v in json_data.items() if v== category_value]
                if not keys is None:
                    for k in keys:
                        del(json_data[k])
                        
            # jsonファイルの更新
            with open(self.enemy_info, 'w', encoding='cp932') as json_file:
                json.dump(json_data, json_file, indent=4)
        except:
            print('jsonファイル更新失敗しました。')

    def registe_json(self):
        json_data = {'name': self.name,
                     'HP': self.HP,
                     'MP': self.MP,
                     'STR': self.str,
                     'DEF': self.defe,
                     'IMG': self.image}

        with open(self.enemy_info, 'w', encoding='cp932') as json_file:
                json.dump(json_data, json_file, indent=4)

if __name__ == '__main__':
    # 単体テスト
    ins = Config(10005, name='蝙蝠', HP=40, MP=0, STR=10, DEF=4, IMG='e001.png')
    
    ins.registe_json()

    print(ins.get_json_info())

    # ins.set_json_info('category_02','school')
    # d = list(ins.get_json_info().values())
    # print(d)
    # ins.del_json_info()