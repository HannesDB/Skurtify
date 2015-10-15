<!DOCTYPE html>
<html>
  <head>
    <title>Skurtify</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="../static/style.css" type="text/css">
    <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">
  </head>

  <body>
    <header>
      <h1>Skurtify</h1>
    </header>
    <div id="bod">
      <p>{{text}}:
          <div id="bild">
            <img src="{{pic}}" alt="{{tracks}}" style="width: 100px; height: 100px;">
          </div>
          <div id="text">
            <p>{{tracks}}</p>
            <p><a href="{{url}}"><img src="{{url_pic}}" alt="Spotify" style="width: 30px; height: 30px;"></a>Spelades kl: {{time}}</p>
          </div>
      </p>
    </div>
  </body>
</html>