
london-bin-sniffer
==================

Mobile Device Detector inspired by London's Recycling Bin with Usertracking. In August 2013 there was a series of articles about Tracking Devices installed in Londons Recycling Bins. I wanted to know how easy it would be to discover WLAN Devices. It turned out it is extremely easy. There is nothing to to What im doing here. It has been done a hundret times before and anyone who has looked at the WiFi Protocolls knows about it. 

I want to build a showcase a average user can set up and run to show their Friends,Parents,Grandparents how easy it is to monitore a device with wlan enabled.

Requirements:
-------------
*  WiFi Card with drivers supported by the [aircrack-ng](http://www.aircrack-ng.org/) projekt.
*  aircrack-ng installed
*  Python 2.7
*  [scapy](http://www.secdev.org/projects/scapy/)
*  sqlite
*  [Flask](http://flask.pocoo.org/) 



Usage:
------

Step 1: Prepare Wlan card.

use airmon-ng from aircrack-ng to bring a wlan device into monitoring mode. If your sniffer device is wlan1 use:

    $ sudo airmon-ng start wlan1

This will create a mon0 device in moitoring mode. You can check with _iwconfig_ if everything was ok. You shhould have a mon0 in monitoring mode.

     mon0      IEEE 802.11abgn  Mode:Monitor  Tx-Power=15 dBm   
               Retry  long limit:7   RTS thr:off   Fragment thr:off
               Power Management:off

With this you can start your the Mobile device detector.

    sudo python sniff.py
    

*TODO* How to start the Webapp for Analysis



Why?
------

To show who easy it is to build a passive surveillance station.

*TODO* Costs for a Raspberry Pi Powered station



Which mobile devices will show up?
----------------------------------

*  All devices looking for an Accespoint
*  AP's anouncing themselves


What (evil) can be done with the recored data
-------

*  count phones around you
*  get an alert of phone is near your monitor
*  check if your neighbour is at home
*  check peoples moving patterns
*  survilance moving patterns ... triangulation??
*  market share of devices
*  ......


What are your Results?
------

*TODO*





