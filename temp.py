import os

def print_leaf_files(root_dir, base_dir="", indent=""):
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        # Kiểm tra nếu là file, in ra đường dẫn tương đối
        if os.path.isfile(item_path):
            relative_path = os.path.relpath(item_path, base_dir)
            print(convert_path_to_unix("COPY " + indent + relative_path + " " +  indent + relative_path))
        elif os.path.isdir(item_path):
            # Nếu là thư mục, tiếp tục đệ quy
            print_leaf_files(item_path, base_dir, indent)

def convert_path_to_unix(path):
    """
    Chuyển đổi đường dẫn Windows (`\`) sang định dạng UNIX (`/`).
    """
    return path.replace("\\", "\\\\")

if __name__ == "__main__":
    current_directory = "."  # Thư mục gốc
    print_leaf_files(current_directory, base_dir=current_directory)
