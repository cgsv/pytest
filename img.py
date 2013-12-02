from pylab import *

def randomColor():
    return random_integers(0, 255, 3)

def unitedPicHori(img1, img2):
    w1,l1,c1 = img1.shape
    w2,l2,c2 = img2.shape
    neww = w1
    if w1 != w2:
        neww = max(w1,w2)
    newimg = zeros((neww, l1+l2,c1),dtype='uint8')
    newimg[:w1,0:l1,:] = img1[:,:,:]
    newimg[:w2,l1:,:] = img2[:,:,:]
    return newimg

def unitedPicHoriAll(*img):
    n = len(img)
    if n <= 0: return
    res = img[0]
    for i in xrange(n-1):
        res = unitedPicHori(res,img[i+1])
    return res

def unitedPicHoriN(img, n):
    if n <= 0: return
    res = img[:,:,:]
    for i in xrange(n-1):
        res = unitedPicHori(res,img)
    return res

def unitedPicVet(img1, img2):
    w1,l1,c1 = img1.shape
    w2,l2,c2 = img2.shape
    newl = l1
    if l1 != l2:
        newl = max(l1,l2)
    newimg = zeros((w1+w2, newl,c1),dtype='uint8')
    newimg[:w1,:l1,:] = img1[:,:,:]
    newimg[w1:,:l2,:] = img2[:,:,:]
    return newimg

def unitedPicVetAll(*img):
    n = len(img)
    if n <= 0: return
    res = img[0]
    for i in xrange(n-1):
        res = unitedPicVet(res,img[i+1])
    return res

def unitedPicVetN(img, n):
    if n <= 0: return
    res = img[:,:,:]
    for i in xrange(n-1):
        res = unitedPicVet(res,img)
    return res

def unitedPicMatric(img, row, col):
    res1 = unitedPicVetN(img, row)
    res = unitedPicHoriN(res1, col)
    return res

def shrinkImg(img,cw, cl):
    return img[::cw,::cl,:]

def shrinkImg2(img, cw, cl):
    w, l, c = img.shape
    mw = np.int0(linspace(0, w - 1, int(w*cw)))
    ml = np.int0(linspace(0, l - 1, int(l*cl)))
    return img[mw, :, :][:, ml,:]

def picInPic(oripic, inpic, sw, sl):
    w1, l1, c1 = oripic.shape
    w2, l2, c2 = inpic.shape
    if w2 + sw > w1 or l2 + sl > l1:
        print 'the picture within in too large'
        return 0
    oricpy = oripic[:,:,:]
    oricpy[sw:sw+w2,sl:sl+l2,:] = inpic[:,:,:]
    return oricpy

def picInpicCenter(pic, coef, invertColor=False, randomC=False):
    pic1 = pic[:,:,:]
    pic2 = shrinkImg2(pic, coef, coef)
    w, l, c = pic.shape
    sw = (w - w*coef)/2
    sl = (l - l*coef)/2
    if invertColor:
        pic2 = 255 - pic2
    if randomC:
        #pic1[:,:,0] = random_integers(0,255)
        #pic1[:,:,1] = random_integers(0,255)
        #pic1[:,:,2] = random_integers(0,255)
        #a = randomColor()
        pic1[:,:] = randomColor()
    return picInPic(pic1, pic2, int(sw), int(sl))

def picInpicCenterAll(pic, coef, invertColor=False, randomC=False):
    pic2 = pic[:,:,:]
    m = max(pic.shape[0], pic.shape[1])
    n = log(1.0/m) / log(coef)
    for i in range(int(n)):
        pic2 = picInpicCenter(pic2, coef, invertColor, randomC)
    return pic2

def enlargeImg(img, cw, cl):
    w, l, color = img.shape
    newimg = zeros((w*cw, l*cl, color),dtype='uint8')
    for iw in xrange(w*cw):
        for il in xrange(l*cl):
            newimg[iw, il, :] = img[iw/cw, il/cl,:]
    return newimg

if __name__ == '__main__':
    xhh = imread('d:/xhh.jpg')
    blankimg = np.zeros((500,500,3), dtype='uint8')
    pl, pw, color = xhh.shape
    xhhs = shrinkImg2(xhh, 0.8, 0.8)
    row1 = unitedPicHoriAll(xhhs, xhhs, xhhs, xhhs)
    left = unitedPicVet(xhhs, xhhs)
    row2 = unitedPicHoriAll(left,xhh,left)
    final = unitedPicVetAll(row1, row2, row1)
    #imshow(final)
    #imshow(unitedPicMatric(xhh,4,3))
    #imshow(enlargeImg(xhh,3,3))
    #imshow(shrinkImg2(xhh,0.3,0.3))
    #imshow(picInPic(xhh, xhhs, pl/10, pw/10))
    imshow(picInpicCenterAll(blankimg,0.8, False, True))
    show()
