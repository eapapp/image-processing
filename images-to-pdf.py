from PIL import Image
from os import path
from os import listdir


if __name__=='__main__':

    print("\nAdding all images in a folder to a single PDF\n---\n")

    imgdir = input('Image folder: ')
    if not path.isdir(imgdir): raise SystemExit
    
    formats = ('.png','.jpg','.jpeg','.bmp','.gif')
    images = []
    for f in listdir(imgdir):
        if f.endswith(formats):
            images.append(f)  

    images.sort()
    files = []
    for f in images:
        img = Image.open(path.join(imgdir,f))
        if img.mode == 'RGBA':
            img.load()
            newimg = Image.new("RGB", img.size, (255, 255, 255))
            newimg.paste(img, mask=img.split()[3])    # 3 is the alpha channel
            files.append(newimg)
        else:
            files.append(img)

    pdf_path = path.join(imgdir, path.basename(imgdir) + '.pdf')
        
    files[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=files[1:]
    )