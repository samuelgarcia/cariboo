import neo

from ephyviewer import mkQApp, MainViewer, TraceViewer
from ephyviewer import NeoAnalogSignalSource
import numpy as np

import mne
from mne.channels.layout import _find_topomap_coords

from cariboo import TopoEegViewer, MneRawSource

def test_open_topo_viewer():
    #~ reader = neo.MicromedIO(filename='File_micromed_1.TRC')
    #~ seg = reader.read_segment()
    #~ n_chan = seg.analogsignals[0].shape[1]
    #~ channel_positions = np.random.randn(n_chan, 2)
    #~ source = NeoAnalogSignalSource(seg.analogsignals[0])
    
    montage_name = 'standard_1020'

    vhdr_fname = 'small_BrainAmp.vhdr'
    raw = mne.io.read_raw_brainvision(vhdr_fname, montage=montage_name,  eog = ['EOG'], preload=True)
    raw = raw.pick('eeg')
    
    
    source = MneRawSource(raw)
    
    #~ montage = mne.channels.make_standard_montage('standard_1020')
    #~ print(montage)
    #~ pos = np.array(list(montage._get_ch_pos().values()))
    #~ print(pos)
    
    
    #~ n_chan = len(raw.info['ch_names'])
    #~ channel_positions = np.random.randn(n_chan, 2)
    channel_positions = _find_topomap_coords(raw.info, None)
    
    
    
    #you must first create a main Qt application (for event loop)
    app = mkQApp()

    win = MainViewer(show_auto_scale=True)

    view1 = TraceViewer(source=source, name='sigs')
    win.add_view(view1)

    view3 = TopoEegViewer(source=source, name='topo', channel_positions=channel_positions)
    win.add_view(view3)

    #show main window and run Qapp
    win.show()

    app.exec_()





if __name__ == '__main__':
    test_open_topo_viewer()
    
    