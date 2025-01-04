# 追加モンスター生成

# 必要な情報
# 1.Playerの位置（モンスター遭遇時）
# 2.モンスター配置していない空のMapデータ（Blockは必要） OK
# 3.モンスター配置情報（こちらはPlayerに倒されるため、変動情報となる）

# 処理ロジック
# 1.空のMapデータにモンスター配置情報を更新する OK
# 2.Playerの位置情報を配置しないエリアを更新する 
# 3.モンスターを１つ追加生成し、配置する


# 敵の生成
#　初期の生成はMapクラスで
#　追加生成はPlayerクラスでEnemyクラスをコールして生成する
from settings import * 
import random

def create_base_map():
    base_map = []

    for i, row in enumerate(TILE['map_01']):
        row_area = []
        for j, column in enumerate(row):
            if column == 'B':
                row_area.append(1) 
            else:
                row_area.append(0)
        base_map.append(row_area)

    return base_map


mob_pos_info = [[6,3],[16,3],[17,3],[10,4],[3,6]]

player_pos_info = [6,2]

def cal_mob_area(mob_pos_info, max_y, max_x):

    all_list = []
    for px, py in mob_pos_info:
        print(f'mob info: {px},{py}')

        # NONエリアの計算
        px_min = max(0, px - MOB_AREA)
        px_max = min(max_x - 1, px + MOB_AREA)
        py_min = max(0, py - MOB_AREA)
        py_max = min(max_y - 1, py + MOB_AREA)

        mob_area = []
        for p_y in range(py_min, py_max + 1):
            for p_x in range(px_min, px_max + 1):
                mob_area.append([p_x, p_y])  # 各座標をリストに追加
        
        all_list.extend(mob_area)
    return all_list


# モンスターを配置する関数
def place_monsters(map_data, mob_pos_info, num):
    for x, y in mob_pos_info:
        if map_data[y][x] == 0:  # 配置可能な場所
            map_data[y][x] = num  # モンスターを配置（2はモンスターを表す）
        else:
            # print(f"座標 ({x}, {y}) にモンスターを配置できません。")
            pass
    return map_data

def place_player(max_x, max_y):
    player_pos_info = [16,8]
    px = player_pos_info[0]
    py = player_pos_info[1]

    px_min = px - NON_ENEMY_AREA
    if px_min <= 0: px_min = 0 
    
    px_max = px + NON_ENEMY_AREA
    if px_max >= max_x: px_max = max_x
    py_min = py - NON_ENEMY_AREA
    
    if py_min <= 0: py_min = 0
    
    py_max = py + NON_ENEMY_AREA
    if py_max >= max_y: py_max = max_y
    
    player_area = []
    for p_y in range(py_min, py_max+1):
        temp = []
        for p_x in range(px_min, px_max+1):
            temp.append([p_x, p_y])
        player_area.extend(temp) 

    return player_area

map_data = create_base_map()
max_map_y = len(map_data)
max_map_x = len(map_data[0])

res_mob = cal_mob_area(mob_pos_info, max_map_y, max_map_x)

# for row in res_mob:
#     print(row)



# モンスターを配置
updated_map = place_monsters(map_data, res_mob, 9)

# p = place_player(max_map_y, max_map_x)
# # Playerを配置
# updated_map = place_monsters(updated_map, p, 3)

# zero_positions = [(i, j) for i, row in enumerate(updated_map) for j, val in enumerate(row) if val == 0]
# random_positions = random.sample(zero_positions, 1)
# for i, j in random_positions:
#         updated_map[i][j] = 9


# # 結果を表示
for row in updated_map:
    print(row)



