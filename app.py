from services import (image_data as image, utils)


def hide_data_in_image():
    image_input = utils.select_image_in_folder("inputs")
    output_path = image_input.replace("inputs/", "outputs/processed_")
    data_to_hide = str(input('Enter the data to hide: '))
    if not len(data_to_hide):
        print('Invalid data')
        exit('Error 2: Invalid data')
    try:
        image.hide_data_in_image(image_input, output_path, data_to_hide)
        print("Data hidden successfully in", output_path)
    except ValueError as e:
        print("Error:", e)

def start_presentation():
    print('******** CryptoPixel  ********')
    print('- Select the option -')
    print('1 - Hide data in image')
    print('2 - Extract data from image')
    option = str(input('Option: '))
    if option not in ['1', '2']:
        print('Invalid option')
        exit('Error 1: Invalid option')
    return option


if __name__ == "__main__":
    option = start_presentation()
    if option == '1':
        hide_data_in_image()
    elif option == '2': 
        image.extract_data_from_image()