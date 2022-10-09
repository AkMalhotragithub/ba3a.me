def template(title = "Ba3a", link = "https://ba3a.me") -> str:
    """Generate an HTML redirect document from the given link and title."""

    beforeCSS = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="generator" content="Ba3a">
        <meta http-equiv="refresh" content="0; URL='{link}'" />
        <title>{title}</title>"""

    afterCSS = f"""</head>
    <body>
        <section class="forbidden">
        <h3>Hi</h3>
        <p>You are being redirected to {title}</p>
        <a href="{link}"><span>Stuck here? <i>Click Me.</i></span></a>
        </section>
        </body>
    </html>"""

    css = """

    <style type="text/css">
    <!--
    body {
        font-size: 50pt;
        padding: 10px;
        background-color: rgb(30, 33, 37);
        font-family: monospace;
        text-align: center;
        color: #ccc;
    }

    section p, span, .button {
        margin: 0;
        padding: 0;
        font-size: 15px;
        font-style: italic;
        font-weight: 300;
        line-height: 25px;
        color: #666666;
    }

    span {
        font-size: 10pt;
        color: white;
    }

    h3 {
        font-size: 35px;
        margin: 0;
        padding: 0;
    }
    .button {
        background-color: rgb(30, 33, 37); /* Green */
        border: 2px solid white;
        text-align: center;
        color: white;
        border-radius: 4px;
        padding: 2px 5px;
    }
        -->
        </style>
    
    """
    return beforeCSS + css + afterCSS