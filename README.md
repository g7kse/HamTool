# HamTool
A command line "Menu" that starts up commonly used stuff and does little odds and sods. this is a work in progress and so some stuff sort of works and other things will be made to work or removed if I can't do it for whatever reason. It works in Ubuntu Terminal application, so should work in another distro. its all in python after all. very little of this is my own work. I am attmpting to collect it all together to make a thing that works for me. If it works for you then thats ace.

## What is it?
The command line is a really handy tool. the main part of this is a menu system that allows a user to select a "thing" to be done. For example set the time on an IC7300 which has a knackered battery and I can't be bothered to fix the hardware because it could be simpler to do this in software. So some things I'm looking to do...


- [x] Set up the basic menu
- [x] Add in [Ian Rentons POTA nearby script](https://github.com/ianrenton/pota-local-progress/tree/main)
- [x] Set the time on the IC7300 (A slightly modded version of [loughkb's](https://github.com/loughkb/IC-7300-time-sync) script)
- [x] CWOps CWT lookup table that checks callsign with membership number from a CSV list...this needed a bit of mucking about with as the CSV isn't "clean"
- [ ] start up hamlib and report freq and mode
- [ ] start up Not1MM and Winserial Keyer (might change this to something with a daemon)
- [ ] morse code decoder - felly struggling with audio stream but its basivcally trying to port the Arduino code from [OZ1HJM](http://www.oz1jhm.dk/content/very-simpel-cw-decoder-easy-build)
- [ ] SOTA alerts and spots - needs a lot of work to re-do and make it work and look like the POTA script. Its G4VFL's old one after all
- [ ] Band conditions. Hmm in need of work
- [ ] Satrt Hamlib...not even started

## What state is it in?
Definiately not finished. Probably not even half finished. Some of this stuff is a mess. but feel free to poke about

## Want to help?

Feel free, I'm only doing this for fun and my [52 ham challenge](https://hamchallenge.org/) "I've made a programme" badge / tick