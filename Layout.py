#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Tue Sep 22 23:38:30 2015
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.derivation = wx.StaticText(self, wx.ID_ANY, _("0"))
        self.indicator_left = wx.StaticText(self, wx.ID_ANY, "")
        self.note = wx.StaticText(self, wx.ID_ANY, _("None"))
        self.indicator_right = wx.StaticText(self, wx.ID_ANY, "")
        self.freq = wx.StaticText(self, wx.ID_ANY, _("0 Hz"))
        self.choice = wx.Choice(self, wx.ID_ANY, choices=[])

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle(_("frame_1"))
        self.derivation.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOWFRAME))
        self.derivation.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, ""))
        self.indicator_left.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOWFRAME))
        self.indicator_left.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, ""))
        self.note.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOWFRAME))
        self.note.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.BOLD, 0, ""))
        self.indicator_right.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOWFRAME))
        self.indicator_right.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, ""))
        self.freq.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOWFRAME))
        self.freq.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        grid_sizer = wx.GridSizer(1, 3, 5, 15)
        sizer.Add(self.derivation, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer.Add(self.indicator_left, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer.Add(self.note, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer.Add(self.indicator_right, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer.Add(grid_sizer, 1, wx.EXPAND, 0)
        sizer.Add(self.freq, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer.Add(self.choice, 0, wx.LEFT, 5)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MainFrame
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame = MainFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()