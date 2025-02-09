class TurnBasedBattle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.current_turn = "player"  # "player" または "enemy"

    def player_turn(self):
        """
        プレイヤーの行動を処理する。
        """
        print(f"{self.player.name}のターンです！")
        # メニューでスキルを選択（仮実装: スキル名を直接入力）
        skill_name = input("使用するスキルを入力してください: ")
        print(self.player.use_skill(skill_name, self.enemy))  # スキルを実行
        self.end_turn()

    def enemy_turn(self):
        """
        敵の行動を処理する。
        """
        print(f"{self.enemy.name}のターンです！")
        # 敵の行動を決定（ランダムにスキルを選択）
        import random
        if self.enemy.skills:
            skill = random.choice(self.enemy.skills)
            print(skill.use(self.enemy, self.player))  # スキルを実行
        self.end_turn()

    def end_turn(self):
        """
        ターンの終了処理を行い、次のターンに移行する。
        """
        if self.current_turn == "player":
            self.current_turn = "enemy"
        else:
            self.current_turn = "player"

    def is_battle_over(self):
        """
        戦闘終了条件をチェックする。
        """
        if self.player.hp <= 0:
            print(f"{self.player.name}は敗北しました...")
            return True
        elif self.enemy.hp <= 0:
            print(f"{self.enemy.name}を倒しました！")
            return True
        return False

    def start_battle(self):
        """
        戦闘を開始する。
        """
        print("戦闘開始！")
        while not self.is_battle_over():
            if self.current_turn == "player":
                self.player_turn()
            else:
                self.enemy_turn()
