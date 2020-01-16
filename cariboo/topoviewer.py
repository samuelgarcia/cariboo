from ephyviewer.base import ViewerBase, QT


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import mne.viz


class TopoEegViewer(ViewerBase):
    def __init__(self, name='', source=None, channel_positions=None):
        """
        
        
        """
        ViewerBase.__init__(self, name=name, source=source)

        mainlayout = QT.QVBoxLayout()
        self.setLayout(mainlayout)

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        
        mainlayout.addWidget(self.canvas)
        
        self.channel_positions = channel_positions
        
        
    def refresh(self):
        #~ print(self.t)
        t_start = self.t - 0.02
        t_stop = self.t + 0.02
        
        i_start, i_stop = self.source.time_to_index(t_start), self.source.time_to_index(t_stop) + 2
        sigs_chunk = self.source.get_chunk(i_start=i_start, i_stop=i_stop)
        data = sigs_chunk.mean(axis=0)
        self.ax.clear()
        mne.viz.plot_topomap(data, self.channel_positions, axes=self.ax, show=False)
        
        self.canvas.draw()


