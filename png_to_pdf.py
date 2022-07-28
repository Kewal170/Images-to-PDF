import os

from PIL import Image

IMAGE_EXTENSIONS = ['.png', '.jpeg', '.jpg']
print("\nRecommended - width : 816 and height : 1056")
print("*" * 50)
try:
    width = int(input("Enter the width :> "))
    height = int(input("Enter the height :> "))
    filename = input("Enter the name of the pdf :> ")
    image_list = []
    print("-" * 50)
    for file in os.listdir():
        count = 0
        if any(file.endswith(extension) for extension in IMAGE_EXTENSIONS):
            print(file)
            img = Image.open(file)
            img = img.resize((width, height))
            image_list.append(img)
        count += 1
    if len(image_list) != 0:
        print("\nAll Images Fetched! Converting to PDF...")
        image_list[0].save(f'{filename}.pdf', save_all=True, append_images=image_list[1:])

        print("-" * 50)
        print(f"Pdf File Converted! : {filename}.pdf")
        print("-" * 50)

    else:
        print("No image file found!")

except Exception as e:
    print(f"Please enter integers.!\nError ::>>  {e}")
