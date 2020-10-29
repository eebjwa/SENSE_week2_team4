import matplotlib.pyplot as plt

def pcounter(image):
    im = plt.imread(image)
    im_list=im.tolist()
    r=g=b=0
    for row in im_list:
        for item in row:
            r=r+item[0]
            g=g+item[1]
            b=b+item[2]  
            
    total=r+g+b
    
    red=r/total *100
    green=g/total *100
    blue=b/total *100
    
    print (f"% red pixels = {red:.1f} %")
    print (f"% green pixels = {green:.1f} %")
    print (f"% blue pixels = {blue:.1f} %")
    print (f"{red:.1f}, {green:.1f}, {blue:.1f}")

pcounter('Image-name.png')
