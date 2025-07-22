#!/usr/bin/python3
#!/usr/bin/env python3

import os, sys
from PIL import Image

tdir = '.'
#trks = os.listdir(tdir)  # all
#trks = ['TestC15-Render','Test18-FlatGI']  # 
<trks = ['Sur4-BlueWinter','Sur8-BloCorcle','Wnt20-FirstSnow']  # 
size = 256, 256

for trk in trks:
    if trk.find('-') != -1:

        infile = trk+'/preview/view.jpg'
        #print(infile)
        outfile = '_previews/'+trk+'.jpg'
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.Resampling.LANCZOS)
            im.save(outfile, "JPEG", quality=95)
        except IOError:
            print('cannot create for: '+trk)
