# VTSTech-COVID19.py
 COVID-19 JHU.EDU CSSE Data Analytics by VTSTech (www.VTS-Tech.org) 

Hello,

My name is Nigel Todman, I'm a software developer from Canada. I've written a Python script to parse the JHU CSSE Data from GitHub and produce various stats and metrics. Perhaps this would be useful to yourself or your colleagues. I often found myself making these calculations by hand every day. And now I can produce these stats globally or nationally rather quickly. (or even automatically)

Screenshot: <img src="https://i.gyazo.com/3c45aeecd5009d7b774d5c8d594fba0a.png">

Data Source: https://github.com/CSSEGISandData/COVID-19

Quick Install:

<pre>
Microsoft Windows [Version 10.0.18362.719]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\VTSTech><b>git clone https://github.com/CSSEGISandData/COVID-19</b>
Cloning into 'COVID-19'...
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 14711 (delta 2), reused 2 (delta 0), pack-reused 14702
Receiving objects: 100% (14711/14711), 47.11 MiB | 7.81 MiB/s, done.
Resolving deltas: 100% (7056/7056), done.

C:\Users\VTSTech><b>cd COVID-19</b>

C:\Users\VTSTech\COVID-19><b>wget https://github.com/Veritas83/VTSTech-COVID19.py/raw/master/VTSTech-COVID19.py</b>
--2020-03-17 17:48:44--  https://github.com/Veritas83/VTSTech-COVID19.py/raw/master/VTSTech-COVID19.py
Resolving github.com (github.com)... 140.82.112.4
Connecting to github.com (github.com)|140.82.112.4|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://raw.githubusercontent.com/Veritas83/VTSTech-COVID19.py/master/VTSTech-COVID19.py [following]
--2020-03-17 17:48:45--  https://raw.githubusercontent.com/Veritas83/VTSTech-COVID19.py/master/VTSTech-COVID19.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.124.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.124.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 17993 (18K) [text/plain]
Saving to: 'VTSTech-COVID19.py'

VTSTech-COVID19.py           100%[============================================>]  17.57K  --.-KB/s    in 0.02s

2020-03-17 17:48:45 (804 KB/s) - 'VTSTech-COVID19.py' saved [17993/17993]

C:\Users\VTSTech\COVID-19><b>VTSTech-COVID19.py</b>
COVID-19 JHU.EDU CSSE Data Analytics
v0.47 Written by VTSTech (www.VTS-Tech.org)
Data Source: https://github.com/CSSEGISandData/COVID-19

Usage: VTSTech-COVID19.py -l
       VTSTech-COVID19.py -d 03-14-2020
       VTSTech-COVID19.py -a -dav

-v                   verbose mode
-l                   list daily reports available
-d MM-DD-YYYY        use this daily report
-a                   use all available reports
-c                   filter by this country (ISO 3166-1 Alpha-2)
-t                   calculate global total cases
-td                  calculate global total deaths
-gdr                 calculate global death rate (use with -c for national)
-dav                 calculate daily average new cases
-dad                 calculate daily average new deaths
-dnc                 calculate daily new cases
-dnd                 calculate daily new deaths
-dgf                 calculate daily growth factor
-drc                 calculate daily death rate change
-din                 find largest daily case increases

C:\Users\VTSTech\COVID-19></pre>

Regards,

Nigel Todman

Software Developer/Technical Consultant

VTSTech Veritas Technical Solutions
