import os

def save_text(output_folder, file_name, text):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    text_file_path = os.path.join(output_folder, f"{file_name}.txt")

    with open(text_file_path, "w") as text_file:
        text_file.write(text)
    print(f"|__Text saved to {text_file_path}.")