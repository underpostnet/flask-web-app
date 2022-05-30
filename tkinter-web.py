



# Import tkinter and webview libraries
import tkinter
import webview

# define an instance of tkinter

root = tkinter.Tk()

#  size of the window where we show our website
root.geometry("800x450")

# Open website
webview.create_window('underpost.net', 'http://localhost:5000')
webview.start()
