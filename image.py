from PIL import Image
import os

def convert(image, file_type, new_name, scale = 0):
    global txt_path

    img = Image.open(image)

    width, height = img.size

    # se possui escala, vamos alterá-la
    if scale != 0:
        img.resize((width // scale, height // scale)).save("resized.%s" % file_type)

        img = Image.open("resized.%s" % file_type)
        width, height = img.size

    # grid que vai guardar a foto convertida em texto
    grid = []
    for _ in range(height):
        grid.append(['X'] * width)

    # guardando os pixels da imagem
    pixels = img.load()

    # percorrendo os pixels
    for row in range(height):
        for col in range(width):
            pixel = sum(pixels[col, row])

            if pixel == 0:
                grid[row][col] = '#'
            
            elif pixel in range(0, 100):
                grid[row][col] = '+'
            
            elif pixel in range(100, 200):
                grid[row][col] = '/'
            
            elif pixel in range(200, 300):
                grid[row][col] = '|'

            elif pixel in range(300, 400):
                grid[row][col] = '^'

            elif pixel in range(400, 500):
                grid[row][col] = "'"

            elif pixel in range(500, 600):
                grid[row][col] = '.'

            elif pixel in range(600, 700):
                grid[row][col] = '-'

            elif pixel in range(700, 800):
                grid[row][col] = '~'

            else:
                grid[row][col] = '='
    
    # criando novo arquivo em images-txt
    new_file = os.path.join(txt_path, new_name)

    if scale != 0:
        # excluindo o arquivo temporário com a nova escala
        os.remove(f"resized.{file_type}")

    # escrevendo no novo arquivo
    with open(new_file, "w") as file:
        for row in grid:
            file.write("".join(row) + '\n')

if __name__ == '__main__':
    jpg_path = "images-jpg"
    txt_path = "images-txt"

    # percorrendo todos as fotos na pasta images-jpg
    for jpg_file in os.listdir(jpg_path):
        name, file_type = jpg_file.split('.')

        # se já existia uma foto convertida em texto, excluímos ela e fazemos de novo
        if os.path.exists(f"{txt_path}\\{"".join(name)}.txt"):
            os.remove(f"{txt_path}\\{"".join(name)}.txt")

        # função de converter foto em texto
        convert(f"{jpg_path}\\{jpg_file}", file_type, f"{"".join(name)}.txt", 3)