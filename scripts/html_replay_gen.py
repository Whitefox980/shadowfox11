def generate_html_replay(payload, url):
    html = f"""
    <html><body>
    <h3>Replay:</h3>
    <form action="{url}" method="GET">
        <input name="q" value='{payload}' />
        <input type="submit" />
    </form>
    </body></html>
    """
    with open("reports/replay_preview.html", "w") as f:
        f.write(html)
