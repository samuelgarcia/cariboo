from ephyviewer.datasource import BaseAnalogSignalSource


class MneRawSource(BaseAnalogSignalSource):
    def __init__(self, raw):
        self.raw = raw

        self.sample_rate = self.raw.info['sfreq']

        self.with_scatter = False

    @property
    def nb_channel(self):
        ch_names = self.raw.ch_names
        n = len(ch_names)
        return n

    def get_channel_name(self, chan=0):
        ch_names = self.raw.info['ch_names']
        return ch_names[chan]

    @property
    def t_start(self):
        return self.raw.times[0]

    @property
    def t_stop(self):
        return self.raw.times[-1]

    def get_length(self):
        return self.raw.n_times

    def get_chunk(self, i_start=None, i_stop=None):
        self.raw.get_data(picks='all', start=i_start, stop=i_stop)
        print('call get_chunk')
