from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import DatetimeTickFormatter
from datetime import datetime
import webbrowser
import os

def parse_data(file_content):
    timestamps = []
    speeds = []
    
    lines = file_content.split('\n')
    current_timestamp = None
    
    for line in lines:
        if line.startswith('Timestamp:'):
            current_timestamp = datetime.strptime(line.split(': ')[1].strip(), '%Y-%m-%d %H:%M:%S')
        elif current_timestamp and 'sender' in line and '  5]   0.00-' in line:
            try:
                speed_parts = line.split('Mbits/sec')[0].split()
                speed = float(speed_parts[-1])
                timestamps.append(current_timestamp)
                speeds.append(speed)
                current_timestamp = None
            except:
                continue
    
    return timestamps, speeds

def create_chart(timestamps, speeds):
    p = figure(
        title='Testing Jaringan',
        x_axis_type='datetime',
        width=800,
        height=400
    )
    
    p.line(
        timestamps,
        speeds,
        line_color='blue',
        line_width=2
    )
    
    p.xaxis.axis_label = 'DATE TIME'
    p.yaxis.axis_label = 'Speed (Mbps)'
    
    p.xaxis.formatter = DatetimeTickFormatter(
        hours="%H:%M",
        days="%d/%m %H:%M",
        months="%m/%Y"
    )
    
    p.title.text_font_size = '14pt'
    p.grid.grid_line_alpha = 0.3
    p.xgrid.grid_line_dash = 'dashed'
    p.ygrid.grid_line_dash = 'dashed'
    
    return p

