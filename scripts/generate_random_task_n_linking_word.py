from pathlib import Path
import random

link_words_file_path = Path("materials/some_linking_words_list_cleaned.txt").resolve()
essay_task_file_path = Path("materials/some_writing_task2_questions.txt").resolve()

with open(link_words_file_path) as f, open(essay_task_file_path) as f_task:
    link_words = f.read().split('\n')
    tasks = f_task.read().split('\n')

print(f"Task: {random.choice(tasks)}")
print(f"Linking word to use: {random.choice(link_words)}")
