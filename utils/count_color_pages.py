if __name__ == "__main__":
    with open("color.log") as f:
        color_info = f.read().splitlines()
        # color_info = f.readlines()

    color_info = color_info[1:]
    color_info = color_info[1::2]
    color_info = [i.strip() for i in color_info]
    color_info = [i.replace("CMYK OK", "") for i in color_info]
    color_info = [i.replace("Page ", "") for i in color_info]
    color_info = [i.split("  ") for i in color_info]
    color_info = [[float(j) for j in i] for i in color_info]

    n_color_pages = 0
    n_black_pages = 0
    colored_pages, black_pages = [], []
    for i, page in enumerate(color_info):
        if (page[0] > 0) or (page[1] > 0) or (page[2] > 0):
            n_color_pages += 1
            colored_pages.append(i+1)
        else:
            n_black_pages += 1
            black_pages.append(i+1)

    """n_color_pages = 0
    n_black_pages = 0

    for page_front, page_back in zip(color_info[::2], color_info[1::2]):
        if (page_front[0] > 0) or (page_front[1] > 0) or (page_front[2] > 0) or \
            (page_back[0] > 0) or (page_back[1] > 0) or (page_back[2] > 0):
            n_color_pages += 1
        else:
            n_black_pages += 1
    """

    n_total = n_color_pages + n_black_pages

    print("Color information:")
    print(f"{n_color_pages}/{n_total} in colour and {n_black_pages}/{n_total} in black and white.")

    print("Colour pages: ", colored_pages)
    print("Black pages:", black_pages)