# Main execution
def main():
    try:
        # Baca file
        file_content = '''Timestamp: 2024-07-30 10:23:42
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 49996 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   197 KBytes  1.61 Mbits/sec    0   34.1 KBytes       
[  5]   1.00-2.00   sec  0.00 Bytes  0.00 bits/sec    0   36.8 KBytes       
[  5]   2.00-3.00   sec  94.5 KBytes   774 Kbits/sec    0   39.4 KBytes       
[  5]   3.00-4.00   sec  86.6 KBytes   710 Kbits/sec    0   52.5 KBytes       
[  5]   4.00-5.00   sec   214 KBytes  1.75 Mbits/sec    0   66.9 KBytes       
[  5]   5.00-6.00   sec  0.00 Bytes  0.00 bits/sec    0   87.9 KBytes       
[  5]   6.00-7.00   sec   126 KBytes  1.03 Mbits/sec    0   98.4 KBytes       
[  5]   7.00-8.00   sec   189 KBytes  1.55 Mbits/sec    0    131 KBytes       
[  5]   8.00-9.00   sec  0.00 Bytes  0.00 bits/sec    0    177 KBytes       
[  5]   9.00-10.00  sec   252 KBytes  2.06 Mbits/sec    0    210 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.13 MBytes   949 Kbits/sec    0             sender
[  5]   0.00-12.24  sec   843 KBytes   564 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-30 11:23:53
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 51612 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  2.79 MBytes  23.4 Mbits/sec    0    151 KBytes       
[  5]   1.00-2.00   sec  8.92 MBytes  74.8 Mbits/sec    0    553 KBytes       
[  5]   2.00-3.00   sec  11.8 MBytes  98.6 Mbits/sec    0   1.04 MBytes       
[  5]   3.00-4.00   sec  9.98 MBytes  83.7 Mbits/sec   53   1.03 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.14 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.24 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.32 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.38 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.42 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.45 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  97.2 MBytes  81.5 Mbits/sec   53             sender
[  5]   0.00-10.18  sec  95.6 MBytes  78.8 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-30 12:24:04
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 58764 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.28 MBytes  10.7 Mbits/sec    0    101 KBytes       
[  5]   1.00-2.00   sec  2.40 MBytes  20.1 Mbits/sec    0    213 KBytes       
[  5]   2.00-3.00   sec  4.86 MBytes  40.8 Mbits/sec    0    434 KBytes       
[  5]   3.00-4.00   sec  8.37 MBytes  70.2 Mbits/sec    0    807 KBytes       
[  5]   4.00-5.00   sec  11.5 MBytes  96.1 Mbits/sec    0   1.33 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.86 MBytes       
[  5]   6.00-7.00   sec  8.75 MBytes  73.4 Mbits/sec   96   1.59 MBytes       
[  5]   7.00-8.00   sec  12.5 MBytes   105 Mbits/sec   65   1.17 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.24 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.28 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  82.1 MBytes  68.9 Mbits/sec  161             sender
[  5]   0.00-10.14  sec  79.7 MBytes  65.9 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-30 13:24:15
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 58916 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   114 KBytes   935 Kbits/sec    0   31.5 KBytes       
[  5]   1.00-2.00   sec   240 KBytes  1.97 Mbits/sec    0   40.7 KBytes       
[  5]   2.00-3.00   sec   539 KBytes  4.42 Mbits/sec    0   66.9 KBytes       
[  5]   3.00-4.00   sec   756 KBytes  6.19 Mbits/sec    0   99.8 KBytes       
[  5]   4.00-5.00   sec  1.05 MBytes  8.77 Mbits/sec    0    148 KBytes       
[  5]   5.00-6.00   sec  1.60 MBytes  13.4 Mbits/sec    0    219 KBytes       
[  5]   6.00-7.00   sec  3.63 MBytes  30.4 Mbits/sec    0    387 KBytes       
[  5]   7.00-8.00   sec  5.17 MBytes  43.4 Mbits/sec    0    614 KBytes       
[  5]   8.00-9.00   sec  4.12 MBytes  34.6 Mbits/sec    0    806 KBytes       
[  5]   9.00-10.00  sec  7.71 MBytes  64.7 Mbits/sec    0   1.10 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  24.9 MBytes  20.9 Mbits/sec    0             sender
[  5]   0.00-10.12  sec  22.6 MBytes  18.8 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-30 14:24:31
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 43470 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   164 KBytes  1.34 Mbits/sec    0   34.1 KBytes       
[  5]   1.00-2.00   sec   192 KBytes  1.57 Mbits/sec    0   40.7 KBytes       
[  5]   2.00-3.00   sec  93.2 KBytes   763 Kbits/sec    0   45.9 KBytes       
[  5]   3.00-4.00   sec  86.6 KBytes   710 Kbits/sec    0   51.2 KBytes       
[  5]   4.00-5.00   sec   207 KBytes  1.70 Mbits/sec    0   68.2 KBytes       
[  5]   5.00-6.00   sec   126 KBytes  1.03 Mbits/sec    0   99.8 KBytes       
[  5]   6.00-7.00   sec   189 KBytes  1.55 Mbits/sec    0    129 KBytes       
[  5]   7.00-8.00   sec   189 KBytes  1.55 Mbits/sec    0    169 KBytes       
[  5]   8.00-9.00   sec   567 KBytes  4.65 Mbits/sec    0    269 KBytes       
[  5]   9.00-10.00  sec  0.00 Bytes  0.00 bits/sec    0    344 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.77 MBytes  1.49 Mbits/sec    0             sender
[  5]   0.00-12.23  sec  1.46 MBytes  1.00 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-30 15:24:41
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 48862 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   700 KBytes  5.73 Mbits/sec    0   59.1 KBytes       
[  5]   1.00-2.00   sec  1.98 MBytes  16.6 Mbits/sec    0    150 KBytes       
[  5]   2.00-3.00   sec  1.35 MBytes  11.4 Mbits/sec    0    210 KBytes       
[  5]   3.00-4.00   sec  2.58 MBytes  21.7 Mbits/sec    0    322 KBytes       
[  5]   4.00-5.00   sec  4.49 MBytes  37.7 Mbits/sec    0    520 KBytes       
[  5]   5.00-6.00   sec  6.15 MBytes  51.6 Mbits/sec    0    808 KBytes       
[  5]   6.00-7.00   sec  8.96 MBytes  75.2 Mbits/sec    0   1.17 MBytes       
[  5]   7.00-8.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.52 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.99 MBytes       
[  5]   9.00-10.00  sec  8.75 MBytes  73.4 Mbits/sec  206   1.12 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  51.2 MBytes  43.0 Mbits/sec  206             sender
[  5]   0.00-10.15  sec  50.9 MBytes  42.0 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-30 16:24:52
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 35320 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  3.35 MBytes  28.1 Mbits/sec    0    176 KBytes       
[  5]   1.00-2.00   sec  8.00 MBytes  67.1 Mbits/sec    0    536 KBytes       
[  5]   2.00-3.00   sec  10.3 MBytes  86.7 Mbits/sec    0   1005 KBytes       
[  5]   3.00-4.00   sec  11.1 MBytes  93.5 Mbits/sec    0   1.49 MBytes       
[  5]   4.00-5.00   sec  8.75 MBytes  73.4 Mbits/sec    0   1.94 MBytes       
[  5]   5.00-6.00   sec  8.75 MBytes  73.4 Mbits/sec   87   1.64 MBytes       
[  5]   6.00-7.00   sec  12.5 MBytes   105 Mbits/sec   70   1.20 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.27 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.32 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.36 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  94.1 MBytes  78.9 Mbits/sec  157             sender
[  5]   0.00-10.18  sec  91.9 MBytes  75.8 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-30 17:25:03
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 38520 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   260 KBytes  2.13 Mbits/sec    0   35.4 KBytes       
[  5]   1.00-2.00   sec   887 KBytes  7.27 Mbits/sec    0   74.8 KBytes       
[  5]   2.00-3.00   sec  2.71 MBytes  22.7 Mbits/sec    0    200 KBytes       
[  5]   3.00-4.00   sec  1.72 MBytes  14.5 Mbits/sec    0    280 KBytes       
[  5]   4.00-5.00   sec  2.40 MBytes  20.1 Mbits/sec    0    391 KBytes       
[  5]   5.00-6.00   sec  4.55 MBytes  38.2 Mbits/sec    0    588 KBytes       
[  5]   6.00-7.00   sec  6.77 MBytes  56.8 Mbits/sec    0    910 KBytes       
[  5]   7.00-8.00   sec  8.30 MBytes  69.6 Mbits/sec    0   1.25 MBytes       
[  5]   8.00-9.00   sec  5.00 MBytes  41.9 Mbits/sec    0   1.49 MBytes       
[  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0   1.84 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  38.8 MBytes  32.6 Mbits/sec    0             sender
[  5]   0.00-10.20  sec  38.1 MBytes  31.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-30 18:25:15
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 57322 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   365 KBytes  2.99 Mbits/sec    0   40.7 KBytes       
[  5]   1.00-2.00   sec   324 KBytes  2.66 Mbits/sec    0   56.4 KBytes       
[  5]   2.00-3.00   sec   284 KBytes  2.32 Mbits/sec    0   68.2 KBytes       
[  5]   3.00-4.00   sec   252 KBytes  2.06 Mbits/sec    0   81.4 KBytes       
[  5]   4.00-5.00   sec   378 KBytes  3.10 Mbits/sec    0   98.4 KBytes       
[  5]   5.00-6.00   sec   441 KBytes  3.61 Mbits/sec    0    119 KBytes       
[  5]   6.00-7.00   sec   378 KBytes  3.10 Mbits/sec    0    171 KBytes       
[  5]   7.00-8.00   sec   819 KBytes  6.71 Mbits/sec    0    243 KBytes       
[  5]   8.00-9.00   sec   378 KBytes  3.10 Mbits/sec    0    327 KBytes       
[  5]   9.00-10.00  sec   819 KBytes  6.71 Mbits/sec    0    446 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  4.33 MBytes  3.64 Mbits/sec    0             sender
[  5]   0.00-10.54  sec  3.91 MBytes  3.11 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-30 19:25:33
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 58756 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    0   17.1 KBytes       
[  5]   1.00-2.00   sec  68.2 KBytes   559 Kbits/sec    0   31.5 KBytes       
[  5]   2.00-3.00   sec  0.00 Bytes  0.00 bits/sec    0   32.8 KBytes       
[  5]   3.00-4.00   sec  65.6 KBytes   538 Kbits/sec    0   34.1 KBytes       
[  5]   4.00-5.00   sec  0.00 Bytes  0.00 bits/sec    0   38.1 KBytes       
[  5]   5.00-6.00   sec  89.2 KBytes   732 Kbits/sec    0   48.6 KBytes       
[  5]   6.00-7.00   sec  0.00 Bytes  0.00 bits/sec    0   59.1 KBytes       
[  5]   7.00-8.00   sec   129 KBytes  1.05 Mbits/sec    0   69.6 KBytes       
[  5]   8.00-9.00   sec  0.00 Bytes  0.00 bits/sec    0   82.7 KBytes       
[  5]   9.00-10.00  sec  0.00 Bytes  0.00 bits/sec    0   95.8 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   396 KBytes   325 Kbits/sec    0             sender
[  5]   0.00-13.11  sec   298 KBytes   186 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-30 20:25:52
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 55802 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    2   15.8 KBytes       
[  5]   1.00-2.00   sec  69.6 KBytes   570 Kbits/sec    0   31.5 KBytes       
[  5]   2.00-3.00   sec  85.3 KBytes   699 Kbits/sec    0   32.8 KBytes       
[  5]   3.00-4.00   sec  0.00 Bytes  0.00 bits/sec    0   35.4 KBytes       
[  5]   4.00-5.00   sec  0.00 Bytes  0.00 bits/sec    0   48.6 KBytes       
[  5]   5.00-6.00   sec   230 KBytes  1.88 Mbits/sec    0   76.1 KBytes       
[  5]   6.00-7.00   sec   126 KBytes  1.03 Mbits/sec    0   98.4 KBytes       
[  5]   7.00-8.00   sec   189 KBytes  1.55 Mbits/sec    0    119 KBytes       
[  5]   8.00-9.00   sec  0.00 Bytes  0.00 bits/sec    0    148 KBytes       
[  5]   9.00-10.00  sec   252 KBytes  2.07 Mbits/sec    0    189 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   996 KBytes   816 Kbits/sec    2             sender
[  5]   0.00-13.62  sec   656 KBytes   395 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-30 21:26:24
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 60854 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    3   28.9 KBytes       
[  5]   1.00-2.00   sec  82.7 KBytes   678 Kbits/sec    0   31.5 KBytes       
[  5]   2.00-3.00   sec  0.00 Bytes  0.00 bits/sec    0   31.5 KBytes       
[  5]   3.00-4.00   sec  91.9 KBytes   753 Kbits/sec    0   36.8 KBytes       
[  5]   4.00-5.00   sec  0.00 Bytes  0.00 bits/sec    0   47.2 KBytes       
[  5]   5.00-6.00   sec  78.8 KBytes   646 Kbits/sec    0   60.4 KBytes       
[  5]   6.00-7.00   sec  0.00 Bytes  0.00 bits/sec    0   65.6 KBytes       
[  5]   7.00-8.00   sec   126 KBytes  1.03 Mbits/sec    0   86.6 KBytes       
[  5]   8.00-9.00   sec  0.00 Bytes  0.00 bits/sec    0   93.2 KBytes       
[  5]   9.00-10.00  sec   189 KBytes  1.55 Mbits/sec    0    129 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   613 KBytes   502 Kbits/sec    3             sender
[  5]   0.00-13.65  sec   385 KBytes   231 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-30 22:26:35
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 33928 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   265 KBytes  2.17 Mbits/sec    0   36.8 KBytes       
[  5]   1.00-2.00   sec  1.23 MBytes  10.3 Mbits/sec    0   94.5 KBytes       
[  5]   2.00-3.00   sec  3.51 MBytes  29.4 Mbits/sec    0    259 KBytes       
[  5]   3.00-4.00   sec  7.63 MBytes  64.0 Mbits/sec    0    598 KBytes       
[  5]   4.00-5.00   sec  10.2 MBytes  85.2 Mbits/sec    0   1.03 MBytes       
[  5]   5.00-6.00   sec  6.23 MBytes  52.3 Mbits/sec    0   1.35 MBytes       
[  5]   6.00-7.00   sec  8.75 MBytes  73.4 Mbits/sec   28   1.07 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.18 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.27 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.33 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  69.0 MBytes  57.9 Mbits/sec   28             sender
[  5]   0.00-10.13  sec  67.0 MBytes  55.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-30 23:26:46
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 42178 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.4 MBytes  95.9 Mbits/sec    0    751 KBytes       
[  5]   1.00-2.00   sec  12.2 MBytes   103 Mbits/sec    0   1.28 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.80 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec   67   1.57 MBytes       
[  5]   4.00-5.00   sec  12.5 MBytes   105 Mbits/sec   23   1.70 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.85 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.96 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.05 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.12 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    6   1.55 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  90.1 Mbits/sec   96             sender
[  5]   0.00-10.19  sec   106 MBytes  87.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 00:26:56
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 44558 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  7.21 MBytes  60.5 Mbits/sec    0    360 KBytes       
[  5]   1.00-2.00   sec  12.3 MBytes   103 Mbits/sec    0    891 KBytes       
[  5]   2.00-3.00   sec  10.8 MBytes  90.6 Mbits/sec    0   1.40 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.92 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec   82   1.58 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec   58   1.17 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.23 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.28 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.31 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   104 MBytes  87.3 Mbits/sec  140             sender
[  5]   0.00-10.17  sec   102 MBytes  84.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 01:27:07
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 55196 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.2 MBytes   102 Mbits/sec    0    681 KBytes       
[  5]   1.00-2.00   sec  11.6 MBytes  97.4 Mbits/sec    0   1.19 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.72 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    1   2.24 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec   78   1.67 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.82 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.94 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.04 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.11 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec  129   1.05 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.2 Mbits/sec  208             sender
[  5]   0.00-10.15  sec   105 MBytes  86.8 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 02:27:18
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 46066 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.8 MBytes  99.3 Mbits/sec    0    770 KBytes       
[  5]   1.00-2.00   sec  12.3 MBytes   103 Mbits/sec    0   1.28 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.81 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec  117   1.57 MBytes       
[  5]   4.00-5.00   sec  12.5 MBytes   105 Mbits/sec  601   1.15 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.22 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.27 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.30 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.32 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.5 Mbits/sec  718             sender
[  5]   0.00-10.17  sec   106 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 03:27:29
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 48514 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.8 MBytes  99.3 Mbits/sec    0    654 KBytes       
[  5]   1.00-2.00   sec  11.3 MBytes  94.6 Mbits/sec    0   1.16 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.69 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.22 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec   81   1.14 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.21 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.26 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.29 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.32 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.33 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.7 Mbits/sec   81             sender
[  5]   0.00-10.17  sec   106 MBytes  87.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 04:27:39
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 49312 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  7.69 MBytes  64.5 Mbits/sec    0    373 KBytes       
[  5]   1.00-2.00   sec  11.9 MBytes  99.6 Mbits/sec    0    911 KBytes       
[  5]   2.00-3.00   sec  10.8 MBytes  90.6 Mbits/sec    0   1.42 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.94 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec   91   1.34 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec  179   1.17 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.24 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.28 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.31 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   104 MBytes  87.3 Mbits/sec  270             sender
[  5]   0.00-10.17  sec   103 MBytes  84.8 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 05:27:50
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 48552 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.9 MBytes   100 Mbits/sec    0    786 KBytes       
[  5]   1.00-2.00   sec  11.2 MBytes  93.9 Mbits/sec    0   1.29 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.82 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec   77   1.57 MBytes       
[  5]   4.00-5.00   sec  12.5 MBytes   105 Mbits/sec    4   1.70 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.85 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.96 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.05 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.12 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec   89   1.05 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.7 Mbits/sec  170             sender
[  5]   0.00-10.15  sec   106 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 06:28:01
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 50876 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.2 MBytes  93.9 Mbits/sec    0    642 KBytes       
[  5]   1.00-2.00   sec  12.0 MBytes   100 Mbits/sec    0   1.15 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.68 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.21 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  250    814 KBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0    869 KBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0    907 KBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0    932 KBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0    945 KBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0    952 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.7 Mbits/sec  250             sender
[  5]   0.00-10.14  sec   105 MBytes  87.1 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 07:28:12
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 60388 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.7 MBytes  97.8 Mbits/sec    0    665 KBytes       
[  5]   1.00-2.00   sec  12.4 MBytes   104 Mbits/sec    0   1.18 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.71 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.23 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec   84   1.67 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.82 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.94 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.04 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.11 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    8   1.51 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.4 Mbits/sec   92             sender
[  5]   0.00-10.19  sec   106 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 08:28:22
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 43752 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.3 MBytes   103 Mbits/sec    0    769 KBytes       
[  5]   1.00-2.00   sec  11.2 MBytes  93.9 Mbits/sec    0   1.28 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.81 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec   71   1.57 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec  484   1.15 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.22 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.27 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.30 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.32 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.34 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  91.0 Mbits/sec  555             sender
[  5]   0.00-10.18  sec   106 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 09:28:33
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 49924 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.6 MBytes  97.5 Mbits/sec    0    601 KBytes       
[  5]   1.00-2.00   sec  11.7 MBytes  98.1 Mbits/sec    0   1.12 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.62 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.15 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  220   1.12 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.19 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.25 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.29 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.32 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  89.8 Mbits/sec  220             sender
[  5]   0.00-10.17  sec   106 MBytes  87.2 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 10:28:44
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 46344 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   471 KBytes  3.86 Mbits/sec    0   47.2 KBytes       
[  5]   1.00-2.00   sec  1.68 MBytes  14.1 Mbits/sec    0    119 KBytes       
[  5]   2.00-3.00   sec  1.23 MBytes  10.3 Mbits/sec    0    181 KBytes       
[  5]   3.00-4.00   sec  1.29 MBytes  10.8 Mbits/sec    0    240 KBytes       
[  5]   4.00-5.00   sec   945 KBytes  7.74 Mbits/sec    0    284 KBytes       
[  5]   5.00-6.00   sec  1.11 MBytes  9.29 Mbits/sec    0    332 KBytes       
[  5]   6.00-7.00   sec   882 KBytes  7.22 Mbits/sec    0    378 KBytes       
[  5]   7.00-8.00   sec  1.42 MBytes  11.9 Mbits/sec    0    444 KBytes       
[  5]   8.00-9.00   sec  3.63 MBytes  30.5 Mbits/sec    0    605 KBytes       
[  5]   9.00-10.00  sec  6.77 MBytes  56.8 Mbits/sec    0    899 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  19.4 MBytes  16.2 Mbits/sec    0             sender
[  5]   0.00-10.17  sec  17.9 MBytes  14.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 11:09:18
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 47040 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   381 KBytes  3.12 Mbits/sec    0   42.0 KBytes       
[  5]   1.00-2.00   sec   169 KBytes  1.39 Mbits/sec    0   52.5 KBytes       
[  5]   2.00-3.00   sec   160 KBytes  1.31 Mbits/sec    0   57.8 KBytes       
[  5]   3.00-4.00   sec  73.5 KBytes   602 Kbits/sec    0   63.0 KBytes       
[  5]   4.00-5.00   sec   388 KBytes  3.18 Mbits/sec    0   81.4 KBytes       
[  5]   5.00-6.00   sec   567 KBytes  4.64 Mbits/sec    0    122 KBytes       
[  5]   6.00-7.00   sec   378 KBytes  3.10 Mbits/sec    0    164 KBytes       
[  5]   7.00-8.00   sec   567 KBytes  4.65 Mbits/sec    0    240 KBytes       
[  5]   8.00-9.00   sec   693 KBytes  5.68 Mbits/sec    0    328 KBytes       
[  5]   9.00-10.00  sec   945 KBytes  7.74 Mbits/sec    0    453 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  4.22 MBytes  3.54 Mbits/sec    0             sender
[  5]   0.00-10.53  sec  3.66 MBytes  2.91 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 12:09:30
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 37668 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.88 MBytes  15.8 Mbits/sec    0    113 KBytes       
[  5]   1.00-2.00   sec  2.65 MBytes  22.2 Mbits/sec    0    234 KBytes       
[  5]   2.00-3.00   sec  3.75 MBytes  31.5 Mbits/sec    0    395 KBytes       
[  5]   3.00-4.00   sec  5.41 MBytes  45.4 Mbits/sec    0    656 KBytes       
[  5]   4.00-5.00   sec  8.49 MBytes  71.2 Mbits/sec    0   1013 KBytes       
[  5]   5.00-6.00   sec  9.96 MBytes  83.6 Mbits/sec   34    983 KBytes       
[  5]   6.00-7.00   sec  5.00 MBytes  41.9 Mbits/sec    0   1.05 MBytes       
[  5]   7.00-8.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.16 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.24 MBytes       
[  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0   1.29 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  60.9 MBytes  51.1 Mbits/sec   34             sender
[  5]   0.00-10.65  sec  59.6 MBytes  46.9 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 16:16:31
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 45142 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.25 MBytes  10.5 Mbits/sec    0   84.0 KBytes       
[  5]   1.00-2.00   sec  1.66 MBytes  13.9 Mbits/sec    0    158 KBytes       
[  5]   2.00-3.00   sec  2.34 MBytes  19.6 Mbits/sec    0    269 KBytes       
[  5]   3.00-4.00   sec  3.26 MBytes  27.3 Mbits/sec    0    411 KBytes       
[  5]   4.00-5.00   sec  1.60 MBytes  13.4 Mbits/sec    0    487 KBytes       
[  5]   5.00-6.00   sec   630 KBytes  5.16 Mbits/sec    0    503 KBytes       
[  5]   6.00-7.00   sec  0.00 Bytes  0.00 bits/sec    0    507 KBytes       
[  5]   7.00-8.00   sec  0.00 Bytes  0.00 bits/sec    0    509 KBytes       
[  5]   8.00-9.00   sec  0.00 Bytes  0.00 bits/sec    0    520 KBytes       
[  5]   9.00-10.00  sec  0.00 Bytes  0.00 bits/sec    0    525 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  10.7 MBytes  9.00 Mbits/sec    0             sender
[  5]   0.00-13.52  sec  10.2 MBytes  6.31 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 17:16:50
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 57088 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   163 KBytes  1.33 Mbits/sec    0   32.8 KBytes       
[  5]   1.00-2.00   sec  84.0 KBytes   688 Kbits/sec    0   36.8 KBytes       
[  5]   2.00-3.00   sec  94.5 KBytes   774 Kbits/sec    0   42.0 KBytes       
[  5]   3.00-4.00   sec   173 KBytes  1.42 Mbits/sec    0   49.9 KBytes       
[  5]   4.00-5.00   sec  72.2 KBytes   591 Kbits/sec    0   60.4 KBytes       
[  5]   5.00-6.00   sec   126 KBytes  1.03 Mbits/sec    0   91.9 KBytes       
[  5]   6.00-7.00   sec   315 KBytes  2.58 Mbits/sec    0    135 KBytes       
[  5]   7.00-8.00   sec  0.00 Bytes  0.00 bits/sec    0    160 KBytes       
[  5]   8.00-9.00   sec   252 KBytes  2.06 Mbits/sec    0    194 KBytes       
[  5]   9.00-10.00  sec   315 KBytes  2.58 Mbits/sec    0    251 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.56 MBytes  1.31 Mbits/sec    0             sender
[  5]   0.00-12.03  sec  1.04 MBytes   725 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 18:17:01
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 49448 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   537 KBytes  4.40 Mbits/sec    0   48.6 KBytes       
[  5]   1.00-2.00   sec   996 KBytes  8.16 Mbits/sec    0   95.8 KBytes       
[  5]   2.00-3.00   sec  1.97 MBytes  16.5 Mbits/sec    0    182 KBytes       
[  5]   3.00-4.00   sec  3.94 MBytes  33.0 Mbits/sec    0    358 KBytes       
[  5]   4.00-5.00   sec  3.63 MBytes  30.4 Mbits/sec    0    528 KBytes       
[  5]   5.00-6.00   sec  5.11 MBytes  42.8 Mbits/sec    0    744 KBytes       
[  5]   6.00-7.00   sec  4.92 MBytes  41.3 Mbits/sec    0    979 KBytes       
[  5]   7.00-8.00   sec  6.15 MBytes  51.6 Mbits/sec    0   1.26 MBytes       
[  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.56 MBytes       
[  5]   9.00-10.00  sec  8.75 MBytes  73.4 Mbits/sec    0   1.97 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  42.2 MBytes  35.4 Mbits/sec    0             sender
[  5]   0.00-10.25  sec  40.8 MBytes  33.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 19:17:24
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 60036 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    1   13.1 KBytes       
[  5]   1.00-2.00   sec  0.00 Bytes  0.00 bits/sec    0   22.3 KBytes       
[  5]   2.00-3.00   sec  70.9 KBytes   581 Kbits/sec    0   31.5 KBytes       
[  5]   3.00-4.00   sec  0.00 Bytes  0.00 bits/sec    0   32.8 KBytes       
[  5]   4.00-5.00   sec  0.00 Bytes  0.00 bits/sec    0   36.8 KBytes       
[  5]   5.00-6.00   sec  85.3 KBytes   699 Kbits/sec    0   42.0 KBytes       
[  5]   6.00-7.00   sec  0.00 Bytes  0.00 bits/sec    0   48.6 KBytes       
[  5]   7.00-8.00   sec  0.00 Bytes  0.00 bits/sec    0   56.4 KBytes       
[  5]   8.00-9.00   sec  74.8 KBytes   613 Kbits/sec    0   61.7 KBytes       
[  5]   9.00-10.00  sec  0.00 Bytes  0.00 bits/sec    0   69.6 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   276 KBytes   226 Kbits/sec    1             sender
[  5]   0.00-14.76  sec   178 KBytes  99.1 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 21:18:01
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 57842 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   268 KBytes  2.19 Mbits/sec    0   39.4 KBytes       
[  5]   1.00-2.00   sec   184 KBytes  1.51 Mbits/sec    0   45.9 KBytes       
[  5]   2.00-3.00   sec   165 KBytes  1.35 Mbits/sec    0   55.1 KBytes       
[  5]   3.00-4.00   sec   538 KBytes  4.41 Mbits/sec    0   74.8 KBytes       
[  5]   4.00-5.00   sec   126 KBytes  1.03 Mbits/sec    0   85.3 KBytes       
[  5]   5.00-6.00   sec   567 KBytes  4.65 Mbits/sec    0    126 KBytes       
[  5]   6.00-7.00   sec   378 KBytes  3.10 Mbits/sec    0    160 KBytes       
[  5]   7.00-8.00   sec   252 KBytes  2.06 Mbits/sec    0    210 KBytes       
[  5]   8.00-9.00   sec   315 KBytes  2.58 Mbits/sec    0    294 KBytes       
[  5]   9.00-10.00  sec   378 KBytes  3.10 Mbits/sec    0    396 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  3.10 MBytes  2.60 Mbits/sec    0             sender
[  5]   0.00-10.92  sec  2.71 MBytes  2.08 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 22:18:21
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 45948 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    0   21.0 KBytes       
[  5]   1.00-2.00   sec  65.6 KBytes   538 Kbits/sec    0   31.5 KBytes       
[  5]   2.00-3.00   sec  64.3 KBytes   527 Kbits/sec    0   34.1 KBytes       
[  5]   3.00-4.00   sec   108 KBytes   882 Kbits/sec    0   38.1 KBytes       
[  5]   4.00-5.00   sec   251 KBytes  2.05 Mbits/sec    0   52.5 KBytes       
[  5]   5.00-6.00   sec  98.4 KBytes   806 Kbits/sec    0   72.2 KBytes       
[  5]   6.00-7.00   sec   252 KBytes  2.07 Mbits/sec    0    102 KBytes       
[  5]   7.00-8.00   sec   189 KBytes  1.55 Mbits/sec    0    142 KBytes       
[  5]   8.00-9.00   sec  0.00 Bytes  0.00 bits/sec    0    175 KBytes       
[  5]   9.00-10.00  sec   252 KBytes  2.06 Mbits/sec    0    220 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.29 MBytes  1.08 Mbits/sec    0             sender
[  5]   0.00-14.30  sec  1.02 MBytes   598 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-07-31 23:18:31
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 41312 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  8.10 MBytes  67.9 Mbits/sec    0    425 KBytes       
[  5]   1.00-2.00   sec  12.2 MBytes   102 Mbits/sec    0    965 KBytes       
[  5]   2.00-3.00   sec  11.0 MBytes  92.3 Mbits/sec    0   1.47 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.00 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  260   1.10 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.17 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.23 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.28 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.31 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.32 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   105 MBytes  88.1 Mbits/sec  260             sender
[  5]   0.00-10.17  sec   103 MBytes  85.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 00:18:42
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 49492 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.5 MBytes   105 Mbits/sec    0    781 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.1 Mbits/sec    0   1.29 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.82 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec   61   1.55 MBytes       
[  5]   4.00-5.00   sec  12.5 MBytes   105 Mbits/sec  129   1.14 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.21 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.26 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.29 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.31 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.32 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.3 Mbits/sec  190             sender
[  5]   0.00-10.17  sec   106 MBytes  87.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 01:18:53
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 33654 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.3 MBytes  94.9 Mbits/sec    0    601 KBytes       
[  5]   1.00-2.00   sec  12.6 MBytes   105 Mbits/sec    0   1.11 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.64 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.17 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  708   1.12 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.19 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.25 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.29 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.31 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.3 Mbits/sec  708             sender
[  5]   0.00-10.17  sec   106 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 02:19:04
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 40240 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.4 MBytes  95.6 Mbits/sec    0    598 KBytes       
[  5]   1.00-2.00   sec  12.5 MBytes   105 Mbits/sec    0   1.11 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.64 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.16 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  423   1.12 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.20 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.25 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.29 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.32 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.3 Mbits/sec  423             sender
[  5]   0.00-10.17  sec   106 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 03:19:14
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 50382 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.5 MBytes  96.6 Mbits/sec    0    612 KBytes       
[  5]   1.00-2.00   sec  11.6 MBytes  97.0 Mbits/sec    0   1.12 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.65 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.18 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec  182   1.12 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.19 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.24 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.28 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.30 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.31 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.7 Mbits/sec  182             sender
[  5]   0.00-10.17  sec   106 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 04:19:25
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 59346 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.2 MBytes  94.2 Mbits/sec    0    591 KBytes       
[  5]   1.00-2.00   sec  11.4 MBytes  95.5 Mbits/sec    0   1.10 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.63 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.16 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec  140   1.12 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.19 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.25 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.28 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.31 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.32 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.3 Mbits/sec  140             sender
[  5]   0.00-10.17  sec   106 MBytes  87.2 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 05:19:36
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 45506 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.4 MBytes   104 Mbits/sec    0    790 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.1 Mbits/sec    0   1.30 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.83 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec   90   1.57 MBytes       
[  5]   4.00-5.00   sec  12.5 MBytes   105 Mbits/sec  350   1.15 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.22 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.27 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.30 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.32 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.2 Mbits/sec  440             sender
[  5]   0.00-10.17  sec   106 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 06:19:47
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 60428 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.5 MBytes  96.4 Mbits/sec    0    664 KBytes       
[  5]   1.00-2.00   sec  12.3 MBytes   103 Mbits/sec    0   1.18 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.70 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.23 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  157   1.13 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.20 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.26 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.29 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.32 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.2 Mbits/sec  157             sender
[  5]   0.00-10.17  sec   106 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 07:19:58
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 46676 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.6 MBytes  97.4 Mbits/sec    0    756 KBytes       
[  5]   1.00-2.00   sec  12.2 MBytes   102 Mbits/sec    0   1.27 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.79 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec   73   1.57 MBytes       
[  5]   4.00-5.00   sec  12.5 MBytes   105 Mbits/sec    8   1.69 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.84 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.95 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.04 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.11 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    1   1.54 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.2 Mbits/sec   82             sender
[  5]   0.00-10.19  sec   106 MBytes  87.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 08:20:08
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 53822 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  10.0 MBytes  84.1 Mbits/sec    0    660 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.3 Mbits/sec    0   1.14 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.67 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.20 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  119   1.12 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.20 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.25 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.29 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.31 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   105 MBytes  88.3 Mbits/sec  119             sender
[  5]   0.00-10.17  sec   104 MBytes  85.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 09:20:19
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 43030 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.88 MBytes  15.8 Mbits/sec    0    139 KBytes       
[  5]   1.00-2.00   sec  2.34 MBytes  19.6 Mbits/sec    0    243 KBytes       
[  5]   2.00-3.00   sec  3.94 MBytes  33.0 Mbits/sec    0    423 KBytes       
[  5]   3.00-4.00   sec  4.92 MBytes  41.3 Mbits/sec    0    644 KBytes       
[  5]   4.00-5.00   sec  9.66 MBytes  81.0 Mbits/sec    0   1.03 MBytes       
[  5]   5.00-6.00   sec  8.73 MBytes  73.2 Mbits/sec    0   1.47 MBytes       
[  5]   6.00-7.00   sec  8.75 MBytes  73.4 Mbits/sec    0   1.94 MBytes       
[  5]   7.00-8.00   sec  7.50 MBytes  62.9 Mbits/sec   86   1.57 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.71 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.85 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  69.0 MBytes  57.9 Mbits/sec   86             sender
[  5]   0.00-10.24  sec  67.7 MBytes  55.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 10:20:30
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 42860 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   546 KBytes  4.47 Mbits/sec    0   51.2 KBytes       
[  5]   1.00-2.00   sec   496 KBytes  4.06 Mbits/sec    0   70.9 KBytes       
[  5]   2.00-3.00   sec   630 KBytes  5.16 Mbits/sec    0   98.4 KBytes       
[  5]   3.00-4.00   sec  1.23 MBytes  10.3 Mbits/sec    0    160 KBytes       
[  5]   4.00-5.00   sec  1.72 MBytes  14.5 Mbits/sec    0    227 KBytes       
[  5]   5.00-6.00   sec  3.81 MBytes  32.0 Mbits/sec    0    416 KBytes       
[  5]   6.00-7.00   sec  2.15 MBytes  18.1 Mbits/sec    0    513 KBytes       
[  5]   7.00-8.00   sec  6.71 MBytes  56.3 Mbits/sec    0    785 KBytes       
[  5]   8.00-9.00   sec  8.96 MBytes  75.2 Mbits/sec    0   1.17 MBytes       
[  5]   9.00-10.00  sec  8.75 MBytes  73.4 Mbits/sec    0   1.63 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  35.0 MBytes  29.3 Mbits/sec    0             sender
[  5]   0.00-10.21  sec  33.6 MBytes  27.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 11:20:41
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 38128 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   192 KBytes  1.57 Mbits/sec    0   35.4 KBytes       
[  5]   1.00-2.00   sec   584 KBytes  4.78 Mbits/sec    0   60.4 KBytes       
[  5]   2.00-3.00   sec  1.36 MBytes  11.4 Mbits/sec    0    123 KBytes       
[  5]   3.00-4.00   sec  3.08 MBytes  25.8 Mbits/sec    0    269 KBytes       
[  5]   4.00-5.00   sec  2.71 MBytes  22.7 Mbits/sec    0    386 KBytes       
[  5]   5.00-6.00   sec  2.03 MBytes  17.0 Mbits/sec    0    476 KBytes       
[  5]   6.00-7.00   sec  3.94 MBytes  33.0 Mbits/sec    0    644 KBytes       
[  5]   7.00-8.00   sec  8.61 MBytes  72.2 Mbits/sec    0   1.04 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.2 Mbits/sec    0   1.56 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   2.08 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  43.7 MBytes  36.7 Mbits/sec    0             sender
[  5]   0.00-10.23  sec  43.0 MBytes  35.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 12:20:58
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 35298 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    0   24.9 KBytes       
[  5]   1.00-2.00   sec   136 KBytes  1.12 Mbits/sec    0   34.1 KBytes       
[  5]   2.00-3.00   sec   101 KBytes   828 Kbits/sec    0   38.1 KBytes       
[  5]   3.00-4.00   sec  89.2 KBytes   731 Kbits/sec    0   42.0 KBytes       
[  5]   4.00-5.00   sec  82.7 KBytes   678 Kbits/sec    0   53.8 KBytes       
[  5]   5.00-6.00   sec   200 KBytes  1.63 Mbits/sec    0   76.1 KBytes       
[  5]   6.00-7.00   sec   126 KBytes  1.03 Mbits/sec    0    110 KBytes       
[  5]   7.00-8.00   sec   189 KBytes  1.55 Mbits/sec    0    152 KBytes       
[  5]   8.00-9.00   sec   189 KBytes  1.55 Mbits/sec    0    192 KBytes       
[  5]   9.00-10.00  sec   252 KBytes  2.06 Mbits/sec    0    226 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.38 MBytes  1.15 Mbits/sec    0             sender
[  5]   0.00-13.72  sec  1.02 MBytes   621 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 13:21:20
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 59028 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    0   24.9 KBytes       
[  5]   1.00-2.00   sec  68.2 KBytes   559 Kbits/sec    0   31.5 KBytes       
[  5]   2.00-3.00   sec   167 KBytes  1.37 Mbits/sec    0   38.1 KBytes       
[  5]   3.00-4.00   sec   178 KBytes  1.46 Mbits/sec    0   47.2 KBytes       
[  5]   4.00-5.00   sec   440 KBytes  3.60 Mbits/sec    0   63.0 KBytes       
[  5]   5.00-6.00   sec   630 KBytes  5.16 Mbits/sec    0   91.9 KBytes       
[  5]   6.00-7.00   sec   630 KBytes  5.16 Mbits/sec    0    125 KBytes       
[  5]   7.00-8.00   sec   945 KBytes  7.74 Mbits/sec    0    168 KBytes       
[  5]   8.00-9.00   sec   504 KBytes  4.13 Mbits/sec    0    228 KBytes       
[  5]   9.00-10.00  sec   315 KBytes  2.58 Mbits/sec    0    276 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  3.83 MBytes  3.21 Mbits/sec    0             sender
[  5]   0.00-13.76  sec  3.46 MBytes  2.11 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 14:21:42
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 43798 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   189 KBytes  1.55 Mbits/sec    0   32.8 KBytes       
[  5]   1.00-2.00   sec  0.00 Bytes  0.00 bits/sec    0   32.8 KBytes       
[  5]   2.00-3.00   sec  0.00 Bytes  0.00 bits/sec    0   34.1 KBytes       
[  5]   3.00-4.00   sec  97.1 KBytes   796 Kbits/sec    0   45.9 KBytes       
[  5]   4.00-5.00   sec  0.00 Bytes  0.00 bits/sec    0   59.1 KBytes       
[  5]   5.00-6.00   sec   135 KBytes  1.11 Mbits/sec    0   74.8 KBytes       
[  5]   6.00-7.00   sec   126 KBytes  1.03 Mbits/sec    0    106 KBytes       
[  5]   7.00-8.00   sec  0.00 Bytes  0.00 bits/sec    0    125 KBytes       
[  5]   8.00-9.00   sec   189 KBytes  1.55 Mbits/sec    0    171 KBytes       
[  5]   9.00-10.00  sec   252 KBytes  2.06 Mbits/sec    0    206 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   988 KBytes   810 Kbits/sec    0             sender
[  5]   0.00-13.34  sec   642 KBytes   394 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 15:21:56
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 37788 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   185 KBytes  1.52 Mbits/sec    0   35.4 KBytes       
[  5]   1.00-2.00   sec   192 KBytes  1.57 Mbits/sec    0   40.7 KBytes       
[  5]   2.00-3.00   sec   785 KBytes  6.43 Mbits/sec    0   78.8 KBytes       
[  5]   3.00-4.00   sec  4.37 MBytes  36.6 Mbits/sec    0    274 KBytes       
[  5]   4.00-5.00   sec  4.43 MBytes  37.2 Mbits/sec    0    483 KBytes       
[  5]   5.00-6.00   sec  3.88 MBytes  32.5 Mbits/sec    0    642 KBytes       
[  5]   6.00-7.00   sec  2.46 MBytes  20.6 Mbits/sec    0    773 KBytes       
[  5]   7.00-8.00   sec  3.88 MBytes  32.5 Mbits/sec    0    949 KBytes       
[  5]   8.00-9.00   sec  2.28 MBytes  19.1 Mbits/sec    0   1.03 MBytes       
[  5]   9.00-10.00  sec  1.23 MBytes  10.3 Mbits/sec    0   1.08 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  23.7 MBytes  19.8 Mbits/sec    0             sender
[  5]   0.00-12.08  sec  22.2 MBytes  15.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 16:22:07
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 53352 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   680 KBytes  5.57 Mbits/sec    0   56.4 KBytes       
[  5]   1.00-2.00   sec  2.12 MBytes  17.8 Mbits/sec    0    152 KBytes       
[  5]   2.00-3.00   sec  1.42 MBytes  11.9 Mbits/sec    0    215 KBytes       
[  5]   3.00-4.00   sec  1.97 MBytes  16.5 Mbits/sec    0    310 KBytes       
[  5]   4.00-5.00   sec  1.66 MBytes  13.9 Mbits/sec    0    391 KBytes       
[  5]   5.00-6.00   sec   504 KBytes  4.13 Mbits/sec    0    400 KBytes       
[  5]   6.00-7.00   sec  0.00 Bytes  0.00 bits/sec    0    415 KBytes       
[  5]   7.00-8.00   sec  1008 KBytes  8.26 Mbits/sec    0    444 KBytes       
[  5]   8.00-9.00   sec  1.72 MBytes  14.4 Mbits/sec    0    529 KBytes       
[  5]   9.00-10.00  sec  1.29 MBytes  10.8 Mbits/sec    0    592 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  12.3 MBytes  10.3 Mbits/sec    0             sender
[  5]   0.00-10.44  sec  11.5 MBytes  9.28 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 17:22:26
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 37202 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   114 KBytes   935 Kbits/sec    0   31.5 KBytes       
[  5]   1.00-2.00   sec  98.4 KBytes   806 Kbits/sec    0   35.4 KBytes       
[  5]   2.00-3.00   sec  91.9 KBytes   753 Kbits/sec    0   38.1 KBytes       
[  5]   3.00-4.00   sec  86.6 KBytes   710 Kbits/sec    0   45.9 KBytes       
[  5]   4.00-5.00   sec   211 KBytes  1.73 Mbits/sec    0   61.7 KBytes       
[  5]   5.00-6.00   sec   126 KBytes  1.03 Mbits/sec    0   93.2 KBytes       
[  5]   6.00-7.00   sec   126 KBytes  1.03 Mbits/sec    0    126 KBytes       
[  5]   7.00-8.00   sec   189 KBytes  1.55 Mbits/sec    0    165 KBytes       
[  5]   8.00-9.00   sec   252 KBytes  2.06 Mbits/sec    0    190 KBytes       
[  5]   9.00-10.00  sec  0.00 Bytes  0.00 bits/sec    0    220 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.27 MBytes  1.06 Mbits/sec    0             sender
[  5]   0.00-14.20  sec  1011 KBytes   583 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 18:22:40
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 33544 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   280 KBytes  2.29 Mbits/sec    0   36.8 KBytes       
[  5]   1.00-2.00   sec   339 KBytes  2.77 Mbits/sec    0   55.1 KBytes       
[  5]   2.00-3.00   sec   673 KBytes  5.52 Mbits/sec    0   85.3 KBytes       
[  5]   3.00-4.00   sec   822 KBytes  6.73 Mbits/sec    0    117 KBytes       
[  5]   4.00-5.00   sec   819 KBytes  6.71 Mbits/sec    0    155 KBytes       
[  5]   5.00-6.00   sec   945 KBytes  7.74 Mbits/sec    0    194 KBytes       
[  5]   6.00-7.00   sec   819 KBytes  6.71 Mbits/sec    0    232 KBytes       
[  5]   7.00-8.00   sec   315 KBytes  2.58 Mbits/sec    0    244 KBytes       
[  5]   8.00-9.00   sec   378 KBytes  3.10 Mbits/sec    0    299 KBytes       
[  5]   9.00-10.00  sec   441 KBytes  3.61 Mbits/sec    0    383 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  5.69 MBytes  4.78 Mbits/sec    0             sender
[  5]   0.00-11.64  sec  5.00 MBytes  3.60 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 20:23:18
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 55742 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    0   23.6 KBytes       
[  5]   1.00-2.00   sec  69.6 KBytes   570 Kbits/sec    0   31.5 KBytes       
[  5]   2.00-3.00   sec  44.6 KBytes   366 Kbits/sec    0   32.8 KBytes       
[  5]   3.00-4.00   sec  93.2 KBytes   763 Kbits/sec    0   38.1 KBytes       
[  5]   4.00-5.00   sec  0.00 Bytes  0.00 bits/sec    0   49.9 KBytes       
[  5]   5.00-6.00   sec   207 KBytes  1.70 Mbits/sec    0   74.8 KBytes       
[  5]   6.00-7.00   sec  0.00 Bytes  0.00 bits/sec    0    104 KBytes       
[  5]   7.00-8.00   sec   218 KBytes  1.79 Mbits/sec    0    139 KBytes       
[  5]   8.00-9.00   sec   189 KBytes  1.55 Mbits/sec    0    182 KBytes       
[  5]   9.00-10.00  sec   252 KBytes  2.07 Mbits/sec    0    214 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.09 MBytes   916 Kbits/sec    0             sender
[  5]   0.00-13.30  sec   686 KBytes   423 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 21:23:30
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 33340 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   110 KBytes   903 Kbits/sec    0   31.5 KBytes       
[  5]   1.00-2.00   sec   167 KBytes  1.37 Mbits/sec    0   35.4 KBytes       
[  5]   2.00-3.00   sec  0.00 Bytes  0.00 bits/sec    0   39.4 KBytes       
[  5]   3.00-4.00   sec   104 KBytes   850 Kbits/sec    0   45.9 KBytes       
[  5]   4.00-5.00   sec   329 KBytes  2.70 Mbits/sec    0   66.9 KBytes       
[  5]   5.00-6.00   sec   655 KBytes  5.37 Mbits/sec    0    105 KBytes       
[  5]   6.00-7.00   sec  1.11 MBytes  9.29 Mbits/sec    0    160 KBytes       
[  5]   7.00-8.00   sec  1.72 MBytes  14.5 Mbits/sec    0    232 KBytes       
[  5]   8.00-9.00   sec  2.46 MBytes  20.6 Mbits/sec    0    349 KBytes       
[  5]   9.00-10.00  sec  2.95 MBytes  24.8 Mbits/sec    0    488 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  9.58 MBytes  8.03 Mbits/sec    0             sender
[  5]   0.00-10.22  sec  8.94 MBytes  7.33 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 22:23:41
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 43478 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  9.81 MBytes  82.3 Mbits/sec    0    539 KBytes       
[  5]   1.00-2.00   sec  12.6 MBytes   105 Mbits/sec    0   1.05 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.58 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.11 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  131   1.46 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec  136   1.27 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.38 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.42 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.44 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  90.1 Mbits/sec  267             sender
[  5]   0.00-10.18  sec   105 MBytes  86.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-01 23:23:52
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 35782 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.7 MBytes  97.9 Mbits/sec    0    606 KBytes       
[  5]   1.00-2.00   sec  11.6 MBytes  97.5 Mbits/sec    0   1.12 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.65 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.18 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec   97   1.73 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.90 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.04 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.16 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.25 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   2.32 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.8 Mbits/sec   97             sender
[  5]   0.00-10.26  sec   107 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 00:24:02
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 39416 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  10.0 MBytes  84.0 Mbits/sec    0    488 KBytes       
[  5]   1.00-2.00   sec  12.6 MBytes   105 Mbits/sec    0   1.00 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.2 Mbits/sec    0   1.53 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.06 MBytes       
[  5]   4.00-5.00   sec  8.75 MBytes  73.4 Mbits/sec   96   1.72 MBytes       
[  5]   5.00-6.00   sec  12.5 MBytes   105 Mbits/sec   27   1.26 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.39 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.42 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.44 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.2 Mbits/sec  123             sender
[  5]   0.00-10.19  sec   105 MBytes  86.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 01:24:13
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 46098 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.0 MBytes   101 Mbits/sec    0    764 KBytes       
[  5]   1.00-2.00   sec  11.2 MBytes  93.9 Mbits/sec    0   1.27 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.80 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.32 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  117   1.23 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.30 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.36 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.40 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.43 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.44 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.8 Mbits/sec  117             sender
[  5]   0.00-10.18  sec   106 MBytes  87.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 02:24:24
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 49068 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.0 MBytes   101 Mbits/sec    0    776 KBytes       
[  5]   1.00-2.00   sec  12.4 MBytes   104 Mbits/sec    0   1.28 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.81 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.34 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec  148   1.22 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.30 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.36 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.40 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.43 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.45 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.7 Mbits/sec  148             sender
[  5]   0.00-10.18  sec   106 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 03:24:35
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 54972 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.1 MBytes   102 Mbits/sec    0    669 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.3 Mbits/sec    0   1.18 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.71 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.23 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  188   1.20 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.28 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.35 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.39 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.43 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.45 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   109 MBytes  91.1 Mbits/sec  188             sender
[  5]   0.00-10.19  sec   106 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 04:24:46
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 44250 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  5.92 MBytes  49.6 Mbits/sec    0    287 KBytes       
[  5]   1.00-2.00   sec  11.3 MBytes  95.0 Mbits/sec    0    791 KBytes       
[  5]   2.00-3.00   sec  11.5 MBytes  96.1 Mbits/sec    0   1.30 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.83 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.35 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec   96   1.79 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.96 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.09 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.20 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   2.28 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   102 MBytes  85.9 Mbits/sec   96             sender
[  5]   0.00-10.26  sec   102 MBytes  83.0 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 05:24:56
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 46916 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.1 MBytes  93.4 Mbits/sec    0    602 KBytes       
[  5]   1.00-2.00   sec  12.7 MBytes   106 Mbits/sec    0   1.12 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.64 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.17 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec   48   1.17 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.25 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.31 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.36 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.39 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.41 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.2 Mbits/sec   48             sender
[  5]   0.00-10.18  sec   106 MBytes  87.2 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 06:25:07
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 55968 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.8 MBytes  99.1 Mbits/sec    0    616 KBytes       
[  5]   1.00-2.00   sec  11.8 MBytes  99.3 Mbits/sec    0   1.13 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.64 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.18 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec   92   1.74 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.90 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.05 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.16 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.25 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   2.32 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  90.1 Mbits/sec   92             sender
[  5]   0.00-10.27  sec   105 MBytes  86.0 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 07:25:18
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 49386 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.3 MBytes   103 Mbits/sec    0    671 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.8 Mbits/sec    0   1.18 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.71 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.24 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec   91   1.75 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.91 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.05 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.17 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.26 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    3   2.06 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.2 Mbits/sec   94             sender
[  5]   0.00-10.24  sec   107 MBytes  87.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 08:25:29
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 44456 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  10.1 MBytes  85.0 Mbits/sec    0    474 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.5 Mbits/sec    0   1009 KBytes       
[  5]   2.00-3.00   sec  8.65 MBytes  72.6 Mbits/sec    0   1.38 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.86 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.39 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec  307   1.23 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.30 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.36 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.41 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.43 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   103 MBytes  86.2 Mbits/sec  307             sender
[  5]   0.00-10.18  sec   101 MBytes  83.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 09:25:40
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 37086 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.8 MBytes  98.8 Mbits/sec    0    698 KBytes       
[  5]   1.00-2.00   sec  11.8 MBytes  98.9 Mbits/sec    0   1.21 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.74 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.27 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec   98   1.21 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.29 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.35 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.40 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.43 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.45 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   109 MBytes  91.1 Mbits/sec   98             sender
[  5]   0.00-10.18  sec   106 MBytes  87.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 10:25:51
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 45166 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  10.6 MBytes  88.9 Mbits/sec    0   1.59 MBytes       
[  5]   1.00-2.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.13 MBytes       
[  5]   2.00-3.00   sec  8.75 MBytes  73.4 Mbits/sec  644    921 KBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    7   1.25 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.32 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.36 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.40 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.42 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.43 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.43 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   104 MBytes  87.5 Mbits/sec  651             sender
[  5]   0.00-10.18  sec   102 MBytes  84.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 11:26:01
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 37594 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  3.85 MBytes  32.3 Mbits/sec    0    218 KBytes       
[  5]   1.00-2.00   sec  3.88 MBytes  32.5 Mbits/sec    0    396 KBytes       
[  5]   2.00-3.00   sec  4.68 MBytes  39.2 Mbits/sec    0    614 KBytes       
[  5]   3.00-4.00   sec  8.31 MBytes  69.7 Mbits/sec    0    969 KBytes       
[  5]   4.00-5.00   sec  7.40 MBytes  62.1 Mbits/sec    0   1.28 MBytes       
[  5]   5.00-6.00   sec  6.25 MBytes  52.4 Mbits/sec    0   1.60 MBytes       
[  5]   6.00-7.00   sec  5.00 MBytes  41.9 Mbits/sec    0   1.87 MBytes       
[  5]   7.00-8.00   sec  6.25 MBytes  52.4 Mbits/sec    0   2.18 MBytes       
[  5]   8.00-9.00   sec  5.00 MBytes  41.9 Mbits/sec   30   2.18 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec  144   1.24 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  61.9 MBytes  51.9 Mbits/sec  174             sender
[  5]   0.00-10.16  sec  60.1 MBytes  49.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 12:26:12
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 33444 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  6.12 MBytes  51.3 Mbits/sec    0    306 KBytes       
[  5]   1.00-2.00   sec  11.7 MBytes  98.1 Mbits/sec    0    837 KBytes       
[  5]   2.00-3.00   sec  11.6 MBytes  97.2 Mbits/sec    0   1.35 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.87 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec   81   1.55 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.70 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.84 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.95 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.04 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   2.10 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   103 MBytes  86.5 Mbits/sec   81             sender
[  5]   0.00-10.25  sec   102 MBytes  83.2 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 13:26:23
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 41834 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.46 MBytes  12.3 Mbits/sec    0    142 KBytes       
[  5]   1.00-2.00   sec  1.54 MBytes  12.9 Mbits/sec    1    211 KBytes       
[  5]   2.00-3.00   sec  7.44 MBytes  62.5 Mbits/sec    0    537 KBytes       
[  5]   3.00-4.00   sec  7.57 MBytes  63.5 Mbits/sec    0    904 KBytes       
[  5]   4.00-5.00   sec  3.45 MBytes  28.9 Mbits/sec    0   1.00 MBytes       
[  5]   5.00-6.00   sec  3.73 MBytes  31.3 Mbits/sec    0   1.19 MBytes       
[  5]   6.00-7.00   sec  8.75 MBytes  73.4 Mbits/sec    0   1.65 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.18 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec  114   1.65 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.81 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  65.2 MBytes  54.7 Mbits/sec  115             sender
[  5]   0.00-10.25  sec  63.9 MBytes  52.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 14:26:34
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 36622 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  2.12 MBytes  17.7 Mbits/sec    0    119 KBytes       
[  5]   1.00-2.00   sec  5.91 MBytes  49.5 Mbits/sec    0    381 KBytes       
[  5]   2.00-3.00   sec  9.47 MBytes  79.5 Mbits/sec    0    823 KBytes       
[  5]   3.00-4.00   sec  7.83 MBytes  65.7 Mbits/sec    0   1.17 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.62 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.13 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec  400   1.12 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.19 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.25 MBytes       
[  5]   9.00-10.00  sec  8.75 MBytes  73.4 Mbits/sec    0   1.29 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  85.3 MBytes  71.6 Mbits/sec  400             sender
[  5]   0.00-10.17  sec  84.1 MBytes  69.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 15:26:45
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 34950 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.52 MBytes  12.8 Mbits/sec    0   97.1 KBytes       
[  5]   1.00-2.00   sec  4.43 MBytes  37.2 Mbits/sec    0    297 KBytes       
[  5]   2.00-3.00   sec  8.06 MBytes  67.6 Mbits/sec    0    664 KBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.1 Mbits/sec    0   1.12 MBytes       
[  5]   4.00-5.00   sec  8.75 MBytes  73.4 Mbits/sec    0   1.59 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.12 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec  406   1.11 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.18 MBytes       
[  5]   8.00-9.00   sec  5.00 MBytes  41.9 Mbits/sec    0   1.24 MBytes       
[  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0   1.28 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  76.5 MBytes  64.2 Mbits/sec  406             sender
[  5]   0.00-10.28  sec  74.2 MBytes  60.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 16:26:59
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 55148 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.07 MBytes  8.95 Mbits/sec    0   76.1 KBytes       
[  5]   1.00-2.00   sec   948 KBytes  7.76 Mbits/sec    0    118 KBytes       
[  5]   2.00-3.00   sec   378 KBytes  3.10 Mbits/sec    0    131 KBytes       
[  5]   3.00-4.00   sec   189 KBytes  1.55 Mbits/sec    0    140 KBytes       
[  5]   4.00-5.00   sec  0.00 Bytes  0.00 bits/sec    0    144 KBytes       
[  5]   5.00-6.00   sec   189 KBytes  1.55 Mbits/sec    0    155 KBytes       
[  5]   6.00-7.00   sec   882 KBytes  7.23 Mbits/sec    0    193 KBytes       
[  5]   7.00-8.00   sec  1.05 MBytes  8.77 Mbits/sec    0    255 KBytes       
[  5]   8.00-9.00   sec   693 KBytes  5.68 Mbits/sec    0    320 KBytes       
[  5]   9.00-10.00  sec   441 KBytes  3.61 Mbits/sec    0    388 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  5.75 MBytes  4.82 Mbits/sec    0             sender
[  5]   0.00-11.97  sec  5.02 MBytes  3.52 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 17:27:12
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 60346 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   160 KBytes  1.31 Mbits/sec    0   32.8 KBytes       
[  5]   1.00-2.00   sec  98.4 KBytes   806 Kbits/sec    0   38.1 KBytes       
[  5]   2.00-3.00   sec   190 KBytes  1.56 Mbits/sec    0   45.9 KBytes       
[  5]   3.00-4.00   sec   181 KBytes  1.48 Mbits/sec    0   53.8 KBytes       
[  5]   4.00-5.00   sec   245 KBytes  2.01 Mbits/sec    0   70.9 KBytes       
[  5]   5.00-6.00   sec   378 KBytes  3.10 Mbits/sec    0    110 KBytes       
[  5]   6.00-7.00   sec   567 KBytes  4.64 Mbits/sec    0    160 KBytes       
[  5]   7.00-8.00   sec   504 KBytes  4.13 Mbits/sec    0    223 KBytes       
[  5]   8.00-9.00   sec   693 KBytes  5.68 Mbits/sec    0    304 KBytes       
[  5]   9.00-10.00  sec   441 KBytes  3.61 Mbits/sec    0    406 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  3.38 MBytes  2.83 Mbits/sec    0             sender
[  5]   0.00-10.83  sec  2.95 MBytes  2.29 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 18:27:41
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 44292 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   110 KBytes   903 Kbits/sec    0   38.1 KBytes       
[  5]   1.00-2.00   sec   262 KBytes  2.15 Mbits/sec    0   65.6 KBytes       
[  5]   2.00-3.00   sec   139 KBytes  1.14 Mbits/sec    0   69.6 KBytes       
[  5]   3.00-4.00   sec   158 KBytes  1.29 Mbits/sec    0   76.1 KBytes       
[  5]   4.00-5.00   sec   259 KBytes  2.12 Mbits/sec    0   85.3 KBytes       
[  5]   5.00-6.00   sec   441 KBytes  3.61 Mbits/sec    0    116 KBytes       
[  5]   6.00-7.00   sec   441 KBytes  3.61 Mbits/sec    0    156 KBytes       
[  5]   7.00-8.00   sec   504 KBytes  4.13 Mbits/sec    0    206 KBytes       
[  5]   8.00-9.00   sec   315 KBytes  2.58 Mbits/sec    0    269 KBytes       
[  5]   9.00-10.00  sec   378 KBytes  3.10 Mbits/sec    0    303 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  2.94 MBytes  2.46 Mbits/sec    0             sender
[  5]   0.00-13.45  sec  2.33 MBytes  1.45 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 19:28:05
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 49708 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    0   22.3 KBytes       
[  5]   1.00-2.00   sec  72.2 KBytes   592 Kbits/sec    0   31.5 KBytes       
[  5]   2.00-3.00   sec  0.00 Bytes  0.00 bits/sec    0   31.5 KBytes       
[  5]   3.00-4.00   sec  0.00 Bytes  0.00 bits/sec    0   31.5 KBytes       
[  5]   4.00-5.00   sec  72.2 KBytes   592 Kbits/sec    0   44.6 KBytes       
[  5]   5.00-6.00   sec  0.00 Bytes  0.00 bits/sec    0   52.5 KBytes       
[  5]   6.00-7.00   sec   110 KBytes   904 Kbits/sec    0   59.1 KBytes       
[  5]   7.00-8.00   sec  0.00 Bytes  0.00 bits/sec    0   73.5 KBytes       
[  5]   8.00-9.00   sec  0.00 Bytes  0.00 bits/sec    0   78.8 KBytes       
[  5]   9.00-10.00  sec  0.00 Bytes  0.00 bits/sec    0   81.4 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   299 KBytes   245 Kbits/sec    0             sender
[  5]   0.00-14.23  sec   217 KBytes   125 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 21:28:42
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 57996 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    0   19.7 KBytes       
[  5]   1.00-2.00   sec  65.6 KBytes   538 Kbits/sec    0   31.5 KBytes       
[  5]   2.00-3.00   sec  49.9 KBytes   409 Kbits/sec    0   34.1 KBytes       
[  5]   3.00-4.00   sec  97.1 KBytes   796 Kbits/sec    0   39.4 KBytes       
[  5]   4.00-5.00   sec  82.7 KBytes   678 Kbits/sec    0   56.4 KBytes       
[  5]   5.00-6.00   sec  0.00 Bytes  0.00 bits/sec    0   63.0 KBytes       
[  5]   6.00-7.00   sec   126 KBytes  1.03 Mbits/sec    0   76.1 KBytes       
[  5]   7.00-8.00   sec  0.00 Bytes  0.00 bits/sec    0   95.8 KBytes       
[  5]   8.00-9.00   sec   126 KBytes  1.03 Mbits/sec    0    117 KBytes       
[  5]   9.00-10.00  sec   189 KBytes  1.55 Mbits/sec    0    139 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   781 KBytes   640 Kbits/sec    0             sender
[  5]   0.00-12.17  sec   466 KBytes   314 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 22:28:53
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 39818 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  2.75 MBytes  23.1 Mbits/sec    0    169 KBytes       
[  5]   1.00-2.00   sec  9.35 MBytes  78.4 Mbits/sec    0    583 KBytes       
[  5]   2.00-3.00   sec  11.4 MBytes  95.5 Mbits/sec    0   1.10 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.63 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.14 MBytes       
[  5]   5.00-6.00   sec  8.75 MBytes  73.4 Mbits/sec   69   1.80 MBytes       
[  5]   6.00-7.00   sec  12.5 MBytes   105 Mbits/sec  359   1.31 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.39 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.44 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.49 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  97.2 MBytes  81.6 Mbits/sec  428             sender
[  5]   0.00-10.19  sec  95.7 MBytes  78.8 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-02 23:29:04
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 38286 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.5 MBytes   105 Mbits/sec    0    760 KBytes       
[  5]   1.00-2.00   sec  11.2 MBytes  93.9 Mbits/sec    0   1.27 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.80 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.32 MBytes       
[  5]   4.00-5.00   sec  8.75 MBytes  73.4 Mbits/sec  168   1.37 MBytes       
[  5]   5.00-6.00   sec  12.5 MBytes   105 Mbits/sec    0   1.34 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.41 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.46 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.50 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.52 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  90.1 Mbits/sec  168             sender
[  5]   0.00-10.19  sec   106 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 00:29:15
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 52074 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.27 MBytes  10.7 Mbits/sec    0   82.7 KBytes       
[  5]   1.00-2.00   sec  2.15 MBytes  18.1 Mbits/sec    0    186 KBytes       
[  5]   2.00-3.00   sec  4.74 MBytes  39.7 Mbits/sec    0    396 KBytes       
[  5]   3.00-4.00   sec  6.15 MBytes  51.6 Mbits/sec    0    673 KBytes       
[  5]   4.00-5.00   sec  10.2 MBytes  85.2 Mbits/sec    0   1.10 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec   41   1.02 MBytes       
[  5]   6.00-7.00   sec  8.75 MBytes  73.4 Mbits/sec    0   1.14 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.24 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.32 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.37 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  74.5 MBytes  62.5 Mbits/sec   41             sender
[  5]   0.00-10.16  sec  72.8 MBytes  60.1 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 01:29:26
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 33922 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.6 MBytes  97.7 Mbits/sec    0    669 KBytes       
[  5]   1.00-2.00   sec  12.5 MBytes   105 Mbits/sec    0   1.18 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.71 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec   89   1.48 MBytes       
[  5]   4.00-5.00   sec  12.5 MBytes   105 Mbits/sec  659   1.09 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.15 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.20 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.23 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.25 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.26 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.5 Mbits/sec  748             sender
[  5]   0.00-10.17  sec   106 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 02:29:37
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 36986 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.9 MBytes  99.5 Mbits/sec    0    748 KBytes       
[  5]   1.00-2.00   sec  11.0 MBytes  92.4 Mbits/sec    0   1.26 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.79 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec   81   1.48 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec   40   1.10 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.16 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.20 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.23 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.25 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.25 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.5 Mbits/sec  121             sender
[  5]   0.00-10.17  sec   106 MBytes  87.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 03:29:47
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 45130 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.6 MBytes  97.3 Mbits/sec    0    663 KBytes       
[  5]   1.00-2.00   sec  12.3 MBytes   104 Mbits/sec    0   1.17 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.70 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec   41   1.79 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec   56   1.11 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.18 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.23 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.26 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.28 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.30 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.3 Mbits/sec   97             sender
[  5]   0.00-10.17  sec   106 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 04:29:58
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 33092 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.1 MBytes   102 Mbits/sec    0    778 KBytes       
[  5]   1.00-2.00   sec  11.2 MBytes  93.9 Mbits/sec    0   1.29 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.81 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec   79   1.55 MBytes       
[  5]   4.00-5.00   sec  12.5 MBytes   105 Mbits/sec    0   1.69 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.83 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.94 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.03 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.09 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec  338   1.04 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.8 Mbits/sec  417             sender
[  5]   0.00-10.15  sec   106 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 05:30:09
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 49492 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.9 MBytes  99.8 Mbits/sec    0    639 KBytes       
[  5]   1.00-2.00   sec  12.1 MBytes   101 Mbits/sec    0   1.15 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.68 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.20 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  259   1.12 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.19 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.24 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.28 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.30 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.32 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.4 Mbits/sec  259             sender
[  5]   0.00-10.18  sec   106 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 06:30:19
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 48436 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.7 MBytes  98.5 Mbits/sec    0    776 KBytes       
[  5]   1.00-2.00   sec  11.1 MBytes  93.4 Mbits/sec    0   1.28 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.81 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec   85   1.55 MBytes       
[  5]   4.00-5.00   sec  12.5 MBytes   105 Mbits/sec    0   1.69 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.83 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.94 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.03 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.10 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    4   1.52 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.5 Mbits/sec   89             sender
[  5]   0.00-10.19  sec   106 MBytes  87.2 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 07:30:30
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 55544 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.7 MBytes  98.1 Mbits/sec    0    690 KBytes       
[  5]   1.00-2.00   sec  11.7 MBytes  97.9 Mbits/sec    0   1.20 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.72 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec   34   1.89 MBytes       
[  5]   4.00-5.00   sec  12.5 MBytes   105 Mbits/sec   91   1.13 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.19 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.24 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.28 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.30 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.31 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.9 Mbits/sec  125             sender
[  5]   0.00-10.17  sec   106 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 08:30:41
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 36890 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.9 MBytes  99.4 Mbits/sec    0    617 KBytes       
[  5]   1.00-2.00   sec  11.8 MBytes  99.3 Mbits/sec    0   1.13 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.66 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.18 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec   85   1.64 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.79 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.91 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.00 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.08 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec   33   1.49 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   109 MBytes  91.2 Mbits/sec  118             sender
[  5]   0.00-10.19  sec   106 MBytes  87.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 09:30:52
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 45756 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.6 MBytes  97.3 Mbits/sec    0    616 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.5 Mbits/sec    0   1.13 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.65 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.18 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec   95   1.11 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.19 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.24 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.28 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.30 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.32 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.7 Mbits/sec   95             sender
[  5]   0.00-10.17  sec   106 MBytes  87.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 10:31:03
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 51370 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  8.92 MBytes  74.8 Mbits/sec    0    436 KBytes       
[  5]   1.00-2.00   sec  12.4 MBytes   104 Mbits/sec    0    980 KBytes       
[  5]   2.00-3.00   sec  11.1 MBytes  93.5 Mbits/sec    0   1.49 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.01 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec  377   1.09 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.17 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.23 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.27 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.29 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.31 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   106 MBytes  89.1 Mbits/sec  377             sender
[  5]   0.00-10.18  sec   104 MBytes  86.0 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 11:31:13
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 43822 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  10.7 MBytes  89.5 Mbits/sec    0    616 KBytes       
[  5]   1.00-2.00   sec  11.6 MBytes  97.0 Mbits/sec    0   1.13 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.65 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.19 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec   83   1.64 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.79 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.91 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.00 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.08 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec   24   1.49 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  90.0 Mbits/sec  107             sender
[  5]   0.00-10.19  sec   106 MBytes  87.0 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 12:31:24
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 51890 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  9.15 MBytes  76.8 Mbits/sec    0    647 KBytes       
[  5]   1.00-2.00   sec  9.84 MBytes  82.6 Mbits/sec    0   1.08 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.59 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.12 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec   79   1.63 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.78 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.91 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.01 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.09 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   2.14 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   104 MBytes  87.2 Mbits/sec   79             sender
[  5]   0.00-10.25  sec   102 MBytes  83.8 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 13:31:35
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 45096 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  10.1 MBytes  85.0 Mbits/sec    0    679 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.8 Mbits/sec    0   1.19 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.71 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.25 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  240   1.15 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.22 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.27 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.31 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.34 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.35 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   105 MBytes  88.4 Mbits/sec  240             sender
[  5]   0.00-10.18  sec   104 MBytes  85.8 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 14:31:46
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 45072 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.3 MBytes  94.9 Mbits/sec    0    589 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.5 Mbits/sec    0   1.11 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.64 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.16 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec  527   1.14 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.21 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.27 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.31 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.35 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.4 Mbits/sec  527             sender
[  5]   0.00-10.17  sec   106 MBytes  87.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 15:31:57
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 60770 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.8 MBytes  99.1 Mbits/sec    0    690 KBytes       
[  5]   1.00-2.00   sec  11.6 MBytes  97.4 Mbits/sec    0   1.20 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.73 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.26 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec  347   1.15 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.22 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.27 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.31 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.35 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  91.0 Mbits/sec  347             sender
[  5]   0.00-10.18  sec   106 MBytes  87.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 16:32:07
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 55020 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.8 MBytes  99.0 Mbits/sec    0    606 KBytes       
[  5]   1.00-2.00   sec  11.6 MBytes  97.5 Mbits/sec    0   1.12 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.64 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.17 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec   84   1.65 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.81 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.94 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.04 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.11 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec   75   1.25 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  89.9 Mbits/sec  159             sender
[  5]   0.00-10.16  sec   106 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 17:32:18
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 38372 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.6 MBytes  96.9 Mbits/sec    0    604 KBytes       
[  5]   1.00-2.00   sec  11.4 MBytes  96.0 Mbits/sec    0   1.12 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.65 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.17 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec  151   1.13 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.21 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.26 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.30 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.34 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.6 Mbits/sec  151             sender
[  5]   0.00-10.17  sec   106 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 18:32:29
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 45534 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.0 MBytes   100 Mbits/sec    0    668 KBytes       
[  5]   1.00-2.00   sec  11.3 MBytes  95.1 Mbits/sec    0   1.18 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.71 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.24 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec  444   1.14 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.22 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.27 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.31 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.33 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.35 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.9 Mbits/sec  444             sender
[  5]   0.00-10.17  sec   106 MBytes  87.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 19:32:40
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 33788 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  10.8 MBytes  90.6 Mbits/sec    0   1.01 MBytes       
[  5]   1.00-2.00   sec  11.2 MBytes  94.2 Mbits/sec    0   1.54 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.06 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec  155   1.12 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.19 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.25 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.30 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.34 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.35 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   106 MBytes  88.7 Mbits/sec  155             sender
[  5]   0.00-10.20  sec   104 MBytes  85.9 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 20:32:52
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 55974 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   731 KBytes  5.99 Mbits/sec    0   86.6 KBytes       
[  5]   1.00-2.00   sec   882 KBytes  7.23 Mbits/sec    0    126 KBytes       
[  5]   2.00-3.00   sec  1.72 MBytes  14.5 Mbits/sec    0    207 KBytes       
[  5]   3.00-4.00   sec  3.69 MBytes  31.0 Mbits/sec    0    365 KBytes       
[  5]   4.00-5.00   sec  3.63 MBytes  30.4 Mbits/sec    0    546 KBytes       
[  5]   5.00-6.00   sec  7.01 MBytes  58.8 Mbits/sec    0    835 KBytes       
[  5]   6.00-7.00   sec  9.29 MBytes  77.9 Mbits/sec    0   1.23 MBytes       
[  5]   7.00-8.00   sec  8.75 MBytes  73.4 Mbits/sec    0   1.71 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.19 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   2.69 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  55.7 MBytes  46.7 Mbits/sec    0             sender
[  5]   0.00-10.31  sec  55.4 MBytes  45.0 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 21:33:03
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 58114 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.98 MBytes  16.6 Mbits/sec    0    138 KBytes       
[  5]   1.00-2.00   sec  5.41 MBytes  45.4 Mbits/sec    0    377 KBytes       
[  5]   2.00-3.00   sec  9.29 MBytes  77.9 Mbits/sec    0    793 KBytes       
[  5]   3.00-4.00   sec  8.96 MBytes  75.2 Mbits/sec    0   1.21 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.73 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.25 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.79 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  89.4 MBytes  75.0 Mbits/sec    0             sender
[  5]   0.00-10.37  sec  89.4 MBytes  72.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 22:33:14
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 33304 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.0 MBytes   100 Mbits/sec    0    795 KBytes       
[  5]   1.00-2.00   sec  11.3 MBytes  94.9 Mbits/sec    0   1.30 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.83 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.36 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.89 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.13 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.13 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.13 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.13 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.13 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.8 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   108 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-03 23:33:25
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 54462 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.0 MBytes  92.2 Mbits/sec    0    558 KBytes       
[  5]   1.00-2.00   sec  11.6 MBytes  97.5 Mbits/sec    0   1.07 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.2 Mbits/sec    0   1.60 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.13 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.65 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.13 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec  824   1.55 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.64 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.72 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.78 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.3 Mbits/sec  824             sender
[  5]   0.00-10.22  sec   106 MBytes  87.2 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 00:33:36
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 36858 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.3 MBytes   103 Mbits/sec    0    777 KBytes       
[  5]   1.00-2.00   sec  11.2 MBytes  93.9 Mbits/sec    0   1.28 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.81 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.34 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.86 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  91.0 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   108 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 01:33:46
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 55578 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.6 MBytes  96.9 Mbits/sec    0    602 KBytes       
[  5]   1.00-2.00   sec  11.7 MBytes  98.2 Mbits/sec    0   1.11 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.64 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.17 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.70 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.14 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.14 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  89.8 Mbits/sec    0             sender
[  5]   0.00-10.28  sec   107 MBytes  87.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 02:33:57
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 34796 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.9 MBytes  99.5 Mbits/sec    0    774 KBytes       
[  5]   1.00-2.00   sec  12.4 MBytes   104 Mbits/sec    0   1.28 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.81 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.34 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.86 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.6 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   108 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 03:34:08
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 54528 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.7 MBytes  98.0 Mbits/sec    0    786 KBytes       
[  5]   1.00-2.00   sec  12.4 MBytes   104 Mbits/sec    0   1.29 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.82 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.35 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.87 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec  913   1.56 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec   69   1.15 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.22 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.4 Mbits/sec  982             sender
[  5]   0.00-10.16  sec   106 MBytes  87.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 04:34:19
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 57888 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.0 MBytes   101 Mbits/sec    0    764 KBytes       
[  5]   1.00-2.00   sec  11.1 MBytes  93.4 Mbits/sec    0   1.27 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.80 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.33 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.85 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.7 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   108 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 05:34:29
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 34208 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.4 MBytes  95.9 Mbits/sec    0    606 KBytes       
[  5]   1.00-2.00   sec  8.74 MBytes  73.3 Mbits/sec    0    999 KBytes       
[  5]   2.00-3.00   sec  11.1 MBytes  93.5 Mbits/sec    0   1.50 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.03 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.56 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.08 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   105 MBytes  88.1 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   105 MBytes  85.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 06:34:40
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 52692 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.1 MBytes   102 Mbits/sec    0    806 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.1 Mbits/sec    0   1.31 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.84 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.37 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.89 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   109 MBytes  91.1 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   108 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 07:34:51
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 35998 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.5 MBytes  96.4 Mbits/sec    0    596 KBytes       
[  5]   1.00-2.00   sec  11.6 MBytes  97.0 Mbits/sec    0   1.11 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.64 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.15 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.69 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.13 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.13 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.13 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.13 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.13 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.6 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   107 MBytes  87.2 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 08:35:02
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 55752 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.8 MBytes  98.7 Mbits/sec    0    672 KBytes       
[  5]   1.00-2.00   sec  12.5 MBytes   105 Mbits/sec    0   1.18 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.71 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.24 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.76 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.6 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   108 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 09:35:13
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 47836 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  5.71 MBytes  47.9 Mbits/sec    0    303 KBytes       
[  5]   1.00-2.00   sec  10.8 MBytes  90.8 Mbits/sec    0    794 KBytes       
[  5]   2.00-3.00   sec  11.4 MBytes  95.5 Mbits/sec    0   1.30 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.83 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.35 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.88 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.14 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.14 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   102 MBytes  85.3 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   102 MBytes  82.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 10:35:24
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 39058 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.6 MBytes  97.4 Mbits/sec    0    612 KBytes       
[  5]   1.00-2.00   sec  11.6 MBytes  97.0 Mbits/sec    0   1.13 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.65 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.18 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.71 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.13 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.13 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.13 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.13 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.13 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.7 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   108 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 11:35:34
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 43870 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.0 MBytes   101 Mbits/sec    0    794 KBytes       
[  5]   1.00-2.00   sec  9.27 MBytes  77.7 Mbits/sec    0   1.19 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.71 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.24 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.77 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec  829   1.55 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.65 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.73 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.79 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   105 MBytes  88.1 Mbits/sec  829             sender
[  5]   0.00-10.21  sec   104 MBytes  85.2 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 12:35:45
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 41916 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.3 MBytes  94.8 Mbits/sec    0    777 KBytes       
[  5]   1.00-2.00   sec  12.4 MBytes   104 Mbits/sec    0   1.28 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.81 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.34 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.86 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  90.1 Mbits/sec    0             sender
[  5]   0.00-10.34  sec   107 MBytes  87.1 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 13:35:56
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 49216 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.0 MBytes  92.1 Mbits/sec    0    545 KBytes       
[  5]   1.00-2.00   sec  11.8 MBytes  99.1 Mbits/sec    0   1.06 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.2 Mbits/sec    0   1.59 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.11 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.64 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.14 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.14 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.4 Mbits/sec    0             sender
[  5]   0.00-10.32  sec   107 MBytes  87.2 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 14:36:07
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 42728 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.2 MBytes  94.1 Mbits/sec    0    609 KBytes       
[  5]   1.00-2.00   sec  12.8 MBytes   107 Mbits/sec    0   1.12 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.65 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.16 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.70 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.4 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   108 MBytes  87.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 15:36:18
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 49428 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.7 MBytes  98.0 Mbits/sec    0    654 KBytes       
[  5]   1.00-2.00   sec  11.2 MBytes  93.6 Mbits/sec    0   1.17 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.69 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.22 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.74 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.17 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.17 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.5 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   107 MBytes  87.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 16:36:29
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 34174 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  10.2 MBytes  85.5 Mbits/sec    0    486 KBytes       
[  5]   1.00-2.00   sec  11.6 MBytes  97.5 Mbits/sec    0   1.00 MBytes       
[  5]   2.00-3.00   sec  11.1 MBytes  93.5 Mbits/sec    0   1.52 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.05 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.57 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.10 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  89.5 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   107 MBytes  86.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 17:36:40
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 51122 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.3 MBytes   103 Mbits/sec    0    769 KBytes       
[  5]   1.00-2.00   sec  11.3 MBytes  94.4 Mbits/sec    0   1.28 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.80 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.33 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.86 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  90.0 Mbits/sec    0             sender
[  5]   0.00-10.31  sec   107 MBytes  87.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 18:36:50
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 47358 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.9 MBytes   100 Mbits/sec    0    684 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.8 Mbits/sec    0   1.19 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.72 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.25 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.78 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec   36   2.21 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec  823   1.59 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.68 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  91.0 Mbits/sec  859             sender
[  5]   0.00-10.20  sec   107 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 19:37:03
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 60960 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  3.26 MBytes  27.4 Mbits/sec    0    730 KBytes       
[  5]   1.00-2.00   sec  4.68 MBytes  39.2 Mbits/sec    0    937 KBytes       
[  5]   2.00-3.00   sec  5.86 MBytes  49.2 Mbits/sec    0   1.15 MBytes       
[  5]   3.00-4.00   sec  3.75 MBytes  31.5 Mbits/sec    0   1.38 MBytes       
[  5]   4.00-5.00   sec  5.00 MBytes  41.9 Mbits/sec    0   1.60 MBytes       
[  5]   5.00-6.00   sec  5.00 MBytes  41.9 Mbits/sec    0   1.83 MBytes       
[  5]   6.00-7.00   sec  2.50 MBytes  21.0 Mbits/sec    0   2.02 MBytes       
[  5]   7.00-8.00   sec  6.25 MBytes  52.4 Mbits/sec    0   2.30 MBytes       
[  5]   8.00-9.00   sec  6.25 MBytes  52.4 Mbits/sec    0   2.61 MBytes       
[  5]   9.00-10.00  sec  6.25 MBytes  52.4 Mbits/sec    0   2.94 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  48.8 MBytes  40.9 Mbits/sec    0             sender
[  5]   0.00-10.57  sec  48.8 MBytes  38.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 20:37:14
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 53910 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   979 KBytes  8.02 Mbits/sec    0    194 KBytes       
[  5]   1.00-2.00   sec  1.42 MBytes  11.9 Mbits/sec    0    252 KBytes       
[  5]   2.00-3.00   sec  2.71 MBytes  22.7 Mbits/sec    0    373 KBytes       
[  5]   3.00-4.00   sec  4.49 MBytes  37.7 Mbits/sec    0    574 KBytes       
[  5]   4.00-5.00   sec  6.58 MBytes  55.2 Mbits/sec    0    895 KBytes       
[  5]   5.00-6.00   sec  10.8 MBytes  90.5 Mbits/sec    0   1.35 MBytes       
[  5]   6.00-7.00   sec  7.50 MBytes  62.9 Mbits/sec    0   1.76 MBytes       
[  5]   7.00-8.00   sec  8.75 MBytes  73.4 Mbits/sec    0   2.14 MBytes       
[  5]   8.00-9.00   sec  7.50 MBytes  62.9 Mbits/sec    0   2.54 MBytes       
[  5]   9.00-10.00  sec  8.75 MBytes  73.4 Mbits/sec    0   2.96 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  59.4 MBytes  49.9 Mbits/sec    0             sender
[  5]   0.00-10.39  sec  58.9 MBytes  47.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 21:37:25
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 58390 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.7 MBytes  98.3 Mbits/sec    0    601 KBytes       
[  5]   1.00-2.00   sec  11.6 MBytes  97.5 Mbits/sec    0   1.11 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.64 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.17 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.70 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.14 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.14 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.14 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.9 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   108 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 22:37:36
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 54824 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.9 MBytes  99.6 Mbits/sec    0    786 KBytes       
[  5]   1.00-2.00   sec  12.4 MBytes   104 Mbits/sec    0   1.30 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.82 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.35 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.88 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.17 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.17 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.7 Mbits/sec    0             sender
[  5]   0.00-10.34  sec   108 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-04 23:37:47
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 36378 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.5 MBytes  96.4 Mbits/sec    0    612 KBytes       
[  5]   1.00-2.00   sec  12.0 MBytes   101 Mbits/sec    0   1.12 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.65 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.18 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.71 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   109 MBytes  91.0 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   108 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 00:37:58
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 49770 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.8 MBytes  99.0 Mbits/sec    0    623 KBytes       
[  5]   1.00-2.00   sec  11.9 MBytes  99.8 Mbits/sec    0   1.14 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.66 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.18 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.70 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.17 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.17 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  90.1 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   107 MBytes  87.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 01:38:08
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 54312 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.1 MBytes   101 Mbits/sec    0    675 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.8 Mbits/sec    0   1.19 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.71 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.24 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.77 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   109 MBytes  91.1 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   108 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 02:38:19
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 39380 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  5.98 MBytes  50.2 Mbits/sec    0    290 KBytes       
[  5]   1.00-2.00   sec  11.4 MBytes  96.0 Mbits/sec    0    794 KBytes       
[  5]   2.00-3.00   sec  11.5 MBytes  96.6 Mbits/sec    0   1.30 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.83 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.36 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.88 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.17 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.17 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   103 MBytes  86.1 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   102 MBytes  83.0 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 03:38:30
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 48966 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  8.51 MBytes  71.4 Mbits/sec    0    427 KBytes       
[  5]   1.00-2.00   sec  11.8 MBytes  99.1 Mbits/sec    0    948 KBytes       
[  5]   2.00-3.00   sec  11.0 MBytes  92.3 Mbits/sec    0   1.45 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.98 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.51 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.03 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.13 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.13 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.13 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.13 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   105 MBytes  88.1 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   105 MBytes  84.9 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 04:38:41
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 60684 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.8 MBytes  99.0 Mbits/sec    0    609 KBytes       
[  5]   1.00-2.00   sec  11.7 MBytes  98.1 Mbits/sec    0   1.12 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.65 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.16 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.70 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.14 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.14 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.14 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  91.0 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   108 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 05:38:52
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 47726 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.7 MBytes  98.5 Mbits/sec    0    623 KBytes       
[  5]   1.00-2.00   sec  11.9 MBytes  99.8 Mbits/sec    0   1.14 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.66 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.19 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.72 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   109 MBytes  91.1 Mbits/sec    0             sender
[  5]   0.00-10.34  sec   108 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 06:39:02
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 32928 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.4 MBytes   104 Mbits/sec    0   1009 KBytes       
[  5]   1.00-2.00   sec  11.1 MBytes  93.5 Mbits/sec    0   1.51 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.04 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.57 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.10 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   109 MBytes  91.0 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   108 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 07:39:13
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 50322 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.5 MBytes  96.3 Mbits/sec    0    752 KBytes       
[  5]   1.00-2.00   sec  12.1 MBytes   102 Mbits/sec    0   1.26 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.79 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.31 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.84 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  90.0 Mbits/sec    0             sender
[  5]   0.00-10.31  sec   107 MBytes  87.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 08:39:24
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 53220 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.1 MBytes   102 Mbits/sec    0    652 KBytes       
[  5]   1.00-2.00   sec  11.3 MBytes  94.6 Mbits/sec    0   1.16 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.69 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.22 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.75 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec   23   2.20 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  89.9 Mbits/sec   23             sender
[  5]   0.00-10.20  sec   105 MBytes  86.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 09:39:35
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 53984 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.7 MBytes  98.2 Mbits/sec    0    761 KBytes       
[  5]   1.00-2.00   sec  12.2 MBytes   103 Mbits/sec    0   1.27 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.80 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.33 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.85 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec  237   1.53 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec  502   1.61 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.69 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.76 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.80 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.3 Mbits/sec  739             sender
[  5]   0.00-10.22  sec   106 MBytes  87.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 10:39:46
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 40206 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  10.1 MBytes  84.6 Mbits/sec    0    513 KBytes       
[  5]   1.00-2.00   sec  12.0 MBytes   101 Mbits/sec    0   1.03 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.2 Mbits/sec    0   1.55 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.08 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.61 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  89.8 Mbits/sec    0             sender
[  5]   0.00-10.34  sec   107 MBytes  86.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 11:40:09
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 36964 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   119 KBytes   978 Kbits/sec    0   31.5 KBytes       
[  5]   1.00-2.00   sec  89.2 KBytes   731 Kbits/sec    0   35.4 KBytes       
[  5]   2.00-3.00   sec   106 KBytes   871 Kbits/sec    0   39.4 KBytes       
[  5]   3.00-4.00   sec   110 KBytes   903 Kbits/sec    0   48.6 KBytes       
[  5]   4.00-5.00   sec  77.4 KBytes   634 Kbits/sec    0   63.0 KBytes       
[  5]   5.00-6.00   sec   138 KBytes  1.13 Mbits/sec    0   90.6 KBytes       
[  5]   6.00-7.00   sec   126 KBytes  1.03 Mbits/sec    0    125 KBytes       
[  5]   7.00-8.00   sec   189 KBytes  1.55 Mbits/sec    0    172 KBytes       
[  5]   8.00-9.00   sec   252 KBytes  2.06 Mbits/sec    0    200 KBytes       
[  5]   9.00-10.00  sec   315 KBytes  2.58 Mbits/sec    0    259 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.49 MBytes  1.25 Mbits/sec    0             sender
[  5]   0.00-13.67  sec  1.01 MBytes   618 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 12:40:31
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 34272 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   113 KBytes   924 Kbits/sec    0   31.5 KBytes       
[  5]   1.00-2.00   sec   104 KBytes   849 Kbits/sec    0   53.8 KBytes       
[  5]   2.00-3.00   sec  86.6 KBytes   710 Kbits/sec    0   57.8 KBytes       
[  5]   3.00-4.00   sec  77.4 KBytes   635 Kbits/sec    0   60.4 KBytes       
[  5]   4.00-5.00   sec   138 KBytes  1.13 Mbits/sec    0   72.2 KBytes       
[  5]   5.00-6.00   sec  0.00 Bytes  0.00 bits/sec    0   97.1 KBytes       
[  5]   6.00-7.00   sec  0.00 Bytes  0.00 bits/sec    0   97.1 KBytes       
[  5]   7.00-8.00   sec   449 KBytes  3.68 Mbits/sec    0    171 KBytes       
[  5]   8.00-9.00   sec  0.00 Bytes  0.00 bits/sec    0    198 KBytes       
[  5]   9.00-10.00  sec   315 KBytes  2.58 Mbits/sec    0    244 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.25 MBytes  1.05 Mbits/sec    0             sender
[  5]   0.00-13.00  sec   865 KBytes   545 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 13:40:50
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 53454 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   110 KBytes   903 Kbits/sec    0   30.2 KBytes       
[  5]   1.00-2.00   sec  70.9 KBytes   580 Kbits/sec    0   57.8 KBytes       
[  5]   2.00-3.00   sec  94.5 KBytes   774 Kbits/sec    0   63.0 KBytes       
[  5]   3.00-4.00   sec   150 KBytes  1.23 Mbits/sec    0   66.9 KBytes       
[  5]   4.00-5.00   sec  0.00 Bytes  0.00 bits/sec    0   77.4 KBytes       
[  5]   5.00-6.00   sec   130 KBytes  1.06 Mbits/sec    0   95.8 KBytes       
[  5]   6.00-7.00   sec   126 KBytes  1.03 Mbits/sec    0    114 KBytes       
[  5]   7.00-8.00   sec  0.00 Bytes  0.00 bits/sec    0    134 KBytes       
[  5]   8.00-9.00   sec   252 KBytes  2.07 Mbits/sec    0    178 KBytes       
[  5]   9.00-10.00  sec  0.00 Bytes  0.00 bits/sec    0    193 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   933 KBytes   764 Kbits/sec    0             sender
[  5]   0.00-11.47  sec   726 KBytes   519 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 14:41:01
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 56078 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.53 MBytes  12.9 Mbits/sec    0   94.5 KBytes       
[  5]   1.00-2.00   sec  4.55 MBytes  38.2 Mbits/sec    0    295 KBytes       
[  5]   2.00-3.00   sec  11.0 MBytes  92.4 Mbits/sec    0    797 KBytes       
[  5]   3.00-4.00   sec  11.4 MBytes  95.6 Mbits/sec    0   1.31 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.83 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.36 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.88 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.14 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec   58   2.20 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  92.2 MBytes  77.4 Mbits/sec   58             sender
[  5]   0.00-10.19  sec  89.5 MBytes  73.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 15:41:12
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 35628 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.5 MBytes  96.3 Mbits/sec    0    662 KBytes       
[  5]   1.00-2.00   sec  11.3 MBytes  95.1 Mbits/sec    0   1.17 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.70 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.23 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.75 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.4 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   107 MBytes  87.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 16:41:23
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 40126 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  2.80 MBytes  23.5 Mbits/sec    1    231 KBytes       
[  5]   1.00-2.00   sec  10.9 MBytes  91.3 Mbits/sec    0    727 KBytes       
[  5]   2.00-3.00   sec  12.0 MBytes   101 Mbits/sec    0   1.24 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.76 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.28 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.81 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  99.4 MBytes  83.4 Mbits/sec    1             sender
[  5]   0.00-10.33  sec  99.0 MBytes  80.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 17:41:34
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 58378 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  4.96 MBytes  41.6 Mbits/sec    0    277 KBytes       
[  5]   1.00-2.00   sec  11.8 MBytes  98.6 Mbits/sec    0    820 KBytes       
[  5]   2.00-3.00   sec  11.5 MBytes  96.1 Mbits/sec    0   1.33 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.86 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.38 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.91 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   102 MBytes  85.5 Mbits/sec    0             sender
[  5]   0.00-10.29  sec   102 MBytes  83.1 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 18:41:48
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 49068 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   125 KBytes  1.02 Mbits/sec    0   31.5 KBytes       
[  5]   1.00-2.00   sec  82.7 KBytes   677 Kbits/sec    0   35.4 KBytes       
[  5]   2.00-3.00   sec   274 KBytes  2.25 Mbits/sec    0   47.2 KBytes       
[  5]   3.00-4.00   sec   266 KBytes  2.18 Mbits/sec    0   60.4 KBytes       
[  5]   4.00-5.00   sec   394 KBytes  3.23 Mbits/sec    0   76.1 KBytes       
[  5]   5.00-6.00   sec   378 KBytes  3.10 Mbits/sec    0   95.8 KBytes       
[  5]   6.00-7.00   sec   567 KBytes  4.65 Mbits/sec    0    148 KBytes       
[  5]   7.00-8.00   sec   504 KBytes  4.13 Mbits/sec    0    211 KBytes       
[  5]   8.00-9.00   sec  1008 KBytes  8.26 Mbits/sec    0    294 KBytes       
[  5]   9.00-10.00  sec  1.29 MBytes  10.8 Mbits/sec    0    415 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  4.81 MBytes  4.03 Mbits/sec    0             sender
[  5]   0.00-10.60  sec  4.00 MBytes  3.16 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 19:42:11
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 49114 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   189 KBytes  1.55 Mbits/sec    0   44.6 KBytes       
[  5]   1.00-2.00   sec   280 KBytes  2.30 Mbits/sec    0    178 KBytes       
[  5]   2.00-3.00   sec   315 KBytes  2.58 Mbits/sec    0    192 KBytes       
[  5]   3.00-4.00   sec   252 KBytes  2.06 Mbits/sec    0    200 KBytes       
[  5]   4.00-5.00   sec   315 KBytes  2.58 Mbits/sec    0    209 KBytes       
[  5]   5.00-6.00   sec  0.00 Bytes  0.00 bits/sec    0    215 KBytes       
[  5]   6.00-7.00   sec   315 KBytes  2.58 Mbits/sec    0    223 KBytes       
[  5]   7.00-8.00   sec  0.00 Bytes  0.00 bits/sec    0    249 KBytes       
[  5]   8.00-9.00   sec  0.00 Bytes  0.00 bits/sec    0    268 KBytes       
[  5]   9.00-10.00  sec   378 KBytes  3.10 Mbits/sec    0    312 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  2.00 MBytes  1.67 Mbits/sec    0             sender
[  5]   0.00-13.77  sec  1.49 MBytes   909 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 20:42:31
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 39304 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    0   21.0 KBytes       
[  5]   1.00-2.00   sec  86.6 KBytes   710 Kbits/sec    0   32.8 KBytes       
[  5]   2.00-3.00   sec   104 KBytes   849 Kbits/sec    0   34.1 KBytes       
[  5]   3.00-4.00   sec  0.00 Bytes  0.00 bits/sec    0   36.8 KBytes       
[  5]   4.00-5.00   sec   102 KBytes   839 Kbits/sec    0   49.9 KBytes       
[  5]   5.00-6.00   sec   146 KBytes  1.19 Mbits/sec    0   69.6 KBytes       
[  5]   6.00-7.00   sec  0.00 Bytes  0.00 bits/sec    0   93.2 KBytes       
[  5]   7.00-8.00   sec   333 KBytes  2.73 Mbits/sec    0    148 KBytes       
[  5]   8.00-9.00   sec   252 KBytes  2.06 Mbits/sec    0    186 KBytes       
[  5]   9.00-10.00  sec  0.00 Bytes  0.00 bits/sec    0    226 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.04 MBytes   875 Kbits/sec    0             sender
[  5]   0.00-13.03  sec   785 KBytes   493 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-05 21:42:50
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 53412 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   116 KBytes   946 Kbits/sec    0   32.8 KBytes       
[  5]   1.00-2.00   sec   173 KBytes  1.42 Mbits/sec    0   90.6 KBytes       
[  5]   2.00-3.00   sec   142 KBytes  1.16 Mbits/sec    0   93.2 KBytes       
[  5]   3.00-4.00   sec   126 KBytes  1.03 Mbits/sec    0   98.4 KBytes       
[  5]   4.00-5.00   sec  0.00 Bytes  0.00 bits/sec    0    102 KBytes       
[  5]   5.00-6.00   sec   189 KBytes  1.55 Mbits/sec    0    114 KBytes       
[  5]   6.00-7.00   sec  0.00 Bytes  0.00 bits/sec    0    133 KBytes       
[  5]   7.00-8.00   sec   189 KBytes  1.55 Mbits/sec    0    177 KBytes       
[  5]   8.00-9.00   sec   252 KBytes  2.06 Mbits/sec    0    211 KBytes       
[  5]   9.00-10.00  sec  0.00 Bytes  0.00 bits/sec    0    243 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.16 MBytes   972 Kbits/sec    0             sender
[  5]   0.00-13.41  sec   952 KBytes   581 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-06 10:07:30
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 43552 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  4.15 MBytes  34.8 Mbits/sec    0    210 KBytes       
[  5]   1.00-2.00   sec  9.97 MBytes  83.6 Mbits/sec    0    655 KBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  93.6 Mbits/sec    0   1.15 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.68 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.20 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.73 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.17 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.17 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  99.0 MBytes  83.1 Mbits/sec    0             sender
[  5]   0.00-10.32  sec  99.0 MBytes  80.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-06 11:07:40
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 48862 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  10.0 MBytes  84.1 Mbits/sec    0    528 KBytes       
[  5]   1.00-2.00   sec  11.4 MBytes  96.0 Mbits/sec    0   1.04 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.2 Mbits/sec    0   1.57 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.10 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.62 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   106 MBytes  89.3 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   106 MBytes  86.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-06 12:07:51
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 59240 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.7 MBytes  98.2 Mbits/sec    0    610 KBytes       
[  5]   1.00-2.00   sec  11.8 MBytes  98.7 Mbits/sec    0   1.12 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.65 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.18 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.70 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  91.0 Mbits/sec    0             sender
[  5]   0.00-10.33  sec   108 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-06 13:08:02
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 53824 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  3.01 MBytes  25.2 Mbits/sec    0    190 KBytes       
[  5]   1.00-2.00   sec  8.92 MBytes  74.8 Mbits/sec    0    597 KBytes       
[  5]   2.00-3.00   sec  11.3 MBytes  94.4 Mbits/sec    0   1.09 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.61 MBytes       
[  5]   4.00-5.00   sec  8.75 MBytes  73.4 Mbits/sec    0   2.08 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.61 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.15 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.15 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  95.7 MBytes  80.3 Mbits/sec    0             sender
[  5]   0.00-10.29  sec  95.7 MBytes  78.0 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-06 14:08:13
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 58702 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  6.31 MBytes  52.9 Mbits/sec    0    312 KBytes       
[  5]   1.00-2.00   sec  9.29 MBytes  77.9 Mbits/sec    0    734 KBytes       
[  5]   2.00-3.00   sec  10.7 MBytes  90.1 Mbits/sec    0   1.18 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.70 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.22 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.75 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   100 MBytes  84.0 Mbits/sec    0             sender
[  5]   0.00-10.33  sec  99.7 MBytes  80.9 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-06 15:08:24
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 40790 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  9.57 MBytes  80.3 Mbits/sec    0    511 KBytes       
[  5]   1.00-2.00   sec  12.1 MBytes   101 Mbits/sec    0   1.03 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.2 Mbits/sec    0   1.56 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.08 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.61 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.14 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec  610   1.55 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec   82   1.14 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.21 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  89.4 Mbits/sec  692             sender
[  5]   0.00-10.17  sec   104 MBytes  85.9 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-06 16:08:35
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 56718 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  4.27 MBytes  35.8 Mbits/sec    0    217 KBytes       
[  5]   1.00-2.00   sec  8.12 MBytes  68.1 Mbits/sec    0    598 KBytes       
[  5]   2.00-3.00   sec  11.4 MBytes  95.5 Mbits/sec    0   1.06 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.56 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.09 MBytes       
[  5]   5.00-6.00   sec  8.75 MBytes  73.4 Mbits/sec    0   2.49 MBytes       
[  5]   6.00-7.00   sec  12.5 MBytes   105 Mbits/sec  747   1.35 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.43 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.50 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.55 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  96.3 MBytes  80.8 Mbits/sec  747             sender
[  5]   0.00-10.19  sec  94.4 MBytes  77.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-06 17:08:46
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 53688 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  9.36 MBytes  78.5 Mbits/sec    0    656 KBytes       
[  5]   1.00-2.00   sec  10.2 MBytes  85.2 Mbits/sec    0   1.10 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.62 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.13 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.65 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.17 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.17 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.17 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   103 MBytes  86.6 Mbits/sec    0             sender
[  5]   0.00-10.31  sec   103 MBytes  84.0 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-06 18:08:56
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 60104 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.3 MBytes  94.8 Mbits/sec    0    655 KBytes       
[  5]   1.00-2.00   sec  12.3 MBytes   104 Mbits/sec    0   1.18 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.71 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.24 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.76 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   3.16 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   3.16 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  90.1 Mbits/sec    0             sender
[  5]   0.00-10.29  sec   107 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-06 19:09:11
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 44652 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   147 KBytes  1.20 Mbits/sec    0   31.5 KBytes       
[  5]   1.00-2.00   sec  99.8 KBytes   817 Kbits/sec    0   36.8 KBytes       
[  5]   2.00-3.00   sec  95.8 KBytes   785 Kbits/sec    0   40.7 KBytes       
[  5]   3.00-4.00   sec  90.6 KBytes   742 Kbits/sec    0   47.2 KBytes       
[  5]   4.00-5.00   sec   290 KBytes  2.38 Mbits/sec    0   65.6 KBytes       
[  5]   5.00-6.00   sec   126 KBytes  1.03 Mbits/sec    0   93.2 KBytes       
[  5]   6.00-7.00   sec   378 KBytes  3.10 Mbits/sec    0    140 KBytes       
[  5]   7.00-8.00   sec   441 KBytes  3.61 Mbits/sec    0    197 KBytes       
[  5]   8.00-9.00   sec   567 KBytes  4.65 Mbits/sec    0    278 KBytes       
[  5]   9.00-10.00  sec   819 KBytes  6.71 Mbits/sec    0    381 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  2.98 MBytes  2.50 Mbits/sec    0             sender
[  5]   0.00-11.01  sec  2.27 MBytes  1.73 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-06 20:09:27
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 38896 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    0   14.4 KBytes       
[  5]   1.00-2.00   sec   358 KBytes  2.94 Mbits/sec    0   94.5 KBytes       
[  5]   2.00-3.00   sec  0.00 Bytes  0.00 bits/sec    0    104 KBytes       
[  5]   3.00-4.00   sec   150 KBytes  1.23 Mbits/sec    0    110 KBytes       
[  5]   4.00-5.00   sec   189 KBytes  1.55 Mbits/sec    0    116 KBytes       
[  5]   5.00-6.00   sec   189 KBytes  1.55 Mbits/sec    0    122 KBytes       
[  5]   6.00-7.00   sec   189 KBytes  1.55 Mbits/sec    0    142 KBytes       
[  5]   7.00-8.00   sec   252 KBytes  2.06 Mbits/sec    0    172 KBytes       
[  5]   8.00-9.00   sec   252 KBytes  2.06 Mbits/sec    0    192 KBytes       
[  5]   9.00-10.00  sec   315 KBytes  2.58 Mbits/sec    0    249 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.89 MBytes  1.59 Mbits/sec    0             sender
[  5]   0.00-10.39  sec  1.43 MBytes  1.15 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-06 21:09:42
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 37458 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    0   19.7 KBytes       
[  5]   1.00-2.00   sec   177 KBytes  1.45 Mbits/sec    0   34.1 KBytes       
[  5]   2.00-3.00   sec   104 KBytes   849 Kbits/sec    0   39.4 KBytes       
[  5]   3.00-4.00   sec  0.00 Bytes  0.00 bits/sec    0   42.0 KBytes       
[  5]   4.00-5.00   sec   188 KBytes  1.54 Mbits/sec    0   59.1 KBytes       
[  5]   5.00-6.00   sec   228 KBytes  1.87 Mbits/sec    0   84.0 KBytes       
[  5]   6.00-7.00   sec   189 KBytes  1.55 Mbits/sec    0    126 KBytes       
[  5]   7.00-8.00   sec   315 KBytes  2.58 Mbits/sec    0    180 KBytes       
[  5]   8.00-9.00   sec   630 KBytes  5.16 Mbits/sec    0    251 KBytes       
[  5]   9.00-10.00  sec   378 KBytes  3.10 Mbits/sec    0    343 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  2.20 MBytes  1.85 Mbits/sec    0             sender
[  5]   0.00-10.79  sec  1.74 MBytes  1.36 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-06 22:10:01
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 58206 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    0   17.1 KBytes       
[  5]   1.00-2.00   sec  70.9 KBytes   581 Kbits/sec    0   31.5 KBytes       
[  5]   2.00-3.00   sec  72.2 KBytes   592 Kbits/sec    0   34.1 KBytes       
[  5]   3.00-4.00   sec  0.00 Bytes  0.00 bits/sec    0   43.3 KBytes       
[  5]   4.00-5.00   sec   105 KBytes   861 Kbits/sec    0   49.9 KBytes       
[  5]   5.00-6.00   sec   135 KBytes  1.11 Mbits/sec    0   72.2 KBytes       
[  5]   6.00-7.00   sec   126 KBytes  1.03 Mbits/sec    0    101 KBytes       
[  5]   7.00-8.00   sec   189 KBytes  1.55 Mbits/sec    0    134 KBytes       
[  5]   8.00-9.00   sec  0.00 Bytes  0.00 bits/sec    0    165 KBytes       
[  5]   9.00-10.00  sec   252 KBytes  2.07 Mbits/sec    0    201 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   995 KBytes   815 Kbits/sec    0             sender
[  5]   0.00-12.29  sec   659 KBytes   439 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-06 23:10:11
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 58762 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.3 MBytes  94.6 Mbits/sec    0    722 KBytes       
[  5]   1.00-2.00   sec  12.0 MBytes   101 Mbits/sec    0   1.23 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.76 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec   18   1.97 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec   65   1.69 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.83 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.95 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.04 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.11 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    8   1.51 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  89.8 Mbits/sec   91             sender
[  5]   0.00-10.19  sec   106 MBytes  86.9 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 00:10:22
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 37098 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.5 MBytes   105 Mbits/sec    0    772 KBytes       
[  5]   1.00-2.00   sec  11.4 MBytes  96.0 Mbits/sec    0   1.27 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.80 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec   57   1.58 MBytes       
[  5]   4.00-5.00   sec  12.5 MBytes   105 Mbits/sec   32   1.71 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.85 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.97 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.06 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.13 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec  484   1.06 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.3 Mbits/sec  573             sender
[  5]   0.00-10.15  sec   106 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 01:10:33
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 34550 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.6 MBytes  97.3 Mbits/sec    0    782 KBytes       
[  5]   1.00-2.00   sec  12.7 MBytes   106 Mbits/sec    0   1.30 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.83 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec   46   1.46 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.60 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.72 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.81 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.88 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.93 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.97 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.6 Mbits/sec   46             sender
[  5]   0.00-10.24  sec   106 MBytes  87.1 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 02:10:44
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 57260 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  13.2 MBytes   110 Mbits/sec    0    979 KBytes       
[  5]   1.00-2.00   sec  9.90 MBytes  83.0 Mbits/sec    0   1.48 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.01 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec  463   1.11 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.18 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.24 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.29 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.32 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.33 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.34 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.6 Mbits/sec  463             sender
[  5]   0.00-10.15  sec   106 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 03:10:55
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 45210 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.0 MBytes   101 Mbits/sec    0    823 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.6 Mbits/sec    0   1.33 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.86 MBytes       
[  5]   3.00-4.00   sec  7.50 MBytes  62.9 Mbits/sec   92   1.58 MBytes       
[  5]   4.00-5.00   sec  12.5 MBytes   105 Mbits/sec    0   1.72 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.86 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.98 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.07 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.13 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec  206   1.07 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   109 MBytes  91.1 Mbits/sec  298             sender
[  5]   0.00-10.15  sec   106 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 04:11:05
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 34492 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.5 MBytes   105 Mbits/sec    0    785 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.1 Mbits/sec    0   1.30 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.82 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec   73   1.58 MBytes       
[  5]   4.00-5.00   sec  12.5 MBytes   105 Mbits/sec   16   1.71 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.85 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.97 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.06 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.13 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec  563   1.06 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.4 Mbits/sec  652             sender
[  5]   0.00-10.15  sec   106 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 05:11:16
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 52508 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.0 MBytes   100 Mbits/sec    0    677 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.8 Mbits/sec    0   1.19 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.72 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.24 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  279   1.14 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.21 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.26 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.30 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.32 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.34 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  91.0 Mbits/sec  279             sender
[  5]   0.00-10.17  sec   106 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 06:11:27
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 42244 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  9.39 MBytes  78.8 Mbits/sec    0    454 KBytes       
[  5]   1.00-2.00   sec  11.8 MBytes  99.1 Mbits/sec    0    994 KBytes       
[  5]   2.00-3.00   sec  11.1 MBytes  93.5 Mbits/sec    0   1.50 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.03 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  481   1.11 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.18 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.24 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.29 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.31 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   106 MBytes  89.0 Mbits/sec  481             sender
[  5]   0.00-10.17  sec   105 MBytes  86.2 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 07:11:38
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 59118 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.7 MBytes  97.9 Mbits/sec    0    692 KBytes       
[  5]   1.00-2.00   sec  11.5 MBytes  96.8 Mbits/sec    0   1.20 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.73 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec   10   2.21 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  517   1.14 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.21 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.26 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.30 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.34 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  89.7 Mbits/sec  527             sender
[  5]   0.00-10.15  sec   105 MBytes  87.2 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 08:11:48
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 45790 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.0 MBytes   101 Mbits/sec    0    785 KBytes       
[  5]   1.00-2.00   sec  11.3 MBytes  94.4 Mbits/sec    0   1.29 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.82 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec   87   1.58 MBytes       
[  5]   4.00-5.00   sec  12.5 MBytes   105 Mbits/sec  392   1.16 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.23 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.27 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.31 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.34 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.8 Mbits/sec  479             sender
[  5]   0.00-10.17  sec   106 MBytes  87.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 09:11:59
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 60974 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  7.94 MBytes  66.6 Mbits/sec    0    410 KBytes       
[  5]   1.00-2.00   sec  9.35 MBytes  78.4 Mbits/sec    0    835 KBytes       
[  5]   2.00-3.00   sec  11.9 MBytes  99.7 Mbits/sec    0   1.33 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.85 MBytes       
[  5]   4.00-5.00   sec  8.75 MBytes  73.4 Mbits/sec   83   1.58 MBytes       
[  5]   5.00-6.00   sec  12.5 MBytes   105 Mbits/sec  111   1.16 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.23 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.28 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.31 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   102 MBytes  85.3 Mbits/sec  194             sender
[  5]   0.00-10.19  sec   100 MBytes  82.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 10:12:11
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 51938 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   469 KBytes  3.84 Mbits/sec    0   45.9 KBytes       
[  5]   1.00-2.00   sec   957 KBytes  7.84 Mbits/sec    0   87.9 KBytes       
[  5]   2.00-3.00   sec  1.29 MBytes  10.8 Mbits/sec    0    152 KBytes       
[  5]   3.00-4.00   sec  1.91 MBytes  16.0 Mbits/sec    0    239 KBytes       
[  5]   4.00-5.00   sec  2.03 MBytes  17.0 Mbits/sec    0    335 KBytes       
[  5]   5.00-6.00   sec  2.77 MBytes  23.2 Mbits/sec    0    449 KBytes       
[  5]   6.00-7.00   sec  1.78 MBytes  15.0 Mbits/sec    0    534 KBytes       
[  5]   7.00-8.00   sec  1.97 MBytes  16.5 Mbits/sec    0    617 KBytes       
[  5]   8.00-9.00   sec  1.54 MBytes  12.9 Mbits/sec    0    692 KBytes       
[  5]   9.00-10.00  sec  2.58 MBytes  21.7 Mbits/sec    0    810 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  17.3 MBytes  14.5 Mbits/sec    0             sender
[  5]   0.00-10.31  sec  16.0 MBytes  13.0 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 11:12:21
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 38726 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  7.34 MBytes  61.5 Mbits/sec    0    484 KBytes       
[  5]   1.00-2.00   sec  8.67 MBytes  72.8 Mbits/sec    0    892 KBytes       
[  5]   2.00-3.00   sec  12.1 MBytes   101 Mbits/sec    0   1.40 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec    0   1.85 MBytes       
[  5]   4.00-5.00   sec  8.75 MBytes  73.4 Mbits/sec   83   1.58 MBytes       
[  5]   5.00-6.00   sec  12.5 MBytes   105 Mbits/sec    6   1.16 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.23 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.28 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.31 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.33 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  99.3 MBytes  83.3 Mbits/sec   89             sender
[  5]   0.00-10.17  sec  97.8 MBytes  80.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 12:12:33
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 55298 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   656 KBytes  5.37 Mbits/sec    0   74.8 KBytes       
[  5]   1.00-2.00   sec  2.52 MBytes  21.2 Mbits/sec    0    184 KBytes       
[  5]   2.00-3.00   sec  8.74 MBytes  73.3 Mbits/sec    0    570 KBytes       
[  5]   3.00-4.00   sec  11.0 MBytes  92.4 Mbits/sec    0   1.05 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.2 Mbits/sec    0   1.58 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.10 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec  279   1.12 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.20 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.26 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.30 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  85.4 MBytes  71.6 Mbits/sec  279             sender
[  5]   0.00-10.20  sec  83.8 MBytes  68.9 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 13:12:43
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 53720 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.8 MBytes  99.0 Mbits/sec    0    605 KBytes       
[  5]   1.00-2.00   sec  11.8 MBytes  99.3 Mbits/sec    0   1.12 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.65 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.17 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec  305   1.14 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.22 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.28 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.32 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.35 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.37 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  90.1 Mbits/sec  305             sender
[  5]   0.00-10.18  sec   106 MBytes  87.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 14:12:54
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 44886 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  3.19 MBytes  26.7 Mbits/sec    0    167 KBytes       
[  5]   1.00-2.00   sec  10.2 MBytes  85.2 Mbits/sec    1    617 KBytes       
[  5]   2.00-3.00   sec  11.9 MBytes  99.8 Mbits/sec    0   1.13 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.64 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.17 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec   76   1.64 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.79 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.91 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.00 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   2.07 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  97.7 MBytes  82.0 Mbits/sec   77             sender
[  5]   0.00-10.25  sec  97.3 MBytes  79.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 15:13:05
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 41816 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.67 MBytes  14.0 Mbits/sec    0    126 KBytes       
[  5]   1.00-2.00   sec  6.83 MBytes  57.3 Mbits/sec    0    428 KBytes       
[  5]   2.00-3.00   sec  12.1 MBytes   101 Mbits/sec    0    952 KBytes       
[  5]   3.00-4.00   sec  9.88 MBytes  82.9 Mbits/sec    0   1.45 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.94 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.47 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec  511   1.32 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.40 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.47 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.52 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  94.2 MBytes  79.0 Mbits/sec  511             sender
[  5]   0.00-10.19  sec  92.1 MBytes  75.8 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 16:13:16
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 46568 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  6.70 MBytes  56.2 Mbits/sec    0    335 KBytes       
[  5]   1.00-2.00   sec  11.8 MBytes  99.1 Mbits/sec    0    873 KBytes       
[  5]   2.00-3.00   sec  11.8 MBytes  98.9 Mbits/sec    0   1.38 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.90 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.43 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec  171   1.63 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec  197   1.42 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.49 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.55 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.59 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   104 MBytes  87.3 Mbits/sec  368             sender
[  5]   0.00-10.20  sec   102 MBytes  83.9 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 17:13:27
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 55616 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  9.08 MBytes  76.1 Mbits/sec    0    496 KBytes       
[  5]   1.00-2.00   sec  12.1 MBytes   101 Mbits/sec    0   1021 KBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.2 Mbits/sec    0   1.53 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.06 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.58 MBytes       
[  5]   5.00-6.00   sec  11.2 MBytes  94.4 Mbits/sec  385   1.36 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.45 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.52 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.57 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.60 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   106 MBytes  89.0 Mbits/sec  385             sender
[  5]   0.00-10.19  sec   104 MBytes  85.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 18:13:38
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 36224 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  5.00 MBytes  42.0 Mbits/sec    0    368 KBytes       
[  5]   1.00-2.00   sec  11.1 MBytes  93.4 Mbits/sec    0    866 KBytes       
[  5]   2.00-3.00   sec  10.7 MBytes  89.6 Mbits/sec    0   1.34 MBytes       
[  5]   3.00-4.00   sec  8.75 MBytes  73.4 Mbits/sec    0   1.79 MBytes       
[  5]   4.00-5.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.30 MBytes       
[  5]   5.00-6.00   sec  8.75 MBytes  73.4 Mbits/sec   60   1.92 MBytes       
[  5]   6.00-7.00   sec  12.5 MBytes   105 Mbits/sec  466   1.40 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.48 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.54 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.58 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  98.1 MBytes  82.3 Mbits/sec  526             sender
[  5]   0.00-10.19  sec  97.1 MBytes  79.9 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 19:13:56
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 55698 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   110 KBytes   903 Kbits/sec    0   30.2 KBytes       
[  5]   1.00-2.00   sec  85.3 KBytes   699 Kbits/sec    0   32.8 KBytes       
[  5]   2.00-3.00   sec  0.00 Bytes  0.00 bits/sec    0   35.4 KBytes       
[  5]   3.00-4.00   sec  99.8 KBytes   817 Kbits/sec    0   43.3 KBytes       
[  5]   4.00-5.00   sec  94.5 KBytes   774 Kbits/sec    0   53.8 KBytes       
[  5]   5.00-6.00   sec   206 KBytes  1.69 Mbits/sec    0   73.5 KBytes       
[  5]   6.00-7.00   sec   189 KBytes  1.55 Mbits/sec    0    112 KBytes       
[  5]   7.00-8.00   sec   189 KBytes  1.55 Mbits/sec    0    151 KBytes       
[  5]   8.00-9.00   sec  0.00 Bytes  0.00 bits/sec    0    196 KBytes       
[  5]   9.00-10.00  sec   252 KBytes  2.06 Mbits/sec    0    217 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.20 MBytes  1.00 Mbits/sec    0             sender
[  5]   0.00-12.37  sec   841 KBytes   557 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 20:14:16
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 54232 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    0   17.1 KBytes       
[  5]   1.00-2.00   sec  68.2 KBytes   559 Kbits/sec    0   31.5 KBytes       
[  5]   2.00-3.00   sec  0.00 Bytes  0.00 bits/sec    0   31.5 KBytes       
[  5]   3.00-4.00   sec  66.9 KBytes   549 Kbits/sec    0   34.1 KBytes       
[  5]   4.00-5.00   sec  0.00 Bytes  0.00 bits/sec    0   39.4 KBytes       
[  5]   5.00-6.00   sec  90.6 KBytes   742 Kbits/sec    0   51.2 KBytes       
[  5]   6.00-7.00   sec  0.00 Bytes  0.00 bits/sec    0   63.0 KBytes       
[  5]   7.00-8.00   sec   134 KBytes  1.10 Mbits/sec    0   84.0 KBytes       
[  5]   8.00-9.00   sec   126 KBytes  1.03 Mbits/sec    0    119 KBytes       
[  5]   9.00-10.00  sec   189 KBytes  1.55 Mbits/sec    0    139 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   719 KBytes   589 Kbits/sec    0             sender
[  5]   0.00-12.51  sec   433 KBytes   284 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 21:14:37
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 54522 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  44.6 KBytes   365 Kbits/sec    0   27.6 KBytes       
[  5]   1.00-2.00   sec   173 KBytes  1.42 Mbits/sec    0   32.8 KBytes       
[  5]   2.00-3.00   sec  0.00 Bytes  0.00 bits/sec    0   35.4 KBytes       
[  5]   3.00-4.00   sec  90.6 KBytes   742 Kbits/sec    0   42.0 KBytes       
[  5]   4.00-5.00   sec  80.1 KBytes   656 Kbits/sec    0   55.1 KBytes       
[  5]   5.00-6.00   sec   139 KBytes  1.14 Mbits/sec    0   82.7 KBytes       
[  5]   6.00-7.00   sec   189 KBytes  1.55 Mbits/sec    0    116 KBytes       
[  5]   7.00-8.00   sec  0.00 Bytes  0.00 bits/sec    0    148 KBytes       
[  5]   8.00-9.00   sec   189 KBytes  1.55 Mbits/sec    0    196 KBytes       
[  5]   9.00-10.00  sec   252 KBytes  2.06 Mbits/sec    0    240 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  1.13 MBytes   948 Kbits/sec    0             sender
[  5]   0.00-13.70  sec   840 KBytes   502 Kbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 22:14:48
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 52786 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  2.09 MBytes  17.6 Mbits/sec    0    147 KBytes       
[  5]   1.00-2.00   sec  3.94 MBytes  33.0 Mbits/sec    0    335 KBytes       
[  5]   2.00-3.00   sec  6.46 MBytes  54.2 Mbits/sec    0    629 KBytes       
[  5]   3.00-4.00   sec  6.95 MBytes  58.3 Mbits/sec    0    936 KBytes       
[  5]   4.00-5.00   sec  8.51 MBytes  71.4 Mbits/sec    0   1.29 MBytes       
[  5]   5.00-6.00   sec  8.75 MBytes  73.4 Mbits/sec    0   1.74 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.22 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.74 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec  398   1.38 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.47 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  77.9 MBytes  65.4 Mbits/sec  398             sender
[  5]   0.00-10.19  sec  76.2 MBytes  62.7 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-07 23:14:59
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 44356 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  10.9 MBytes  91.7 Mbits/sec    0    553 KBytes       
[  5]   1.00-2.00   sec  10.8 MBytes  90.8 Mbits/sec    0   1.05 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.2 Mbits/sec    0   1.58 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.10 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.63 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec  146   1.36 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.45 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.52 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.57 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.61 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  89.5 Mbits/sec  146             sender
[  5]   0.00-10.20  sec   105 MBytes  86.5 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-08 00:15:10
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 33386 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.2 MBytes   102 Mbits/sec    0    778 KBytes       
[  5]   1.00-2.00   sec  11.3 MBytes  94.4 Mbits/sec    0   1.29 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.81 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.34 MBytes       
[  5]   4.00-5.00   sec  8.75 MBytes  73.4 Mbits/sec   89   1.93 MBytes       
[  5]   5.00-6.00   sec  12.5 MBytes   105 Mbits/sec  696   1.40 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.49 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.54 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.59 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.62 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  91.0 Mbits/sec  785             sender
[  5]   0.00-10.20  sec   107 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-08 01:15:21
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 44928 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  10.6 MBytes  88.5 Mbits/sec    0    717 KBytes       
[  5]   1.00-2.00   sec  11.0 MBytes  92.0 Mbits/sec    0   1.14 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.67 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.20 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.72 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec  610   1.38 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.47 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.53 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.58 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.61 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   105 MBytes  88.3 Mbits/sec  610             sender
[  5]   0.00-10.20  sec   104 MBytes  85.3 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-08 02:15:32
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 34274 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.1 MBytes   101 Mbits/sec    0    663 KBytes       
[  5]   1.00-2.00   sec  11.3 MBytes  94.6 Mbits/sec    0   1.17 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.70 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.23 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.76 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec  404   1.39 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.47 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.54 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.58 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.61 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.9 Mbits/sec  404             sender
[  5]   0.00-10.20  sec   106 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-08 03:15:42
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 46490 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  8.87 MBytes  74.4 Mbits/sec    0    427 KBytes       
[  5]   1.00-2.00   sec  12.4 MBytes   104 Mbits/sec    0    971 KBytes       
[  5]   2.00-3.00   sec  11.1 MBytes  93.5 Mbits/sec    0   1.48 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.00 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.53 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec  487   1.34 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.43 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.50 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.55 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.59 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   106 MBytes  89.1 Mbits/sec  487             sender
[  5]   0.00-10.20  sec   104 MBytes  85.8 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-08 04:15:53
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 47608 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.5 MBytes  96.4 Mbits/sec    0    757 KBytes       
[  5]   1.00-2.00   sec  12.1 MBytes   101 Mbits/sec    0   1.27 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.79 MBytes       
[  5]   3.00-4.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.32 MBytes       
[  5]   4.00-5.00   sec  8.75 MBytes  73.4 Mbits/sec   75   1.93 MBytes       
[  5]   5.00-6.00   sec  12.5 MBytes   105 Mbits/sec  164   1.40 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.48 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.54 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.59 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.62 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   107 MBytes  90.0 Mbits/sec  239             sender
[  5]   0.00-10.20  sec   106 MBytes  87.4 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-08 05:16:04
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 56030 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  12.0 MBytes   100 Mbits/sec    0    773 KBytes       
[  5]   1.00-2.00   sec  12.4 MBytes   104 Mbits/sec    0   1.28 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.81 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.33 MBytes       
[  5]   4.00-5.00   sec  8.75 MBytes  73.4 Mbits/sec   91   1.92 MBytes       
[  5]   5.00-6.00   sec  12.5 MBytes   105 Mbits/sec  582   1.40 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.48 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.54 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.58 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.61 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.7 Mbits/sec  673             sender
[  5]   0.00-10.20  sec   107 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-08 06:16:15
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 50836 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.9 MBytes  99.5 Mbits/sec    0    776 KBytes       
[  5]   1.00-2.00   sec  12.4 MBytes   104 Mbits/sec    0   1.28 MBytes       
[  5]   2.00-3.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.81 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.34 MBytes       
[  5]   4.00-5.00   sec  8.75 MBytes  73.4 Mbits/sec   92   1.93 MBytes       
[  5]   5.00-6.00   sec  12.5 MBytes   105 Mbits/sec  314   1.41 MBytes       
[  5]   6.00-7.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.49 MBytes       
[  5]   7.00-8.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.54 MBytes       
[  5]   8.00-9.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.59 MBytes       
[  5]   9.00-10.00  sec  10.0 MBytes  83.9 Mbits/sec    0   1.61 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.6 Mbits/sec  406             sender
[  5]   0.00-10.20  sec   107 MBytes  87.6 Mbits/sec                  receiver

iperf Done.

========================================
Timestamp: 2024-08-08 07:16:26
Connecting to host 10.0.8.235, port 5201
[  5] local 10.0.8.230 port 37116 connected to 10.0.8.235 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  11.7 MBytes  98.0 Mbits/sec    0    652 KBytes       
[  5]   1.00-2.00   sec  11.3 MBytes  94.6 Mbits/sec    0   1.16 MBytes       
[  5]   2.00-3.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.69 MBytes       
[  5]   3.00-4.00   sec  10.0 MBytes  83.9 Mbits/sec    0   2.22 MBytes       
[  5]   4.00-5.00   sec  11.2 MBytes  94.4 Mbits/sec    0   2.75 MBytes       
[  5]   5.00-6.00   sec  10.0 MBytes  83.9 Mbits/sec  500   1.38 MBytes       
[  5]   6.00-7.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.47 MBytes       
[  5]   7.00-8.00   sec  11.2 MBytes  94.4 Mbits/sec    0   1.53 MBytes       
[  5]   8.00-9.00   sec  10.0 MBytes  83.9 Mbits/sec    0   1.58 MBytes       
[  5]   9.00-10.00  sec  11.2 MBytes  94.4 Mbits/sec    0   1.61 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec   108 MBytes  90.6 Mbits/sec  500             sender
[  5]   0.00-10.20  sec   106 MBytes  87.3 Mbits/sec                  receiver

iperf Done.

========================================
'''
        
        # Process data and create chart
        timestamps, speeds = parse_data(file_content)
        
        if not timestamps or not speeds:
            print("No data found!")
            return
            
        print(f"Found {len(timestamps)} data points")
        
        # Create and save chart
        chart = create_chart(timestamps, speeds)
        output_path = "network_speed_chart.html"
        output_file(output_path)
        show(chart)
        
        # Open the chart in browser
        abs_path = os.path.abspath(output_path)
        print(f"Chart saved to: {abs_path}")
        webbrowser.open('file://' + abs_path)
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()