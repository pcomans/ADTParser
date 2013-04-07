ADTParser
=========

A very simple solution for parsing the article of the day on the German Wikipedia.

It expects that you create a subpage of your Wikipedia user page and add the following template:

    {{Wikipedia:Hauptseite/Artikel des Tages/{{LOCALDAYNAME}}}}

Prerequisites

    sudo pip install lxml
    sudo pip install pil
