from settings import *

import random

# enemy_obj = [
#             {
#                 "name": "bat",
#                 "path": "../img/enemy/e001.png"
#             },
#             {
#                 "name": "sneck",
#                 "path": "../img/enemy/e002.png"
#             },
#             {
#                 "name": "サソリ",
#                 "path": "../img/enemy/e003.png"
#             },
#         ]

# print(enemy_obj[0]['name'])
# print(enemy_obj[1]['path'])

def replace_zeros_with_nines(grid, num_replacements):
    """
    リスト内の0をランダムに選択して指定された数を9に置き換える。
    
    Parameters:
        grid (list of list of int): 対象の2次元リスト
        num_replacements (int): 置き換える0の数
    
    Returns:
        list of list of int: 置き換え後のリスト
    """
    # 0の座標を探す
    zero_positions = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 0]
    
    # 指定された数だけランダムに選択
    if num_replacements > len(zero_positions):
        raise ValueError("0の数より置き換える数が多いです。")
    
    random_positions = random.sample(zero_positions, num_replacements)
    
    # 選択された位置を9に置き換える
    for i, j in random_positions:
        grid[i][j] = 9
    
    return grid

# px 
px = -1
py = -1
for i, row in enumerate(TILE['map_01']):
    for j, column in enumerate(row):
        if column == 'P':
            px = j
            py = i
            break
# Pの位置特定
print(f'px:{px} py:{py}')

# NONエリアの計算
px_min = px - NON_ENEMY_AREA
if px_min <= 0: px_min = 0 
px_max = px + NON_ENEMY_AREA
py_min = py - NON_ENEMY_AREA
if py_min <= 0: py_min = 0
py_max = py + NON_ENEMY_AREA

print(f'px_min:{px_min} px_max:{px_max} py_min:{py_min} py_max:{py_max}')

# 配置するエリアの取得
loc_enemy_area = []
for i, row in enumerate(TILE['map_01']):
    row_area = []
    for j, column in enumerate(row):
        if column == '.':
            px = j
            py = i
            if (px > px_min and py > py_min) and (px < px_max and py < py_max):
                row_area.append(1)
            else:
                row_area.append(0) 
        else:
            row_area.append(1)
    loc_enemy_area.append(row_area)

res = replace_zeros_with_nines(loc_enemy_area, MAX_ENEMY_NUM)

for i, row in enumerate(loc_enemy_area):
    print(row)
    for j, column in enumerate(row):
        if column == 9:
            print(f'x:{j} y:{i}に{column}を配置')


