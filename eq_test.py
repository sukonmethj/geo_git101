from obspy import read

st = read()
# st.plot()
st[1].spectrogram(log=True)

# Filter the waveform
tr = st[1].copy()
tr.filter('bandpass', freqmin=1.0, freqmax=5.0, corners=4, zerophase=True)
tr.plot()

tr.write('demo_eq.mseed', format='MSEED')

fig=tr.plot(show=False)
fig.savefig('demo_waveform.png', dpi=300)