import glob


def load_markdown_slides():
    """
    Search the slide pages in the current directory, loading them in
    alphabetical order as a list of strings.

    The slide pages must be on markdown format having ".md" extension
    """

    slides = []

    for file in glob.glob('*.md'):
        with open(file, 'r') as sb:
            slides.append(sb.read())

    return slides