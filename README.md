# Flask Reveal

[flask-reveal](https://github.com/humrochagf/flask-reveal) is a cool way to setup your [reveal.js](https://github.com/hakimel/reveal.js) presentations without the need to edit a monolithic html file and using markdown syntax mixed with some html tags.

## Requirements

 - Python 3
 - Flask
 - reveal.js
 - docopt

## Usage

On the first use, you need to setup the reveal.js files with the project. To make that, just run the following command:

```
python run.py installreveal (-f | --file FILE)
```

Where the `FILE` can be either the **.tar.gz** or the **.zip** release file found at the [reveal.js releases](https://github.com/hakimel/reveal.js/releases).

To start your presentation run:

```
python run.py start [-d | –debug] [-p | –path PATH]
```

Running without the `PATH` information, it will do the presentation files lookup inside the current directory.

## Presentation Setup

The flask-reveal checks for three things on your presentation folder.

### The '.md' Files

These are your presentation files written using markdown with some especial tags described on [markdown section](#markdown) and are placed on your presentation root folder.

The file loading is done by alphabetical order, so make sure they are ordered.

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
**REVEAL_CONFIG**: python dictionary with the [reveal.js configuration attributes](https://github.com/hakimel/reveal.js/#configuration) but using python types (e.g.: true is python boolean True)

```python
REVEAL_CONFIG = {
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
    'loop': True,

    # Change the presentation direction to be RTL
    'rtl': False,

    # Turns fragments on and off globally
    'fragments': True,

    # Flags if the presentation is running in an embedded mode,
    # i.e. contained within a limited portion of the screen
    'embedded': False,

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

    # Slide theme
    'theme': 'default',  # default/beige/blood/moon/night/serif/simple/sky/solarized

    # Transition style
    'transition': 'default',  # default/cube/page/concave/zoom/linear/fade/none

    # Transition speed
    'transitionSpeed': 'default',  # default/fast/slow

    # Transition style for full page slide backgrounds
    'backgroundTransition': 'default',  # default/none/slide/concave/convex/zoom

    # Number of slides away from the current that are visible
    'viewDistance': 3,

    # Parallax background image
    'parallaxBackgroundImage': '',  # e.g. "'https://s3.amazonaws.com/hakim-static/reveal-js/reveal-parallax-1.jpg'"

    # Parallax background size
    'parallaxBackgroundSize': '',  # CSS syntax, e.g. "2100px 900px"
}
```

### The 'img' folder

All images used on your presentation are placed inside the **'img'** folder and referenced on your slides starting from your presentation root.

```markdown
![Python Logo](img/python.png)
```

## Markdown

The markdown used on the presentation files support most of the [GitHub Markdown](https://help.github.com/articles/markdown-basics) and adds some especial html comment tags to edit styles and control effects that are explained on the [reveal.js markdown docs](https://github.com/hakimel/reveal.js/#markdown).

**Important:** You can use all html tags on the presentation files, but some block tags can present unexpected behavior.
