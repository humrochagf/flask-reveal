# Flask Reveal

[![PyPI](https://img.shields.io/pypi/v/flask-reveal.svg)](https://pypi.org/project/flask-reveal/)
[![PyPI - License](https://img.shields.io/pypi/l/flask-reveal.svg)](https://pypi.org/project/flask-reveal/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask-reveal.svg)](https://pypi.org/project/flask-reveal/)
[![Build Status](https://travis-ci.org/humrochagf/flask-reveal.svg?branch=master)](https://travis-ci.org/humrochagf/flask-reveal)
[![Coverage Status](https://coveralls.io/repos/github/humrochagf/flask-reveal/badge.svg)](https://coveralls.io/github/humrochagf/flask-reveal)
[![Code Health](https://landscape.io/github/humrochagf/flask-reveal/master/landscape.svg?style=flat)](https://landscape.io/github/humrochagf/flask-reveal/master)

[flask-reveal](https://github.com/humrochagf/flask-reveal) is a cool way to setup your [reveal.js](https://github.com/hakimel/reveal.js) presentations without the need to edit a monolithic html file and using markdown syntax mixed with some html tags.

## Requirements

The current version of flask-reveal runs on python 3.x

- Flask
- reveal.js

## Installation

You can install it from the PyPI:

```shell
$ pip install flask-reveal
```

## Usage

### Running the Presentation

To start your presentation run:

```shell
$ flaskreveal start [-m=MEDIA | --media=MEDIA] [-d | --debug] PATH
```

The `PATH` is the path to the markdown presentation file.

The `MEDIA` value sets custom media folder. If not passed, sets to default **img\** folder inside the presentation folder.

### Creating a new Presentation

To create a new presentation run:

```shell
$ flaskreveal mkpresentation [NAME]
```

### Install/Update reveal.js files

If you need for some reason reinstall reveal.js files, just run the following command:

```shell
$ flaskreveal installreveal
```

It will download reveal.js from a default **url** and make the install. If you want to set the **url** by yourself:

```shell
$ flaskreveal installreveal -u URL
```

If you already have the reveal.js file:

```shell
$ flaskreveal installreveal -f FILE
```

Where the `FILE` can be either the **.tar.gz** or the **.zip** release file found at the [reveal.js releases](https://github.com/hakimel/reveal.js/releases).

### PDF Export

Presentations can be exported to PDF via a special print stylesheet. This feature will be described using [Google Chrome](https://google.com/chrome) or [Chromium](https://www.chromium.org/Home), but I got the same results using [Firefox](https://www.mozilla.org/en-US/firefox/new/).

1. Run the presentation with flask-reveal.
2. Open your brownser with the `print-pdf` as query string like : `localhost:5000/?print-pdf`.
3. Open the in-browser print dialog (CTRL+P or CMD+P).
4. Change the **Destination** setting to **Save as PDF**.
5. Change the **Layout** to **Landscape**.
6. Change the **Margins** to **None**.
7. Enable the **Background graphics** option.
8. Click **Save**.

Alternatively you can use the [decktape](https://github.com/astefanutti/decktape) project.

### Share your presentation using [Ngrok](https://ngrok.com/)

You can easily share your presentation using [Ngrok](https://ngrok.com/). Download it, and put the binary file at root. Then you can do :
```shell
$ ngrok http 5000
```
This assume `5000` is your localhost.
`ngrok` will create a secure tunnel to your localhost :

```shell
ngrok by @inconshreveable                                              (Ctrl+C to quit)

Tunnel Status                 online
Version                       2.0.19/2.1.1
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://323744c6.ngrok.io -> localhost:5000
Forwarding                    https://323744c6.ngrok.io -> localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

## Presentation Setup

The flask-reveal checks for three things on your presentation folder.

### The 'slides.md' File

This is your presentation file written using markdown with some especial tags described on [markdown section](#markdown) and is placed on your presentation root folder.

Split your slides by setting up a *slide separator* into **REVEAL_CONFIG**. Default separator is `---`.

### The 'img' folder

All images used on your presentation are placed inside the **'img'** folder and referenced on your slides starting from your presentation root.

```markdown
![Python Logo](img/python.png)
```

### The 'config.py' File

The configuration file are placed on the presentation root folder and is responsible to customize your presentation.

This file is optional and can the values above can be changed:

**REVEAL_META**: python dictionary with metadata from the presentation

```python
REVEAL_META = {
    # Title of the slide
    'title': 'The title',

    # Author in the metadata of the slide
    'author': 'Some Author',

    # Description in the metadata of the slide
    'description': 'Some description'
}
```

**REVEAL_THEME**: string with reveal theme of choice

```python
# Themes
# beige, black, blood, league, moon, night, serif, simple, sky,
# solarized, white
REVEAL_THEME = 'black'
```

**REVEAL_CONFIG**: python dictionary with the [reveal.js configuration attributes](https://github.com/hakimel/reveal.js/#configuration) but using python types (e.g.: true is python boolean True)

```python
REVEAL_CONFIG = {
    # Slide separator
    'slideSep': '---',

    # Display controls in the bottom right corner
    'controls': True,

    # Display a presentation progress bar
    'progress': True,

    # Display the page number of the current slide
    'slideNumber': False,

    # Push each slide change to the browser history
    'history': True,

    # Enable keyboard shortcuts for navigation
    'keyboard': True,

    # Enable the slide overview mode
    'overview': True,

    # Vertical centering of slides
    'center': True,

    # Enables touch navigation on devices with touch input
    'touch': True,

    # Loop the presentation
    'loop': False,

    # Change the presentation direction to be RTL
    'rtl': False,

    # Turns fragments on and off globally
    'fragments': True,

    # Flags if the presentation is running in an embedded mode,
    # i.e. contained within a limited portion of the screen
    'embedded': False,

    # Flags if we should show a help overlay when the questionmark
    # key is pressed
    'help': True,

    # Flags if speaker notes should be visible to all viewers
    'showNotes': False,

    # Number of milliseconds between automatically proceeding to the
    # next slide, disabled when set to 0, this value can be overwritten
    # by using a data-autoslide attribute on your slides
    'autoSlide': 0,

    # Stop auto-sliding after user input
    'autoSlideStoppable': True,

    # Enable slide navigation via mouse wheel
    'mouseWheel': False,

    # Hides the address bar on mobile devices
    'hideAddressBar': True,

    # Opens links in an iframe preview overlay
    'previewLinks': False,

    # Transition style
    # default/cube/page/concave/zoom/linear/fade/none
    'transition': 'default',

    # Transition speed
    'transitionSpeed': 'default',  # default/fast/slow

    # Transition style for full page slide backgrounds
    # default/none/slide/concave/convex/zoom
    'backgroundTransition': 'default',

    # Number of slides away from the current that are visible
    'viewDistance': 3,

    # Parallax background image
    # e.g.:
    # "'https://s3.amazonaws.com/hakim-static/reveal-js/reveal-parallax-1.jpg'"
    'parallaxBackgroundImage': '',

    # Parallax background size
    'parallaxBackgroundSize': '',  # CSS syntax, e.g. "2100px 900px"

    # Amount to move parallax background (horizontal and vertical)
    # on slide change
    # Number, e.g. 100
    'parallaxBackgroundHorizontal': '',
    'parallaxBackgroundVertical': '',
}
```

## Markdown

The markdown used on the presentation files support most of the [GitHub Markdown](https://help.github.com/articles/markdown-basics) and adds some especial html comment tags to edit styles and control effects that are explained on the [reveal.js markdown docs](https://github.com/hakimel/reveal.js/#markdown).

**Important:** You can use all html tags on the presentation files, but some block tags can present unexpected behavior.
