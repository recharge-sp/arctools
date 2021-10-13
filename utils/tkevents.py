def selectall(event):
    event.widget.tag_add("sel","1.0","end")
    event.widget.mark_set("insert", "end")
    return 'break'