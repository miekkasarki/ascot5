"""
Contains definition of IndexFrame class.

File: indexframe.py
"""
import tkinter
import a5py.ascot5io.ascot5tools as tools


class PlotFrame(tkinter.Frame):
    """
    An opening frame where other frames can be accessed and HDF5 file modified.
    """

    def __init__(self, gui):
        """
        Initialize index frame.

        Index frame contains text panel showing the path to the current file and
        a button to browse and load a new file. For each input parent a small
        panel is displayed, see function make_inputactivationframe().
        """
        super().__init__(gui._root)

        