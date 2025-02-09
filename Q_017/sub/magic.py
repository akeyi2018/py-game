from sub.player_data import *


class Magic:
    def __init__(self, name, cost, effect):
        self.name = name  # 魔法の名前
        self.cost = cost  # 消費MP
        self.effect = effect  # 魔法の効果（関数）

    def execute(self, target):
        """魔法を実行する"""
        if self.effect:
            self.effect(target)

class Magic_maneger:
    def __init__(self, parent):
        self.parent = parent
        self.all_magic_list = [
            ("ホイミ", self.hoimi_effect),  # 名前, 消費MP, 効果
            ("メラ", self.mera_effect),
            ("ヒャド", self.hyado_effect),
        ]
        self.magic_table = {
            "ホイミ": 1,
            "メラ": 5,
            "ヒャド": 8
        }

        self.magic_name_list = []
        self.get_magic_name()

        self.current_magic = []
        self.append_magic()

    # 魔法名を取得
    def get_magic_name(self):
        for k, v in self.magic_table.items():
            if LV >= v:
                self.magic_name_list.append(k)

    # 魔法を装備
    def append_magic(self):
        for name in self.magic_name_list:
            for i, (m, _) in enumerate(self.all_magic_list):
                if name in m:
                    self.current_magic.append(self.all_magic_list[i])

    def hoimi_effect(self):
        # cost
        cost = 5
        if cost <= self.parent.status.view_status['MP']:
            self.parent.status.view_status['MP'] -= cost
            self.parent.status.view_status['HP'] += 20  # 例: HPを20回復
            if self.parent.status.view_status['HP'] >= self.parent.status.view_status['MAX_HP']:
                self.parent.status.view_status['HP'] = self.parent.status.view_status['MAX_HP']
            msg = f"  {self.parent.status.view_status['name']}はホイミを唱えました。"
            self.parent.msg_que.put(msg)
            msg = f"  {self.parent.status.view_status['name']}のHPが20回復した！"
            self.parent.msg_que.put(msg)
            self.parent.menu.show_main_commands()
        else:
            print("MPが足りない！")

    def mera_effect(self, target):
        target.hp -= 10  # 例: 敵に10ダメージ
        print(f"{target.name}に10のダメージ！")

    def hyado_effect(self, target):
        target.hp -= 12  # 例: 敵に12ダメージ
        print(f"{target.name}に12のダメージ！")


class Model:
    def __init__(self):
        self.hp = 50
        self.name = 'takeshi'
        self.lv = 7
        self.magic_table = {
            "ホイミ": 1,
            "メラ": 5,
            "ヒャド": 8
        }
        self.magic_name_list = []
        self.get_magic_name()
        self.magic_list = []

    # 魔法名を取得
    def get_magic_name(self):
        for k, v in self.magic_table.items():
            if self.lv >= v:
                self.magic_name_list.append(k)
    # 魔法を装備
    def append_magic(self, magic_list):
        for name in self.magic_name_list:
            for m in magic_list:
                if name in m.name:
                    self.magic_list.append(m)


if __name__ == '__main__':
    mm = Magic_maneger()

    target = Model()
    
    print(target.hp)

    target.append_magic(mm.magic_list)
    num = 2
    try:
        print(f'{target.name}が{target.magic_name_list[num]}を唱えました。')
        target.magic_list[num].execute(target)

        print(target.hp)
    except:
        print(f'{target.name}はまだその呪文を覚えていません。')
