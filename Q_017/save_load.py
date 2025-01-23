import os, pickle, time

class GameData:
    def __init__(self, save_info=None):
        self.route_path = '../game_data'
        self.save_info = save_info

    # 保存ファイル名を確保（最大10ファイル格納可能)
    def get_new_file(self):
        file = ''
        for count in range(100, 111):
            save_file = f'game_data_{count:03}.pickle'
            full_path = os.path.join(self.route_path, save_file)
            if not os.path.exists(full_path):
                file = full_path
                break
            # 暫定的
            else:
                file = full_path
                break
        return file
    
    def save(self):
        save_file = self.get_new_file()
        with open(save_file,'wb') as f:
            pickle.dump(self.save_info,f)
            print('SUCCESSLY TO SAVE.')

    def load_files(self):
        file = 'game_data_100.pickle'
        save_file = os.path.join(self.route_path, file)
        with open(save_file, 'rb') as f:
            self.save_info = pickle.load(f)
            print(self.save_info)
            print('SUCCESSLY TO LOAD.')

        return self.save_info

