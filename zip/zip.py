# in zip folder unzip zip then a new zip will apear with name chunk_n.zip wher n is 0 when unzipping that another zip with chunk_1 apper do it until failes

import os
import zipfile


def unzip_file(file_path, dest_dir):
  with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(dest_dir)


def main():
  base_dir = os.getcwd()
  chunk_num = 28405

  while True:
    zip_name = f'chunk_{chunk_num}.zip'
    zip_path = os.path.join(base_dir, zip_name)

    if not os.path.exists(zip_path):
      print(
          f"No more zip files found after chunk_{chunk_num}.zip. Exiting.")
      break

    print(f"Unzipping {zip_name}...")
    unzip_file(zip_path, base_dir)
    chunk_num += 1


def main2():
    # Initialize the chunk number and the base directory
  n = 0
  base_dir = os.getcwd()
  final_file = os.path.join(base_dir, 'final.txt')

  # Open the final.txt in write mode
  with open(final_file, 'w') as final_output:
    while True:
      # Build the chunk file name
      name = f'chunk_{n}.txt'
      chunk_path = os.path.join(base_dir, name)

      # If the chunk file does not exist, exit the loop
      if not os.path.exists(chunk_path):
        print(f"No more files found after chunk_{n}.txt. Exiting.")
        break

      # Read the content of the current chunk file and write it to final.txt
      with open(chunk_path, 'r') as chunk_file:
        content = chunk_file.read()
        final_output.write(content)

      n += 1


if __name__ == "__main__":
  main2()
