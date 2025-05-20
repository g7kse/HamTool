# HamTool
[52 ham challenge](https://hamchallenge.org/) has some interesting challenges to do. One a week. this one is going to be hard for me as I don't really do coding. I just pinch what someone else has done (thanks to all the clever coders I have an illusion of competence - i.e. I can follow instructions reasonably well)

So what I wanted is......A command line "Menu" that starts up commonly used stuff and does little odds and sods. this is a work in progress and so some stuff sort of works and other things will be made to work or removed if I can't do it for whatever reason. It works in Ubuntu Terminal application, so should work in another distro. its all in python after all. very little of this is my own work. I am attmpting to collect it all together to make a thing that works for me. If it works for you then thats ace. A kind of working screen looks like this

![hamtool](https://github.com/user-attachments/assets/07078bea-540c-42ba-b243-ab228e011bfc)


## What is it?
The command line is a really handy tool that avoids the complicty of a GUI. The main part of this is a menu system that allows a user to select a "thing" to be done. For example set the time on an IC7300 which has a knackered battery and I can't be bothered to fix the hardware because it is a bit of a hack and perhaps software could help out. So some things I'm looking to do...

- [x] Set up the basic menu
- [x] Add in [Ian Rentons POTA nearby script](https://github.com/ianrenton/pota-local-progress/tree/main)
- [x] Set the time on the IC7300 (A slightly modded version of [loughkb's](https://github.com/loughkb/IC-7300-time-sync) script)
- [x] CWOps CWT lookup table that checks callsign with membership number from a CSV list...this needed a bit of mucking about with as the CSV isn't "clean"
- [ ] Morse code decoder - felly struggling with audio stream but its basivcally trying to port the Arduino code from [OZ1HJM](http://www.oz1jhm.dk/content/very-simpel-cw-decoder-easy-build)
- [ ] SOTA alerts and spots - needs a lot of work to re-do and make it work and look like the POTA script. Its G4VFL's old one after all
- [ ] Band conditions. Hmm in need of work
- [ ] Start Hamlib and show frequency and mode...not even started

## What state is it in?
Definiately not finished. I'd have this as barely started. Some of this stuff is a mess.

## Want to help?
I'll need it btw, so please do. But don't just change something. Explain the method so I can learn. I learn by doing rather than reading then applying. Its the mech eng in me.

## What needs to be done?
In order of preference:
1. Look at the scripts that currently work and see if they are 'done correctly' - If there is poor practice or efficiences then let me know
2. How should this be 'packaged'? Ideally this should be a application like any other, just double click to start. I haven't quite got my head round how to do that in linux
3. Help with some of the other scripts

## What doesn't need to be done?
Please don't treat this as a never ending piece of development work. Its supposed to be a short exercise to help in a simple way. Lets not turn it into a monster.
