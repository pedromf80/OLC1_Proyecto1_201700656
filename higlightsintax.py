from tkinter import*

# dictionary to hold words and colors
highlightWords = {'if': 'green',
                  'else': 'red',
                  'while': 'blue',
                  'true': 'red',
                  'false': 'red',
                  'var': 'yellow',
                  'find': 'orange'
                  }

def highlighter(event):
    '''the highlight function, called when a Key-press event occurs'''
    for k,v in highlightWords.items(): # iterate over dict
        startIndex = '1.0'
        while True:
            startIndex = text.search(k, startIndex, END) # search for occurence of k
            if startIndex:
                endIndex = text.index('%s+%dc' % (startIndex, (len(k)))) # find end of k
                text.tag_add(k, startIndex, endIndex) # add tag to k
                text.tag_config(k, foreground=v)      # and color it with v
                startIndex = endIndex # reset startIndex to continue searching
            else:
                break

root = Tk()
text = Text(root)
text.pack()

text.bind('<Key>', highlighter) # bind key event to highlighter()

root.mainloop()