from PIL import Image, ImageDraw


def twist_image(input_file_name, output_file_name):
    im = Image.open(input_file_name)
    x, y = im.size

    im1 = im.crop((0, 0, int(0.5 * x), y))
    im2 = im.crop((int(0.5 * x), 0, x, y))

    im.paste(im2, (0, 0))
    im.paste(im1, (int(x * 0.5), 0))

    im.save(output_file_name)


twist_image('statement-image.jpg', 'new_statement-image.jpg')