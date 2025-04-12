import os

def list_images(pasta):
    return [f for f in os.listdir(pasta) if f.lower().endswith(('.png'))]

def select_image_in_folder(pasta):
    images = list_images(pasta)
    if not images:
        exit(f"PNG not found in folder '{pasta}'.")
    print(f"\nImages in folder '{pasta}':")
    for idx, imagem in enumerate(images, start=1):
        print(f"{idx}. {imagem}")

    choice = input("Input the Image Number: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(images):
            caminho = os.path.join(pasta, images[choice - 1])
            return caminho
        else:
            exit("Invalid Image Number.")
    except ValueError:
        exit("Invalid input. Input a number.")
    
    return None