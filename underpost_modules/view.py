

def render(pathData):
    return """
          <!DOCTYPE html>
            <html lang='""" + pathData["lang"] + """'>
              <head>

                  <meta charset='`+MainProcess.data.charset+`'>
                  <meta content=width=device-width,initial-scale=1.0 name=viewport>

                  <title>""" + pathData["title"] + """</title>

                  <meta name ='title' content='""" + pathData["title"] + """'>
                  <meta name ='description' content='""" + pathData["description"] + """'>

                  <script defer src='/init.js'></script>
                  <script defer src='/util.js'></script>
                  <script defer src='/vanilla.js'></script>
                  <script defer type='module' src='/views/""" + pathData["router"] + """'></script>
              </head>
              <body>
                  <render></render>
              </body>
          </html>

    """
