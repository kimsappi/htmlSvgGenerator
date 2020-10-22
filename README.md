![Example](foreignObject.svg "Example output")

The SVG above (if shown) was generated with:
```
python3 htmlSvgGenerator.py --html example.html --css example.css
```

# About
Generates fancy SVG images from HTML and CSS for embedding in your Markdown.

# Dependencies
* Python 3

# Options
```
-h, --help           show this help message and exit
--html file          filename of the input HTML file
--css file           filename of the input CSS file
-o file, --out file  desired filename of the output file
-x px, --width px    desired width of the image in pixels
-y px, --height px   desired height of the image in pixels
-v, --verbose        print details relating to file names
```

# Idea credit and further reading
@sindresorhus: https://github.com/sindresorhus/css-in-readme-like-wat
