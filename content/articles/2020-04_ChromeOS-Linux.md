Title: ChromeOS as a personal computer
Summary: I finally gathered enough courage to switch from OSX to ChromeOS and boy I like it!
Category: Articles
Date: 2020-04-20
Updated: 2020-07-25
Author: Tomas Peterka

I finally gathered enough courage to switch from OSX to ChromeOS. And boy I like it!

ChromeOS is just Gentoo with custom graphic interface and read-only system partition.
The only writable folder is your _Download_ folder. The only graphical application is
(surprise surprise) _Chrome Browser_. This is indeed an amazing unhackable computer
for your grandmother but would it do as a personal computer?

## First impressions

Chrome OS is great in terms of basic customization. I could very easily re-map keys as
I am used to from OSX (very important for me), change sounds so the system is quiet 
(important too) and wallpapers update from the Internet every day. Basically all you 
need from an UI.

Google copied from Apple (as many times before) controlling the UI with your keyboard and
mouse. Google (as many times before) brought it even closer to perfection. Not just it has
similar keys layout and shortcuts as OSX, it even has the same touchpad gestures and _en plus_
you can move between your opened tabs by swiping with three fingers horizontaly! I wish all others
operating systems (or just browsers) copied this because it is soooo comfy!

The real fun starts once you turn on _the developer mode_. This allows you to launch a console `ctrl+alt+t`
and will unlock `/usr/local` for writing. Now we are talking! This helps you to install
some basic utilities so you don't feel so powerless. But it still doesn't give you graphical
applications such as an editor. Sure you _should_ have your development environment installed
on some server but we are talking about _personal computer_, remember? You don't want each
of your key stroke to fly around the world. You want stuff locally. Welcome to Linux containers
running on ChromeOS.

## Linux containers

Linux containers are native component of ChromeOS since version 69-ish. The project is called Crostini
and, as the authors admit, is heavily inspired by Crouton. Support for linux containers gets better
with every major release increment. Version 72 stabilized container formats, version 74 brought backups,
and version 79 adds support for audio (playback and capture). At the time of writing, latest relase is 83.

Linux containers are deactivated by default so you need to turn them on in "Advanced Settings".
Running linux on your ChromeBook is literally [one switch away from you](https://support.google.com/chromebook/answer/9145439).

Linux container(s) are perfect fit to Chrome/OS phylosophy. Everything needs to be sandboxed
and as any other application running on ChromeOS, even Linux apps are sandboxed too.
However, you can communicate with the container sufficiently - you can transfer files
and IP connections.

### Networking with the container

You can access your linux container named "penguin" via its FQDN `penguin.linux.test`. 
If you try `ip a` you will see a TAP interface dedicated to VMs
```
17: vmtap0: <BROADCAST,MULTICAST,ALLMULTI,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 100.115.92.25/30 brd 100.115.92.27 scope global vmtap0
```
It is a bridge to the containers. Inside the container, however, you are in a different subnet
```
5: eth0@if6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    inet 100.115.92.205/28 brd 100.115.92.207 scope global eth0
```
Therefore access to the VMs is NATed. It still allows me to run a PostgreSQL and connect
to it from outside so big thumb up by me.

### Sharing files with the container

You can move files in and out. That's pretty much it. I tried to access files in ChromeOS
and work with them but it does not work 100% because of rights issues and some specific
SYS calls that are unavailable via this file-bridge.

If you want to for example update such external files with git or compile them with golang
you are out of luck. It is necessary to do that outside of shared folders.


### Accessing Wayland

This is the most exciting part! You can actually access Wayland's output! I am usure how
this magic is done but you can run graphical applications in the container and they display
like native in ChromeOS. There is no noticable latency, it really feels like native! I am
so impressed!

I was able install Sublime and re-map keybinding as I like them. A bit confusing when the keys
are a bit special but managed with a few restrictions. Now I can continue developing applications.


### Carry on with usual life

I am ready to try to launch my automatic tests. They use Firefox driver by default. Didn't have much
success with installing gecko-driver. Let's try to change to chrome driver then! Should be easy on 
ChromeOS, no? No.

> All ChromeOS test images shall have Chrome Driver binary installed in /usr/local/chromedriver/.
_(The Chromedriver team)[https://sites.google.com/a/chromium.org/chromedriver/getting-started/chromeos]_

Too bad I don't have the test image because there is no chromedriver folder in my /usr/local/. Crew does
not contain anything either. I tried to use the (provided binaries)[https://sites.google.com/a/chromium.org/chromedriver/home]
for linux x84 but got burnt - dependencies missing! I gave up at this point. Will go with Linux containers again.
Funnily enough, no Firefox driver can be found in repositories. But luckily a chrome-driver is there!

```
$ apt list chromium-driver
Listing... Done
chromium-driver/stable,stable,now 80.0.3987.162-1~deb10u1 amd64
```

Yay! Let's get rolling again. My chrome device is so slow that I can actually observe the tests being
executed. And here is one advantage of those Chrome devices - they always come with a touchscreen with
pricetag ranging from 200$ to ... well ... there never was an upper limit for price of any sort of goods.

