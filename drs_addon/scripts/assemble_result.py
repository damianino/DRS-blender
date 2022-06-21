from PIL import Image
import os
import logging

def assembleResult(dir):
    
    resImgPath = os.path.join(dir, "res.png")
    
    if not os.path.exists(resImgPath):
        logging.error("Result image does not exist")
        return
    
    if len(os.listdir(dir)) < 102:
        logging.error("missing files to assemble")
        return

    resImg = Image.open(resImgPath)

    stepX, stepY = resImg.size
    stepX /= 10
    stepY /= 10
    stepX = int(stepX)
    stepY = int(stepY)

    for i in range(0, 100):
        x = (i % 10) * stepX
        y = (10 - i // 10) * stepY
        print(f"{i} : {(x, y)}")
        fragmentPath = os.path.join(dir, str(i)+".png")
        fragment = Image.open(fragmentPath)
        resImg.paste(fragment, (x, y))

    resImg.save(resImgPath, "PNG")
