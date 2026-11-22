"""Build the static site in ./site from ./site-src (and the demo app in ./demo).

  site/index.html          landing page (+ login, KO/EN)
  site/app/index.html      Holy Impact newcomer app (from demo/index.html + login session)
  site/console/index.html  platform admin console
Also writes an artifact-ready copy of the landing page to the session scratchpad.
"""
import base64, os, re

R = '/home/user/HOLYIMPACTNEWCOMER'
SCRATCH = '/tmp/claude-0/-home-user-HOLYIMPACTNEWCOMER/a7f6d155-3316-5ee5-8136-6347c17b778c/scratchpad/site'


def logo(p):
    t = open(p).read()
    vb = re.search(r'viewBox="([^"]+)"', t).group(1)
    body = re.search(r'</title>(.*)</svg>', t, re.S).group(1).replace('#111111', 'currentColor')
    return f'<svg viewBox="{vb}" role="img" aria-hidden="true">{body}</svg>'


LOGO_F = logo(R + '/brand/tendbyname/tendbyname-website-logo-black.svg')
LOGO_A = logo(R + '/brand/tendbyname/tendbyname-stacked-logo-black.svg')


def fill(s):
    return s.replace('{{LOGIN}}', open(R + '/site-src/login.html').read()).replace('{{LOGO_F}}', LOGO_F).replace('{{LOGO_A}}', LOGO_A)


def page(src, lang='ko', extra_head='', drop_artifact_meta=True):
    """Wrap an artifact-style page (title/meta/link/style first, then markup) in a full HTML document."""
    head_end = src.index('</style>') + len('</style>')
    head = src[:head_end]
    if drop_artifact_meta:
        head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
    return ('<!doctype html>\n<html lang="%s">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n%s%s\n</head>\n<body>\n%s\n</body>\n</html>\n'
            % (lang, extra_head, head, src[head_end:]))


# landing
body = fill(open(R + '/site-src/body.html').read())
os.makedirs(SCRATCH, exist_ok=True)
fav = 'data:image/svg+xml;base64,' + base64.b64encode(open(R + '/brand/tendbyname/tend-app-icon-final.svg').read().encode()).decode()
art = body.replace('<meta name="copyright"', f'<link rel="icon" href="{fav}">\n<meta name="copyright"', 1)
open(SCRATCH + '/tend-by-name.html', 'w').write(art)
open(R + '/site/index.html', 'w').write(page(body, extra_head='<link rel="icon" href="favicon.svg" type="image/svg+xml">\n'))

# app (newcomer demo + session)
demo = open(R + '/demo/index.html').read()
session = open(R + '/site-src/app-session.js').read()
demo = demo.rstrip()
assert demo.endswith('</script>')
demo = demo + '\n<script>\n' + session + '\n</script>\n'
os.makedirs(R + '/site/app', exist_ok=True)
open(R + '/site/app/index.html', 'w').write(page(demo, extra_head='<link rel="icon" href="../favicon.svg" type="image/svg+xml">\n'))

# console
con = fill(open(R + '/site-src/console.html').read())
os.makedirs(R + '/site/console', exist_ok=True)
open(R + '/site/console/index.html', 'w').write(page(con))
print('ok')
