import wx
def encrypt(event):
    x = in_text.GetValue()
    ky = key.GetValue()
    x = x.replace(" ","")
    row_number = len(x)//len(ky)
    xList = [[0] * len(ky) for i in range(row_number+1)]
    count = 0
    for i in range(row_number+1):
        for j in range(len(ky)):
           if count == len(x):
                 break
           else:
                xList[i][j] = x[count]
                count += 1
    if ky.isalpha():
        count = 0
        y = list(x)
        ky = ky.lower()
        ky_order = sorted(list(ky))
        for t in ky_order:
            for s in range(row_number+1):
                if xList[s][ky.find(t)] != 0:
                    y[count] = xList[s][ky.find(t)]
                    count += 1
                else:
                    continue
        d = ''.join(y)
    elif ky.isdigit():
        count = 0
        y = list(x)
        ky_num = list(ky)
        for g in range(len(ky_num)):
            ky_num[g] = int(ky_num[g])
        for t in ky_num:
            for s in range(row_number+1):
                if xList[s][t-1] != 0:
                    y[count] = xList[s][t-1]
                    count += 1
                else:
                    continue
        d = ''.join(y)
    else:
        d = "请输入正确格式的密钥！"
    out_text.SetValue(d)
def decoding(event):
    text = in_text.GetValue()
    ky = key.GetValue()
    text = text.replace(" ","")
    if len(text)%len(ky) == 0:
        x = len(text)//len(ky)
    else:
        x = len(text)//len(ky)
        x += 1
    xList = [[0] * len(ky) for i in range(x)]
    count = 0
    if ky.isalpha():
        ky = ky.lower()
        ky_order = sorted(list(ky))   #count != len(text):
        for t in ky_order:
            for s in range(x):
                if ( s == x-1 & ky.find(t) in range(len(text)%len(ky),len(ky)) ):
                    continue
                else:
                    xList[s][ky.find(t)] = text[count]
                    count += 1
    elif ky.isdigit():
        ky_num = list(ky)
        for g in range(len(ky_num)):
            ky_num[g] = int(ky_num[g])
        for t in ky_num:
            for s in range(x):
                if ( s == x-1 & t-1 in range(len(text)%len(ky),len(ky)) ):
                    continue
                else:
                    xList[s][t - 1] = text[count]
                    count += 1
    else:
        out_text.SetValue("请输入正确格式的数字串或字母串！")
        return
    count = 0
    y = list(text)
    for i in range(x):
        for j in range(len(ky)):
            if xList[i][j] != 0:
                    y[count] = xList[i][j]
                    count += 1
    temp = ''.join(y)
    out_text.SetValue(temp)

app = wx.App()
win = wx.Frame(None,title="置换加密",size=(410,335))
bkg = wx.Panel(win)

aButton = wx.Button(bkg, label='加密')
aButton.Bind(wx.EVT_BUTTON, encrypt)
bButton = wx.Button(bkg, label='解密')
bButton.Bind(wx.EVT_BUTTON, decoding)
in_text = wx.TextCtrl(bkg, value="在这里输入加密文本", style=wx.TE_MULTILINE|wx.HSCROLL)
key = wx.TextCtrl(bkg)
out_text = wx.TextCtrl(bkg, style=wx.TE_MULTILINE|wx.HSCROLL)

hbox = wx.BoxSizer()    #Boxsizer默认为水平，VERTICAL为竖直,ADD的顺序就是在该方向上部件的排列顺序
hbox.Add(key, proportion=1, flag=wx.EXPAND)    #proportion决定窗口在改变大小时所获得的额外空间，若三个都为1则三等分
hbox.Add(aButton, proportion=0, flag=wx.LEFT, border=5)    #flag指的是边距，如wx.TOP就是指上边距
hbox.Add(bButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(in_text, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.TOP|wx.RIGHT, border=5)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
vbox.Add(out_text, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT, border=5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()

