def tile_horizontally(background_img, pattern, start_location, repetitions, shift):
    "Tiles a pattern on a background image, repeatedly with a given shift."
    img = background_img.copy()
    for i in range(repetitions):
        r, c = start_location
        c += i * shift
        img = insert_pattern(img, pattern, location=(r, c))
    return img