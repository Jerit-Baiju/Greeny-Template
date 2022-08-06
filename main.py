from pyflit import Page

while True:
    if open('pages/test.html','r').read() != open('templates/out.html','r').read():
        main = Page('main')
        main.add_page('test.html')
        open('templates/out.html','w').write(open('pages/test.html','r').read())
        print("UPDATED")