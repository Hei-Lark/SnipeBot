## The Assorted Aces Bot- SnipeBot

Originally made to keeps track of the Assorted Ace's snipes, keeping count of who shot who, who was shot, who shot, and whatever. Logistics
are saved as different files within the folder 'snipeCounts.' Code for each type of command are .py files inside of
the 'cogs' folder.

File CountedUp.json keeps the nested dictionaries of each member's member id, hit counts, and been_hit counts. The
TOTAL snipes are also in there. The LargeLogs.txt is a massive log file saving the information of each snipe in the
format: <sniper>, <target>, <datetime>. These logs will be kept until edited manually by someone with the permissions.

## The Commands

1. The snipe commands: /snipe @user
    Only 1 command in this, used in the snipe channel.
    It returns a message in the channel, increments the appropriate hits and been_hit counters, increments TOTAL
counter, and adds an entry to the LargeLogs.txt.

2. Fetch commands
    Fetches statistics from the log files.
    a. /fetchhits @user
        Returns the number of times @user has successfully sniped another member of the club.
    b. /fetchtakeouts @user
        Returns the number of times @user has been sniped by another member of the club.
    c. /fetchtarget @user
        Return the number of times the user has sniped @user

## Currently Work in Progress
administrative commands such as leaderboards and clearing the logs.