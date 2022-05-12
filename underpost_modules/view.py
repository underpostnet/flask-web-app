

def render(pathData, envData):
    return """
          <!DOCTYPE html>
            <html lang='""" + pathData["lang"] + """'>
              <head>

                  <meta charset='""" + envData["charset"] + """'>
                  <meta content=width=device-width,initial-scale=1.0 name=viewport>

                  <title>""" + pathData["title"] + """</title>

                  <meta name ='title' content='""" + pathData["title"] + """'>
                  <meta name ='description' content='""" + pathData["description"] + """'>

                  <script defer src='/static/init.js'></script>
                  <script defer src='/static/util.js'></script>
                  <script defer src='/static/vanilla.js'></script>
                  <script defer type='module' src='/static/""" + pathData["router"] + """'></script>
              </head>
              <body>
                  <render></render>
              </body>
          </html>

    """
