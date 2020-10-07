Title: Django market
Category: Projects
Date: 2009-06-01
Status: draft
Summary: django-market is a e-marketplace where multiple sellers can be offering the same product

My first big project. The lofty idea was to have an eshop as a stand on a bazaar. The customer can visit
multiple shops selling the same thing and compare prices and other variants. Therefore I called the app
django-market in the end. The original name was "the national shopping gallery" because the main article
was the origin of all goods. All goods had to be manufactured locally. This was a good selling point back
then and it would work today as well I think. 

The app itself is extremely complicated - imagine an app that has been in development for several years 
without ever being shown to public. Funny fact: when I let it go, the guy who took my domain did exact
oposite - he launched a very simple site backed by AirTable, Google Form and a custom frontend and it
worked perfectly at beginning. Now it would use some updates to get more traction. Unfortunately the 
guy is not responding to any of my messages.

I learnt having dependencies always in the right direction not to introduce cycles. I learnt to have
high cohesion and low coupling in order to fight those cyclic dependencies. I started by modifying other
django project [django-shop](https://github.com/awesto/django-shop) - a popular project back then. 
I tried to keep my stuff as an extensionbut after few painful months I have decided to split from the 
project and rewrite some fundamental parts. Especially model inherictance was a real pain in django
due to its magic with meta programming.

The project consists of multiple parts which I will describe in greater details

## Core module

Contains essential classes like `customer, seller, shop, category, manufacturer, product`, and `offer`.
You can see that product and (price)offer are divided. That is because a product exist only once
and all shops are simply putting up their price offers. A customer can then see what shops have what
prices and decide based on that.

## Checkout

Module containing the logic for placing an `order`, issuing an `invoice` and handle `shipping` and `payment`.
I think I overdid the complexity of this module so it took me a long time to life it of the ground.

## Tariff

This module is the one why I never published my work. This module was there for monetizing the application.
It enforced tarrifs on sellers based on how many products they offered. It uses signals, statistics and even
has the possibility to issue promo codes.

Project repository https://github.com/katomaso/django-market