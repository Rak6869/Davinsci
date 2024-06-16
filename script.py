from PIL import Image
import sys
def davinsci(path,w1,h1,cho):
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
            if(cho==1):
                #print('Average')
                for rgb in pixel:
                    res += rgb
                avg = int(res/3)
                bm.append(avg)
            elif(cho==2):
                #print('Lightness')
                avg = int((max(pixel) + min(pixel)) / 2)
                bm.append(avg)
            elif(cho==3):
                #print('Luminosity')
                r,g,b = pixel
                avg = int((0.21*r + 0.72*g + 0.07*b))
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
        print(mapp[key],end='')
        if(count==w):
            print('\n')
            count=0

    #print(len(final))

run_flag = 0
flag = 0
cho_hw = -1
w2 = 1850
h2 = 250
ch = 1
ch_flag = 0
print('-----------------------------------------DAVINSCI-----------------------------------------')
path = input('Enter Path (without quotes): ')
pa = r'{}'.format(path)
print('Default Setting (1850x250, Average) (9)')
print('Change Resolution (1850x250) (1)')
print('Change Brightness Matrix (2)')
print('Run (4)')
print('Exit (5)')
print('The settings you do not change will be set with default choices')
while ch_flag == 0:
    cho_run = int(input('choice: '))
    if cho_run == 1:
        w2 = int(input('Width: '))
        h2 = int(input('Height: '))
        run_flag = 1
        ch_flag = 0
    elif cho_run == 2:
        while(flag==0):
            cho_bright = int(input('\n1.Average\n2.Lightness\n3.Luminosity\nEnter you choice: '))
            if cho_bright == 1:
                ch = 1
                flag = 1
                ch_falg = 0
                run_flag = 1
            elif cho_bright == 2:
                ch = 2
                flag = 1
                ch_flag = 0
                run_flag = 1
            elif cho_bright == 3:
                ch = 3
                flag = 1
                ch_flag = 0
                run_flag = 1
            else:
                print('Enter Valid Choice')
    elif cho_run == 4:
        if run_flag == 1:
            davinsci(pa,w2,h2,ch)
            print(ch)
            ch_flag = 1
    elif cho_run == 9:
        print(ch)
        davinsci(pa,w2,h2,ch)
        ch_flag = 1
    elif cho_run == 5:
        sys.exit()
    else:
        print('Enter Valid Choice')
        ch_flag = 0
