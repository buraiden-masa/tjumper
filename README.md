# tjumper
Advances or return the your system clock for any number of seconds

# How to use
This script was made fot python2.75.
You can change the system clock by specifying any number of seconds in the -t option.
<pre>
NOTE: If you specify a negative value (e.g. -600), the time will be returned. 
</pre>

For example:
```
# python tjumper.py -t 10
Correct 10 second.......
current   time = 2018-01-17 18:08:30.121068
converted time = 2018-01-17 18:08:40.121068
```

See also the help page that displayed by -h option:
```
# python tjumper.py -h
usage: Correct the system clock arbitray number of seconds

description

optional arguments:
  -h, --help            show this help message and exit
  -t TIME, --time TIME  specify the number of seconds you wanna advance/rewind
  -d, --date            show current system clock

[EOF]
```

# License
This software is released under the MIT License.
