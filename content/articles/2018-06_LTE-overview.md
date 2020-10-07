Title: LTE overview
Summary: Technical overview of LTE technology with some abbreviations explained
Category: Articles
Date: 2018-06-24
Updated: 2018-06-28
Author: Tomas Peterka

Long Term Evolution was originally the name of the working group which have specified this standard.

LTE standard became part of 3GPP specification in 2008 as Release 8. That specification was being extended until 2013 with Release 13. LTE is known as the 4. generation network (4G).

From technical point of view, LTE works completely over IP. Gone are proprietary E1 links connecting BTS and (digital) switchboards. New IP switchboard is called IMS and it handles all types of traffic (voice, signaling, and data). Gone is also SS7 signalling protocol which was replaced by DIAMETER and SIP protocols.

Voice entry point MSC was replaced by MGW. Data entry point is SGW (controlled by MME) and the output element is PGW.

5G network was supposed to transport solely over optics but price drop of IP technologies allowed operators to re-use their existing structure. The only requirements for 5G networks are VoLTE (voice over LTE transport) and higher data throughput.

Signalling (control plane) is separated from the data (user plane). Signalling instruct user's device to accept incoming calls, messages, re-register to networks or to change network elements (handover). The signalling protocol within the CORE network is DIAMETER. Its interfaces are denoted as Rx, Ry, or Sx, Sy for LTE (and Gx, Gy for 3G networks). Signalling for voice session initiation remains well known protocol SIP.

Every device in LTE network is assigned an IP address which needs to remain constant when moving between cells (called eNB in LTE and BTS in GSM). IP address is assigned after Attach to MME via standard DHCP. Attach step resolves local network elements (mainly APN's IP) and register user device against HLS (main IMSI database). The session within MME is called PDP context. Authentication is part of DIAMETER protocol that takes care of "AAA" (authentication, authorization, accounting). IP is assigned by standard DHCP.

VoLTE is the true game-changer because it unifies the last outside-standing technology with IP transport. It is so dfferent that if a LTE device is signalled incomming GSM call the device quickly unregister from LTE and re-register to 2G network just to be able to accept such call.
