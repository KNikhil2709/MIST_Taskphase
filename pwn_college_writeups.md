#Split-piping stderr and stdout
pwn.college{ctvlVK2qhFU2q-r2jQ5MVupE73w.dFDNwYDL1gTN0czW}

We need to send stdout to '/challenge/planet' and stderr to '/challenge/the'

~$ /challenge/hack | tee>(/challenge/planet) 2>&1 /challenge/the
Error-
ssh-entrypoint: tee/dev/fd/63: No such file or directory
Are you sure you're properly redirecting /challenge/hack's standard output into '/challenge/planet'?
You must redirect my standard error into '/challenge/the'!
~$ /challenge/hack | tee>(/challenge/planet) | 2>&1 /challenge/the
Error- 
ssh-entrypoint: tee/dev/fd/63: No such file or directory
Are you sure you're properly redirecting /challenge/hack's standard output into '/challenge/planet'?
You must redirect my standard error into '/challenge/the'!
Are you sure you're properly redirecting /challenge/hack's standard error into '/challenge/the'?
~$ /challenge/hack | ( /challenge/planet ) 2> >( /challenge/the )
Error- 
You must redirect my standard error into '/challenge/the'!
You are redirecting standard error *of /challenge/planet*! Instead, you must redirect standard error of 'hack'.
This must be done *before* any |. The right side of the pipe is a different command, with its own redirection, than the left side!
Are you sure you're properly redirecting /challenge/hack's standard error into '/challenge/the'?
Judging by the above error messages, one correction we need to make is that the standard error or 'hack' must be redirected before using | or | must not be used at all.
This is probably because using | mixes the stdout and stderr.
Lets try using a command without |
For example-

~$ echo hi | rev
ih
~$ echo hi > >(rev)
ih

The first and second programs are the same, hence lets try using the second method.









#Multiple globs
pwn.college{cB5wDK9uFDKHbUPlrEyLFBZi_9W.QXycTO2EDL1gTN0czW}
:/challenge/files$ /challenge/run *p*
Running the above statement in /challenge/files will give us the flag as p covers every word that has the letter p.






#Bashrc Backdoor
pwn.college{UOrjR33aimjURmvTX8HO0oRLMKj.QXxMTM3EDL1gTN0czW}

the .bashrc file serves as the startup script.
In this challenge we can add a line to the .bashrc script which cats the flag file and gives us the flag when the victim logs on.

~$ echo "cat /flag" >> /home/zardus/.bashrc
~$ /challenge/victim
Username: zardus
Password: **********
pwn.college{UOrjR33aimjURmvTX8HO0oRLMKj.QXxMTM3EDL1gTN0czW}
zardus@shenanigans~bashrc-backdoor:~$ exit
logout
~$ /challenge/hack > >(/challenge/planet) 2> >(/challenge/the)
In this command, we are using > and 2> to split it into an stdout which goes into >(/challenge/planet) and an stderr which goes into >(/challenge/the)
This gives us the flag.
