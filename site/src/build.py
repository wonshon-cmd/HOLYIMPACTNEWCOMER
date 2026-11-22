import re,os
R='/home/user/HOLYIMPACTNEWCOMER'
def inner(p):
    t=open(p).read()
    vb=re.search(r'viewBox="([^"]+)"',t).group(1)
    body=re.search(r'</title>(.*)</svg>',t,re.S).group(1).replace('#111111','currentColor')
    return f'<svg viewBox="{vb}" role="img" aria-hidden="true">{body}</svg>'
b=open(R+'/site/src/body.html').read()
b=b.replace('{{LOGO_F}}',inner(R+'/brand/tendbyname/tendbyname-website-logo-black.svg')).replace('{{LOGO_A}}',inner(R+'/brand/tendbyname/tendbyname-stacked-logo-black.svg'))
icon=open(R+'/brand/tendbyname/tend-app-icon-final.svg').read()
import base64
fav='data:image/svg+xml;base64,'+base64.b64encode(icon.encode()).decode()
art=b.replace('<meta name="copyright"',f'<link rel="icon" href="{fav}">\n<meta name="copyright"')
os.makedirs('/tmp/claude-0/-home-user-HOLYIMPACTNEWCOMER/a7f6d155-3316-5ee5-8136-6347c17b778c/scratchpad/site',exist_ok=True)
open('/tmp/claude-0/-home-user-HOLYIMPACTNEWCOMER/a7f6d155-3316-5ee5-8136-6347c17b778c/scratchpad/site/tend-by-name.html','w').write(art)
full='<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
head_end=b.index('</style>')+len('</style>')
full+=art[:head_end].replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')+'\n</head>\n<body>\n'+art[head_end:]+'\n</body>\n</html>\n'
open(R+'/site/index.html','w').write(full)
print('ok')
