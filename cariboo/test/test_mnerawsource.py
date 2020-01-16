import neo

from ephyviewer import mkQApp, MainViewer, TraceViewer
import numpy as np

import mne


from cariboo import MneRawSource


def test_mne_raw_source():

    reader = neo.MicromedIO(filename='File_micromed_1.TRC')
    #~ print(reader)
    seg = reader.read_segment()
    
    filename='File_micromed_1.TRC'
    
    raw = 
    
    source = MneRawSource(raw)

    #you must first create a main Qt application (for event loop)
    app = mkQApp()

    win = MainViewer(show_auto_scale=True)

    source = NeoAnalogSignalSource(seg.analogsignals[0])

    view1 = TraceViewer(source=source, name='sigs')
    win.add_view(view1)


    #show main window and run Qapp
    win.show()


    app.exec_()





if __name__ == '__main__':
    test_open_topo_viewer()
    
    