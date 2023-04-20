CPU Load Generator
==================

This package allows to generate a fixed CPU load for a finite time period.
The script takes in input the desired CPU load, the duration of the experiment and
the CPU core or all cores on which the load has to be generated.

**Installation**
    
    pip install git+https://github.com/erathaowl/CPULoadGenerator.git

*Usage*
To generate 20% of load on core 0 for 20 seconds run:

    python -m cpu_load_generator -l 0.2 -d 20 -c 0

To generate 50% of load on all logical cores for 20 seconds run:

    python -m cpu_load_generator -l 0.5 -d 20 -c -1

Set duration = 0 or repeat = 0 in json profile to perform an infinite loop

There is an option to run CPU load based on profile file. An exemplary profile is under 
load_profiles/default_profile.json. In order to run generator based on a profile issue 
the following command:

    python -m cpu_load_generator -p <path_to_profile_json>

To use its features from your code:

```python
from cpu_load_generator import load_single_core, load_all_cores, from_profile

load_single_core(core_num=0, duration_s=20, target_load=0.4)  # generate load on single core (0)
load_all_cores(duration_s=30, target_load=0.2)  # generates load on all cores
from_profile(path_to_profile_json=r"c:\profiles\profile1.json")
```



