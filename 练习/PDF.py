from PIL import Image
import os

def image_to_pdf(picture_path, savefilepath):

    imagelist = []
    picName_lst = os.listdir(picture_path)
    picName_lst = sorted(picName_lst, key=lambda x: int(x[:-4]))
    for el in picName_lst:
        new_path = os.path.join(picture_path, el)
        image = Image.open(new_path)
        image.convert("RGB")
        imagelist.append(image)
    im1 = imagelist[0]
    im_rest = imagelist[1:]
    im1.save(savefilepath, save_all=True, append_images=im_rest)

if __name__ == "__main__":
    picture_path= "./image"  # 相对路径
    savefilepath = "./image/合并文档.pdf"
    image_to_pdf(picture_path, savefilepath)