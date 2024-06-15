from PIL import Image
import sys
def davinsci(path,w1,h1):
    pim = Image.open(r'{}'.format(path))
    oim = pim.resize((w1,h1))#375 250
    im = oim.convert('RGB')
    w,h = im.size
    #print('(width {}, height {})'.format(w,h))
    mat = []

    for width in range(h):
        row=[]
        for height in range(w):
            
            r,g,b = im.getpixel((height,width))
            a = (r,g,b)
            row.append(a)
            #print(row) 
        mat.append(row)
    #print(mat)
        
    print('pixel rgb values retrieved')
    #for i in mat:
        #print(i)
    bm = []
    #print(len(mat))
    print('converting to brightness matrix')
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            pixel = mat[x][y]
            avg = 0
            res = 0
            for rgb in pixel:
                res += rgb
            avg = int(res/3)
            bm.append(avg)
    print('total pixels',len(bm))
    #print(bm)

    mapp = {
        0: '`',    1: '^',    2: '\\',   3: '"',    4: ',',    5: ':',    6: ';',    
        7: 'I',    8: 'l',    9: '!',   10: 'i',   11: '~',   12: '+',   13: '_',   
    14: '-',   15: '?',   16: ']',   17: '[',   18: '}',   19: '{',   20: '1',   
    21: ')',   22: '(',   23: '|',   24: '\\',  25: '/',   26: 't',   27: 'f',   
    28: 'j',   29: 'r',   30: 'x',   31: 'n',   32: 'u',   33: 'v',   34: 'c',   
    35: 'z',   36: 'X',   37: 'Y',   38: 'U',   39: 'J',   40: 'C',   41: 'L',   
    42: 'Q',   43: '0',   44: 'O',   45: 'Z',   46: 'm',   47: 'w',   48: 'q',   
    49: 'p',   50: 'd',   51: 'b',   52: 'k',   53: 'h',   54: 'a',   55: 'o',   
    56: '*',   57: '#',   58: 'M',   59: 'W',   60: '&',   61: '8',   62: '%',   
    63: 'B',   64: '@',   65: '$'
    }


    final=[]
    count = 1
    for i in bm:
        #print(i)
        count+=1
        key = round(i/3.923) 
        print(mapp[key],mapp[key],mapp[key],end='')
        if(count==w):
            print('\n')
            count=0

    #print(len(final))

path = sys.argv[1]
pa = r'{}'.format(path)
w2 = int(sys.argv [2])
h2 = int(sys.argv[3])
davinsci(pa,w2,h2)
