#%%
import json
import pandas as pd
import os

# Paths to the files
test_data_path = "/fs/scratch/PAS2099/DataSet_Butterfly/train_test_separate/(malleti x plesseni) x malleti/train_data.json"
csv_file_path = "/fs/scratch/PAS2099/danielf/SAM2/segment-anything-2/data/butterfly/dorsal_img_master.csv"
output_json_path = "/fs/scratch/PAS2099/DataSet_Butterfly/train_test_separate/(malleti x plesseni) x malleti/1_train_data.json"

# Load the JSON data
with open(test_data_path, "r") as file:
    test_data = json.load(file)

# Load the CSV data
csv_data = pd.read_csv(csv_file_path)

# Create a dictionary for quick lookup of X_value to file_url mapping
x_to_file_url = dict(zip(csv_data['X'], csv_data['file_url']))

# Generate the updated JSON data
updated_data = []
for entry in test_data:
    x_value = entry[0]
    if x_value in x_to_file_url:
        # Create new entry with updated paths
        new_entry = [
            x_value,  # Keep the same X_value
            x_to_file_url[x_value],  # Replace the original image path with the file_url
            os.path.relpath(entry[2], "/fs/scratch/PAS2099/")  # Convert the mask path to a relative path
        ]
        updated_data.append(new_entry)

# Save the updated JSON data to a new file
with open(output_json_path, "w") as file:
    json.dump(updated_data, file, indent=4)

print(f"Updated JSON saved to: {output_json_path}")



#%%
#%%
import json
import pandas as pd
import os
import shutil

# Paths to the folder and CSV file
folder_path = "/fs/scratch/PAS2099/DataSet_Butterfly/train_test_separate/notabilis x lativitta/"
csv_file_path = "/fs/scratch/PAS2099/danielf/SAM2/segment-anything-2/data/butterfly/dorsal_img_master.csv"

# Load the CSV data
csv_data = pd.read_csv(csv_file_path)

# Create a dictionary for quick lookup of X_value to file_url mapping
x_to_file_url = dict(zip(csv_data['X'], csv_data['file_url']))

# List of files to process
file_names = ["test_data.json", "train_data.json"]

for file_name in file_names:
    # Full path to the current file
    file_path = os.path.join(folder_path, file_name)
    backup_file_path = os.path.join(folder_path, f"{file_name.split('.')[0]}_backup.json")
    
    # Check if the file exists
    if os.path.exists(file_path):
        # Load the JSON data
        with open(file_path, "r") as file:
            data = json.load(file)
        
        # Generate the updated JSON data
        updated_data = []
        for entry in data:
            x_value = entry[0]
            if x_value in x_to_file_url:
                # Create new entry with updated paths
                new_entry = [
                    x_value,  # Keep the same X_value
                    x_to_file_url[x_value],  # Replace the original image path with the file_url
                    os.path.relpath(entry[2], "/fs/scratch/PAS2099/")  # Convert the mask path to a relative path
                ]
                updated_data.append(new_entry)
        
        # Rename the original file as a backup
        shutil.move(file_path, backup_file_path)
        
        # Save the updated JSON data with the original name
        with open(file_path, "w") as file:
            json.dump(updated_data, file, indent=4)
        
        print(f"Processed {file_name}: backup saved as {backup_file_path} and updated file saved as {file_path}")
    else:
        print(f"File not found: {file_path}")
#%%

import json

# Path to the input and output files
input_json_path = "/fs/scratch/PAS2099/DataSet_Butterfly/minor_major_mask_final.json"
minor_output_json_path = "/fs/scratch/PAS2099/DataSet_Butterfly/minor_species_only.json"
major_output_json_path = "/fs/scratch/PAS2099/DataSet_Butterfly/major_species_only.json"

# List of major species to filter
major_species = [
    "(malleti x plesseni) x malleti",
    "lativitta",
    "cyrbia",
    "malleti",
    "notabilis x lativitta"
]

# Load the JSON data
with open(input_json_path, "r") as file:
    data = json.load(file)

# Separate the entries into major and minor species
major_species_data = [entry for entry in data if any(species in str(entry) for species in major_species)]
minor_species_data = [entry for entry in data if all(species not in str(entry) for species in major_species)]

# Save the filtered data to separate files
with open(minor_output_json_path, "w") as file:
    json.dump(minor_species_data, file, indent=4)

with open(major_output_json_path, "w") as file:
    json.dump(major_species_data, file, indent=4)

print(f"Minor species JSON saved to: {minor_output_json_path}")
print(f"Major species JSON saved to: {major_output_json_path}")

#%%
import json

# 输入和输出文件路径
input_json_path = "/fs/scratch/PAS2099/DataSet_Butterfly/minor_major_mask_final.json"
minor_output_json_path = "/fs/scratch/PAS2099/DataSet_Butterfly/minor_species_only.json"
major_output_json_path = "/fs/scratch/PAS2099/DataSet_Butterfly/major_species_only.json"

