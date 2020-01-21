import neo

from ephyviewer import mkQApp, MainViewer, TraceViewer
import numpy as np

import mne


from cariboo import MneRawSource


def test_mne_raw_source():

    #reader = neo.MicromedIO(filename='File_micromed_1.TRC')
    vhdr_fname = './cariboo/test/signals/suj_0006_EEGAnna.vhdr'
    raw = mne.io.read_raw_brainvision(vhdr_fname, montage='standard_1020',  eog = ['EOG'], preload=True,)
    # raw.set_montage
    croped_raw = raw.crop(0, 10)

    source = MneRawSource(croped_raw)

    #you must first create a main Qt application (for event loop)
    app = mkQApp()

    win = MainViewer(show_auto_scale=True)

    view1 = TraceViewer(source=source, name='sigs')

    win.add_view(view1)


    #show main window and run Qapp
    win.show()


    app.exec_()





if __name__ == '__main__':
    test_mne_raw_source()
