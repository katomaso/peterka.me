Title: TOR made for connectivity? Meet Re6st!
Author: Tomáš Peterka
Date: 2018-02-10
Status: draft
Summary: Re6st (pronounced resist) is a network layer combining industry-grade encryption and university-grade routing protocol.

# Babeld

# OpenVPN

Bridge
controlled by brctl utility

TUN
MESH network

What is AD-HOC (wireless) network mode?

    config wifi-iface
        option device   radio0
        option network  wlan_24
        option mode     adhoc
        option ssid     mymesh
        option encryption none

    config wifi-iface
        option device   radio1
        option network  wlan_5
        option mode     adhoc
        option ssid     mymesh
        option encryption none

Example taken from https://wiki.openwrt.org/doc/uci/babeld

## Re6st