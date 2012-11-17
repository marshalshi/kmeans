import main
import wx

class bucky(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "k-means", size = (360,120))
        self.panel = wx.Panel(self)

        wx.StaticText(self.panel, -1, 'file: ',(10,10))
        self.openfile = wx.TextCtrl(self.panel, -1, pos=(40,10), size=(250,-1))
        self.openbutton = wx.Button(self.panel, label = 'open', pos = (300,10), size= (50,-1))
        self.okbutton = wx.Button(self.panel, label= 'GO', pos=(300,60), size= (50,-1))
        wx.StaticText(self.panel, -1, 'the num of k: ', (10,60))
        self.text1 = wx.TextCtrl(self.panel, -1, pos=(100,60), size=(50,-1))

        self.Bind(wx.EVT_BUTTON, self.onopen, self.openbutton)
        self.Bind(wx.EVT_BUTTON, self.openf, self.okbutton)

        self.radio1 = wx.RadioButton(self.panel, -1, "randomChoose", pos=(170, 50), style=wx.RB_GROUP)
        self.radio2 = wx.RadioButton(self.panel, -1, "k-center", pos=(170, 70))
        self.radio3 = wx.RadioButton(self.panel, -1, "k-means++", pos=(170, 90))

    def openf(self, event):
        l = self.openfile.GetValue()
        k = self.text1.GetValue()
        if self.radio1.GetValue():
            text = 1
        elif self.radio2.GetValue():
            text = 2
        else:
            text = 3
        import os
        if os.path.exists(l) and l and k and k.isdigit() and int(k) >=0 and text:
            file = open(l)
            pts = []
            for line in file.readlines():
                line = line.split()
                pts.append(( int(line[0]), int(line[1])))
            file.close()
            if len(pts) >= int(k):
                main.main( l, int(k),text)
            else:
                box = wx.MessageDialog(None, 'your k is bigger than the num of pts!', 'wrong', wx.OK)
                if box.ShowModal() == wx.ID_OK:
                    box.Destroy()
                self.text1.Clear()
        else:
            box = wx.MessageDialog(None, 'you miss a file or write a wrong k', 'wrong', wx.OK)
            if box.ShowModal() == wx.ID_OK:
                box.Destroy()
            self.openfile.Clear()
            self.text1.Clear()

    def onopen(self, event):
        self.openfile.Clear()
        dialog = wx.FileDialog(None, 'open file', style = wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.file = dialog.GetPath()
            self.openfile.write(self.file)

if __name__=='__main__':
    app = wx.PySimpleApp()
    frame = bucky(None, -1)
    frame.Show()
    app.MainLoop()
