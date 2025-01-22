#%%
import json

def modify_json_paths(json_file_path, output_file_path, keys_to_skip, old_path, new_path):
    """
    修改 JSON 文件中的路径，跳过指定的键。
    
    Args:
        json_file_path (str): 输入 JSON 文件路径。
        output_file_path (str): 保存修改后的 JSON 文件路径。
        keys_to_skip (list): 不修改的键列表。
        old_path (str): 要替换的旧路径部分。
        new_path (str): 替换为的新路径部分。
    """
    # 读取 JSON 文件
    with open(json_file_path, "r") as f:
        data = json.load(f)
    
    # 遍历 JSON 数据
    for key, entries in data.items():
        if key in keys_to_skip:
            continue  # 跳过指定的键

        for entry in entries:
            # 修改 picture 路径
            if old_path in entry[1]:
                entry[1] = entry[1].replace(old_path, new_path)
            # 修改 mask 路径
            if old_path in entry[2]:
                entry[2] = entry[2].replace(old_path, new_path)
    
    # 保存修改后的 JSON 文件
    with open(output_file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Modified JSON saved to {output_file_path}")

# 示例使用
if __name__ == "__main__":
    # 输入 JSON 文件路径
    json_file_path = "/fs/scratch/PAS2099/DataSet_Butterfly/minor_major_mask_png.json"
    
    # 输出修改后的 JSON 文件路径
    output_file_path = "/fs/scratch/PAS2099/DataSet_Butterfly/minor_major_mask_png_modified.json"
    
    # 不修改的键列表
    keys_to_skip = [
        "lativitta",
        "cyrbia",
        "malleti",
        "(malleti x plesseni) x malleti",
        "notabilis x lativitta"
    ]
    
    # 要替换的路径
    old_path = "/fs/scratch/PAS2099/Herz/segment_anything_2/code/cambridge/minor_subspecies/dataset/"
    new_path = "/fs/scratch/PAS2099/DataSet_Butterfly/Minor_species_data/"
    
    # 调用函数修改 JSON 文件
    modify_json_paths(json_file_path, output_file_path, keys_to_skip, old_path, new_path)

# %%
import json

def modify_major_paths(json_file_path, output_file_path, keys_to_modify, old_path, new_path):
    """
    修改 JSON 文件中 Major 部分的路径。
    
    Args:
        json_file_path (str): 输入 JSON 文件路径。
        output_file_path (str): 保存修改后的 JSON 文件路径。
        keys_to_modify (list): 要修改的 Major 键列表。
        old_path (str): 要替换的旧路径部分。
        new_path (str): 替换为的新路径部分。
    """
    # 读取 JSON 文件
    with open(json_file_path, "r") as f:
        data = json.load(f)
    
    # 遍历 JSON 数据
    for key, entries in data.items():
        if key in keys_to_modify:
            for entry in entries:
                # 修改 picture 路径
                if old_path in entry[1]:
                    entry[1] = entry[1].replace(old_path, new_path)
                # 修改 mask 路径
                if old_path in entry[2]:
                    entry[2] = entry[2].replace(old_path, new_path)
    
    # 保存修改后的 JSON 文件
    with open(output_file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Modified JSON saved to {output_file_path}")

# 示例使用
if __name__ == "__main__":
    # 输入 JSON 文件路径
    json_file_path = "/fs/scratch/PAS2099/DataSet_Butterfly/minor_major_mask_png_modified.json"
    
    # 输出修改后的 JSON 文件路径
    output_file_path = "/fs/scratch/PAS2099/DataSet_Butterfly/minor_major_mask_png_modified_2.json"
    
    # 需要修改的 Major 键列表
    keys_to_modify = [
        "lativitta",
        "cyrbia",
        "malleti",
        "(malleti x plesseni) x malleti",
        "notabilis x lativitta"
    ]
    
    # 要替换的路径
    old_path = "/fs/scratch/PAS2099/Herz/Mask_Storage/"
    new_path = "/fs/scratch/PAS2099/DataSet_Butterfly/Major_spefies_data/"
    
    # 调用函数修改 JSON 文件
    modify_major_paths(json_file_path, output_file_path, keys_to_modify, old_path, new_path)

#%%
import os
import json

def check_paths_in_json(json_file_path, major_keys):
    """
    检查 JSON 文件中所有 img 和 mask 路径是否存在，分为 minor 和 major 部分。
    
    Args:
        json_file_path (str): JSON 文件路径。
        major_keys (list): major 部分的键列表。
    
    Returns:
        dict: 包含缺失路径的详细信息。
    """
    # 读取 JSON 文件
    with open(json_file_path, "r") as f:
        data = json.load(f)
    
    # 定义结果存储
    missing_paths = {"minor": [], "major": []}

    # 遍历 JSON 数据
    for key, entries in data.items():
        category = "major" if key in major_keys else "minor"
        for entry in entries:
            img_path = entry[1]
            mask_path = entry[2]
            if not os.path.exists(img_path):
                missing_paths[category].append({"type": "img", "path": img_path})
            if not os.path.exists(mask_path):
                missing_paths[category].append({"type": "mask", "path": mask_path})
    
    # 输出结果
    print("Missing Paths Summary:")
    print("======================")
    for category, paths in missing_paths.items():
        print(f"{category.capitalize()} ({len(paths)} missing paths):")
        for item in paths:
            print(f"  {item['type']} - {item['path']}")
    print("======================")
    return missing_paths

# 示例使用
if __name__ == "__main__":
    # JSON 文件路径
    json_file_path = "/fs/scratch/PAS2099/DataSet_Butterfly/minor_major_mask_png_modified_2.json"
    
    # 定义 major 部分的键列表
    major_keys = [
        "lativitta",
        "cyrbia",
        "malleti",
        "(malleti x plesseni) x malleti",
        "notabilis x lativitta"
    ]
    
    # 调用函数检查路径
    missing_paths = check_paths_in_json(json_file_path, major_keys)
#%%
import os
import json

def process_species_data(major_species_folder, output_folder, reference_json):
    """
    处理每个 major species 的 train/test 数据，生成新的 PNG 路径列表。
    
    Args:
        major_species_folder (str): major species 文件夹路径。
        output_folder (str): 输出文件夹路径。
        reference_json (str): 包含所有数据的 JSON 文件路径。
    """
    # 加载参考 JSON 文件
    with open(reference_json, "r") as f:
        reference_data = json.load(f)
    
    # 遍历每个 major species 文件夹
    for species_name in os.listdir(major_species_folder):
        species_path = os.path.join(major_species_folder, species_name)
        json_folder = os.path.join(species_path, "json")
        
        # 检查 json 文件夹是否存在
        if not os.path.isdir(json_folder):
            print(f"JSON folder not found for species: {species_name}")
            continue
        
        # 读取 test_data.json 和 train_data.json
        for split in ["test_data.json", "train_data.json"]:
            split_path = os.path.join(json_folder, split)
            if not os.path.exists(split_path):
                print(f"{split} not found for species: {species_name}")
                continue
            
            # 加载 train/test 数据
            with open(split_path, "r") as f:
                data = json.load(f)
            
            # 存储结果和未找到的数据
            result_data = []
            missing_data = []
            
            # 查找每个 ID 的 PNG 路径
            for entry in data:
                entry_id = entry[0]
                found = False
                
                # 遍历 reference JSON 数据
                for key, entries in reference_data.items():
                    for ref_entry in entries:
                        if ref_entry[0] == entry_id:
                            result_data.append(ref_entry[1:3])  # 提取两个 PNG 路径
                            found = True
                            break
                    if found:
                        break
                
                # 如果未找到，记录为 missing
                if not found:
                    missing_data.append(entry_id)
            
            # 创建输出文件夹
            species_output_folder = os.path.join(output_folder, species_name)
            os.makedirs(species_output_folder, exist_ok=True)
            
            # 保存结果文件
            output_file_path = os.path.join(species_output_folder, split)
            with open(output_file_path, "w") as f:
                json.dump(result_data, f, indent=4)
            
            print(f"Saved {split} for {species_name} at {output_file_path}")
            
            # 如果有未找到的数据，打印统计信息
            if missing_data:
                print(f"Missing data for {split} in species: {species_name}")
                print(f"IDs not found: {missing_data}")

# 主程序
if __name__ == "__main__":
    # 输入文件夹路径
    major_species_folder = "/fs/scratch/PAS2099/Herz/major_species"
    output_folder = "/fs/scratch/PAS2099/DataSet_Butterfly/train_test_separate"
    reference_json = "/fs/scratch/PAS2099/DataSet_Butterfly/minor_major_mask_final.json"
    
    # 调用函数处理数据
    process_species_data(major_species_folder, output_folder, reference_json)
#%%
import os
import pickle
import cv2
import numpy as np

def convert_pkl_to_png(pkl_file_path, png_file_path):
    """
    将 .pkl 文件中的 mask 数据转换为灰度值的 .png 文件。
    
    Args:
        pkl_file_path (str): 输入的 .pkl 文件路径。
        png_file_path (str): 输出的 .png 文件路径。
    """
    with open(pkl_file_path, "rb") as f:
        masks = pickle.load(f)  # 读取 .pkl 文件

    # 初始化空白图像
    blank = np.zeros((1024, 1024), dtype=np.uint8)
    
    # 遍历每个 mask，将其填充到 blank 图像
    for idx, mask in enumerate(masks):
        mask = cv2.resize(mask, (1024, 1024)).astype(bool)
        blank[mask] = idx + 1  # 用不同灰度值表示每个 mask

    # 保存为 PNG 文件
    cv2.imwrite(png_file_path, blank)
    print(f"Generated PNG: {png_file_path}")

def process_major_species_folder(base_folder):
    """
    遍历 Major Species 文件夹，检查 .pkl 文件是否有对应的 .png 文件。
    如果没有 .png 文件，则生成它。
    
    Args:
        base_folder (str): Major Species 文件夹的路径。
    """
    for species_name in os.listdir(base_folder):
        species_path = os.path.join(base_folder, species_name)
        pkl_folder = os.path.join(species_path, "pkl")
        
        # 检查是否有 pkl 文件夹
        if not os.path.isdir(pkl_folder):
            print(f"No 'pkl' folder found for {species_name}, skipping...")
            continue
        
        # 遍历 pkl 文件夹中的 .pkl 文件
        for pkl_file in os.listdir(pkl_folder):
            if not pkl_file.endswith(".pkl"):
                continue
            
            pkl_file_path = os.path.join(pkl_folder, pkl_file)
            png_file_name = pkl_file.replace(".pkl", ".png")
            png_file_path = os.path.join(pkl_folder, png_file_name)
            
            # 检查是否存在对应的 .png 文件
            if not os.path.exists(png_file_path):
                # 如果不存在，则生成 .png 文件
                convert_pkl_to_png(pkl_file_path, png_file_path)
            else:
                print(f"PNG file already exists: {png_file_path}")

# 主程序
if __name__ == "__main__":
    # Major Species 数据文件夹路径
    base_folder = "/fs/scratch/PAS2099/DataSet_Butterfly/Major_spefies_data"
    
    # 调用函数处理数据
    process_major_species_folder(base_folder)


#%%
import os
import json

def process_species_data(major_species_folder, output_folder, pkl_base_folder):
    """
    处理每个 major species 的 train/test 数据，生成新的 JSON 文件，包含 ID、original 和 mask 的路径。
    
    Args:
        major_species_folder (str): major species 文件夹路径。
        output_folder (str): 输出文件夹路径。
        pkl_base_folder (str): 包含 pkl 文件夹的基路径。
    """
    # 遍历每个 major species 文件夹
    for species_name in os.listdir(major_species_folder):
        species_path = os.path.join(major_species_folder, species_name)
        json_folder = os.path.join(species_path, "json")
        
        # 检查 json 文件夹是否存在
        if not os.path.isdir(json_folder):
            print(f"JSON folder not found for species: {species_name}")
            continue
        
        # 处理 train_data.json 和 test_data.json
        for split in ["train_data.json", "test_data.json"]:
            split_path = os.path.join(json_folder, split)
            if not os.path.exists(split_path):
                print(f"{split} not found for species: {species_name}")
                continue
            
            # 加载 train/test 数据
            with open(split_path, "r") as f:
                data = json.load(f)
            
            # 存储结果和未找到的数据
            result_data = []
            missing_data = []
            
            # 查找每个 ID 的 PNG 路径
            for entry in data:
                entry_id = entry[0]
                pkl_folder = os.path.join(pkl_base_folder, species_name, "pkl")
                original_path = os.path.join(pkl_folder.replace("pkl", "original"), f"{species_name}_{entry_id}.png")
                mask_path = os.path.join(pkl_folder, f"masks_{entry_id}.png")
                
                if os.path.exists(original_path) and os.path.exists(mask_path):
                    result_data.append([entry_id, original_path, mask_path])
                else:
                    missing_data.append({"id": entry_id, "species": species_name})
            
            # 创建输出文件夹
            species_output_folder = os.path.join(output_folder, species_name)
            os.makedirs(species_output_folder, exist_ok=True)
            
            # 保存结果文件
            output_file_path = os.path.join(species_output_folder, split)
            with open(output_file_path, "w") as f:
                json.dump(result_data, f, indent=4)
            
            print(f"Saved {split} for {species_name} at {output_file_path}")
            
            # 如果有未找到的数据，打印统计信息
            if missing_data:
                print(f"Missing data for {split} in species: {species_name}")
                for missing in missing_data:
                    print(f"  ID {missing['id']} not found in species {missing['species']}")

# 主程序
if __name__ == "__main__":
    # 输入文件夹路径
    major_species_folder = "/fs/scratch/PAS2099/Herz/major_species"
    output_folder = "/fs/scratch/PAS2099/DataSet_Butterfly/train_test_separate"
    pkl_base_folder = "/fs/scratch/PAS2099/DataSet_Butterfly/Major_spefies_data"
    
    # 调用函数处理数据
    process_species_data(major_species_folder, output_folder, pkl_base_folder)

