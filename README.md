ADTParser
=========

A very simple solution for parsing the article of the day on the German Wikipedia.

It expects that you create a subpage of your Wikipedia user page and add the following template:

    {{Wikipedia:Hauptseite/Artikel des Tages/{{LOCALDAYNAME}}}}

On Debian

    sudo apt-get install libjpeg-dev

On OS X

    brew install libjpeg

Python libraries

    sudo pip install lxml
    sudo pip install pil

Setup instructions on Raspbian

    sudo aptitude install build-essential
    sudo aptitude install libxml2-dev
    sudo aptitude install libxslt-dev
    sudo aptitude install python-dev
    sudo aptitude install python-setuptools
    sudo aptitude install python-imaging
    sudo easy_install pip
    sudo pip install lxml

Running pip install took a very long time on my machine. Don't get discouraged. Go get a coffee or something.
