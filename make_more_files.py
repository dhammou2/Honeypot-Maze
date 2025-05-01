import os
import random
import string
import sys
import time
from openai import OpenAI

# WARNING: I do not recommend hardcoding an API key. I just did it for demostration purposes :')
client = OpenAI(api_key="API_KEY")

def get_fake_filenames_from_gpt():
    response = client.responses.create(
        model="gpt-4.1",
        input=(
            "Generate a list of 1 to 5 realistic but fake sensitive file names that might attract a hacker. "
            "Make them look like passwords, credentials, financial data, HR records, admin keys, or secret config files. "
            "Just the file names, no explanation (do number them, do not include zip files)."
        )
    )

    raw_text = response.output_text
    file_names = [
        line.strip("•- 1234567890.").strip()
        for line in raw_text.strip().splitlines()
        if line.strip()
    ]

    print("[*] GPT-Generated File Names:", file_names)
    return file_names

def random_string(length=40):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_more_fake_files_and_folders(target_folder):
    marker = os.path.join(target_folder, ".expanded")
    if os.path.exists(marker):
        print(f"[!] Already expanded: {target_folder}")
        return

    print(f"[+] Expanding folder: {target_folder}")

    fake_files = get_fake_filenames_from_gpt()

    for _ in range(random.randint(2, 3)):
        file_name = random.choice(fake_files)
        file_path = os.path.join(target_folder, file_name)
        with open(file_path, "w") as f:
            for _ in range(5):
                f.write(random_string() + "\n")
        print(f"  [+] Created file: {file_path}")

    subfolder_name = f"sys_{random.randint(1000, 9999)}"
    subfolder_path = os.path.join(target_folder, subfolder_name)
    os.makedirs(subfolder_path, exist_ok=True)
    print(f"  [+] Created subfolder: {subfolder_path}")

    with open(marker, "w") as m:
        m.write("already expanded")

    time.sleep(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python make_more_files.py /path/to/target_folder")
        return

    target = sys.argv[1]
    create_more_fake_files_and_folders(target)

if __name__ == "__main__":
    main()
