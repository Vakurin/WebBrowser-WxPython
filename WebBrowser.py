import wx
import wx.html2
import wx.html


class WebBrowser(wx.Frame):
    go = []
    address = []
    browser = []
    history = []

    def GoButton(self, event):
        # pressing the jump button event
        print("pressing the jump button event")
        print(self.address.GetValue())
        self.browser.LoadURL(self.address.GetValue())  # load page, address is taken from the input line
        return

    def OnLoad(self, event):
        self.webtitle = self.browser.GetCurrentURL()
        self.history.InsertItems([self.webtitle], 0)

        return

    def NewWindow(self, event):
        # NEW Window open on right click!!!
        title = self.browser.GetCurrentTitle()
        self.SetTitle(title)
        second_window = WebBrowser(None, title=title)
        second_window.browser.LoadURL(event.URL)
        print(dir(event))
        print('URL', event.URL)
        second_window.Show()

    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, id=-1, title=title)  # components boxsize can work with object in form
        sizer = wx.BoxSizer(wx.VERTICAL)  # in our case vertical

        self.browser = wx.html2.WebView.New(self)  # Web Browser
        self.address = wx.TextCtrl(self, value="http://google.com")  # TextBox
        self.go = wx.Button(self, label="GO", id=wx.ID_OK)  # button
        self.history = wx.ListBox(self, size=(100, -1), style=wx.LB_SINGLE)

        # add objects in proportional placement
        sizer.Add(self.browser, proportion=80, flag=wx.EXPAND, border=10)
        sizer.Add(self.address, proportion=5, flag=wx.EXPAND, border=10)
        sizer.Add(self.go, proportion=5, flag=wx.EXPAND, border=10)
        sizer.Add(self.history, proportion=10, flag=wx.EXPAND, border=10)

        self.SetSizer(sizer)
        self.SetSize((1050, 750))

        self.Bind(wx.EVT_BUTTON, self.GoButton, self.go)  # connect event GoButton and button
        self.Bind(wx.html2.EVT_WEBVIEW_NAVIGATED, self.OnLoad, self.browser)
        self.Bind(wx.html2.EVT_WEBVIEW_NEWWINDOW, self.NewWindow, self.browser)


app = wx.App()
main_window = WebBrowser(None, "Web Browser")
main_window.browser.LoadURL("http://google.com")
main_window.Show()
app.MainLoop()

