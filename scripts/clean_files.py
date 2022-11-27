from pathlib import Path

file_path = Path("materials/some_linking_words_list.txt").resolve()

with open(file_path) as f:
    contents = f.read().split('\n')

cleaned_items = []

for item in contents:
    items = " ".join(item.split(' ')[1:])
    cleaned_item = items.split('—')[0]
    cleaned_items.append(cleaned_item.strip())

new_file_path = Path(file_path.parent, file_path.stem + '_cleaned' + file_path.suffix)
with open(new_file_path, 'w+') as f:
    f.write("\n".join(cleaned_items))
