from pathlib import Path
practice_dir = Path.home() / "practice_files" / "documents"
practice_dir.mkdir(parents=True, exist_ok=True)

print(practice_dir.exists())
print()

files_list = ["text15.txt", "document.pdf", "recipes.txt", "image1.png", "image2.gif", "image3.png", "image4.jpg"]

file1_path = practice_dir / "text15.txt"
print(type(file1_path))

file2_path = practice_dir / files_list[1]
print(type(file2_path))

files_path = []

for file in files_list:
  file_path = practice_dir / file
  files_path.append(file_path)
  print(type(file_path))
  # print(file_path.is_file())

print(files_path)
print()

for path in files_path:
  path.touch()
  print(path.is_file())

print()
image_dir = practice_dir / "images_in_documents"
image_dir.mkdir(exist_ok=True)
print(image_dir.exists())

print()
new_images_dir = Path.home() / "practice_files" / "images"
new_images_dir.mkdir(exist_ok=True)
print(new_images_dir.exists())
print()

for path in practice_dir.glob("image?.*"):
  file_name = path.stem + path.suffix
  print(file_name) 
  source = practice_dir / file_name
  destination = new_images_dir / file_name
  source.replace(destination)

  


