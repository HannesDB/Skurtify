<!DOCTYPE html>
<html>
  <head>
    <title>Skurtify</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="static/style.css" type="text/css"></link>
    <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">
  </head>

  <body>
    <header>
      <h1>Skurtify</h1>
    </header>
    <div>
      <p>Top 20 result:
        %for i, t, a in zip(ids, tracks, art):
          <p>
            {{i}}. {{t}}. {{a}}
          </p>
        %end
      </p>
    </div>
  </body>
</html>