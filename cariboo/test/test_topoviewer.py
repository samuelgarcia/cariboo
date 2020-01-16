import neo

from ephyviewer import mkQApp, MainViewer, TraceViewer
from ephyviewer import NeoAnalogSignalSource
import numpy as np



from cariboo import TopoEegViewer


def test_open_topo_viewer():
    reader = neo.MicromedIO(filename='File_micromed_1.TRC')
    #~ print(reader)
    seg = reader.read_segment()

    n_chan = seg.analogsignals[0].shape[1]
    
    channel_positions = np.random.randn(n_chan, 2)

    #you must first create a main Qt application (for event loop)
    app = mkQApp()

    win = MainViewer(show_auto_scale=True)

    source = NeoAnalogSignalSource(seg.analogsignals[0])

    #~ view1 = TraceViewer(source=source, name='sigs')
    #~ win.add_view(view1)


    view3 = TopoEegViewer(source=source, name='topo', channel_positions=channel_positions)
    win.add_view(view3)

    #show main window and run Qapp
    win.show()


    app.exec_()





if __name__ == '__main__':
    test_open_topo_viewer()
    
    