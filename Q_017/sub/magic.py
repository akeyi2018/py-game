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
    def __init__(self):
        self.magic_list = [
            Magic("ホイミ", 5, self.hoimi_effect),  # 名前, 消費MP, 効果
            Magic("メラ", 7, self.mera_effect),
            Magic("ヒャド", 8, self.hyado_effect),
        ]

    def hoimi_effect(self, target):
        target.hp += 20  # 例: HPを20回復
        print(f"{target.name}のHPが20回復した！")

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