# Major species 列表
major_species = [
    "(malleti x plesseni) x malleti",
    "lativitta",
    "cyrbia",
    "malleti",
    "notabilis x lativitta"
]

# 加载 JSON 数据
with open(input_json_path, "r") as file:
    data = json.load(file)

# 分离数据到 major 和 minor
major_species_data = []
minor_species_data = []

for entry in data:
    # 检查 entry 是否属于 major species
    if any(species in str(entry) for species in major_species):
        major_species_data.append(entry)
    else:
        minor_species_data.append(entry)

# 保存结果到新的文件
with open(minor_output_json_path, "w") as file:
    json.dump(minor_species_data, file, indent=4)

with open(major_output_json_path, "w") as file:
    json.dump(major_species_data, file, indent=4)

print(f"Minor species JSON 保存至: {minor_output_json_path}")
print(f"Major species JSON 保存至: {major_output_json_path}")

#%%
import json

# 输入和输出文件路径
input_json_path = "/fs/scratch/PAS2099/DataSet_Butterfly/minor_major_mask_final.json"
minor_output_json_path = "/fs/scratch/PAS2099/DataSet_Butterfly/minor_species_only.json"
major_output_json_path = "/fs/scratch/PAS2099/DataSet_Butterfly/major_species_only.json"

# Major species 列表
major_species = [
    "(malleti x plesseni) x malleti",
    "lativitta",
    "cyrbia",
    "malleti",
    "notabilis x lativitta"
]

# 加载 JSON 数据
with open(input_json_path, "r") as file:
    data = json.load(file)

# 初始化 major 和 minor species 数据
major_species_data = {}
minor_species_data = {}

# 遍历数据，区分 major 和 minor species
for species_name, species_data in data.items():
    if species_name in major_species:
        major_species_data[species_name] = species_data
    else:
        minor_species_data[species_name] = species_data

# 保存结果到新的文件
with open(minor_output_json_path, "w") as file:
    json.dump(minor_species_data, file, indent=4)

with open(major_output_json_path, "w") as file:
    json.dump(major_species_data, file, indent=4)

print(f"Minor species JSON 保存至: {minor_output_json_path}")
print(f"Major species JSON 保存至: {major_output_json_path}")


#%%
import json
import os
import pandas as pd

# 输入和输出文件路径
minor_input_json_path = "/fs/scratch/PAS2099/DataSet_Butterfly/minor_species_only.json"
csv_file_path = "/fs/scratch/PAS2099/danielf/SAM2/segment-anything-2/data/butterfly/dorsal_img_master.csv"
minor_output_json_path = "/fs/scratch/PAS2099/DataSet_Butterfly/minor_species_updated.json"

# 加载 JSON 数据
with open(minor_input_json_path, "r") as file:
    minor_species_data = json.load(file)

# 加载 CSV 数据，构建 X_value 到 file_url 的映射
csv_data = pd.read_csv(csv_file_path)
x_to_file_url = dict(zip(csv_data['X'], csv_data['file_url']))

# 更新 JSON 数据
updated_minor_species_data = {}
for species_name, entries in minor_species_data.items():
    updated_entries = []
    for entry in entries:
        x_value = entry[0]
        if x_value in x_to_file_url:
            updated_entry = [
                x_value,  # 保持 X_value 不变
                x_to_file_url[x_value],  # 用 file_url 替换原来的 original 路径
                os.path.relpath(entry[2], "/fs/scratch/PAS2099/"),  # 将 masked_img 路径改为相对路径
                entry[3]  # 保持其他字段不变
            ]
            updated_entries.append(updated_entry)
    updated_minor_species_data[species_name] = updated_entries

# 保存更新后的 JSON 数据
with open(minor_output_json_path, "w") as file:
    json.dump(updated_minor_species_data, file, indent=4)

print(f"Updated minor species JSON saved to: {minor_output_json_path}")

#%%
import os
import shutil

# Path to the parent folder containing all species folders
parent_folder_path = "/fs/scratch/PAS2099/DataSet_Butterfly/Minor_species_data"

# Iterate over each folder in the parent directory
for species_folder in os.listdir(parent_folder_path):
    species_folder_path = os.path.join(parent_folder_path, species_folder)
    
    # Skip if it's not a directory
    if not os.path.isdir(species_folder_path):
        continue

    # Iterate over the contents of the species folder
    for subfolder in os.listdir(species_folder_path):
        subfolder_path = os.path.join(species_folder_path, subfolder)

        # If the folder is not 'masked_img', delete it
        if os.path.isdir(subfolder_path) and subfolder != "masked_img":
            shutil.rmtree(subfolder_path)
            print(f"Deleted folder: {subfolder_path}")

print("Cleanup complete: All folders except 'masked_img' have been deleted.")
