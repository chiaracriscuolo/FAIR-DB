import os

def get_absolute_path(current_file, path_to_save_file ):
    path_current_folder = os.path.dirname(os.path.abspath(current_file))
    return os.path.join(path_current_folder, path_to_save_file)