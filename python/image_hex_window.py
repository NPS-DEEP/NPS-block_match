import tkinter 
from image_hex_table import ImageHexTable

class ImageHexWindow():
    """Provides a window to show a hex dump of specified bytes of a
    media image.

    To get back the window after being closed reselect an offset.
    """
    def __init__(self, master, identified_data, filters, offset_selection):
        """Args:
          master(a UI container): Parent.
          identified_data(IdentifiedData): Identified data about the scan.
          filters(Filters): Filters that impact the view.
          offset_selection(OffsetSelection): The selected offset.
        """
        # variables
        self._offset_selection = offset_selection

        # make toplevel window
        self._root_window = tkinter.Toplevel(master)
        self._root_window.title("Hex View")
        self._root_window.transient(master)
        self._root_window.protocol('WM_DELETE_WINDOW', self._close)

        # add the frame to contain the color legend
        # add the color legend
        f = tkinter.Frame(self._root_window)
        f.pack(side=tkinter.TOP, pady=4)
        tkinter.Label(f,text="   ",background="#660000").pack(side=tkinter.LEFT)
        tkinter.Label(f,text="Not filtered      ").pack(side=tkinter.LEFT)
        tkinter.Label(f,text="   ",background="#004400").pack(side=tkinter.LEFT)
        tkinter.Label(f,text="Filtered      ").pack(side=tkinter.LEFT)
        tkinter.Label(f,text="   ",background="#ccccff").pack(side=tkinter.LEFT)
        tkinter.Label(f,text="Not matched").pack(side=tkinter.LEFT)

        # add the frame to contain the image hex table
        image_hex_table = ImageHexTable(self._root_window,
                               identified_data, filters, offset_selection,
                                                width=88, height=32)
        image_hex_table.frame.pack(side=tkinter.TOP, anchor="w")

        # register to receive offset selection change events
        offset_selection.set_callback(self._handle_offset_selection)
        self._root_window.withdraw()

    def _handle_offset_selection(self, *args):
        # make visible if valid and not already visible
        if self._offset_selection.offset != -1:
            self._root_window.deiconify()

    def _close(self):
        self._root_window.withdraw()