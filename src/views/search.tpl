<!DOCTYPE html>
<html>
  <head>
    <title>Skurtify</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="../static/style.css" type="text/css">
  </head>

  <body>
    <div id="bodydiv">
      <header id="head">
        <h1>Skurtify</h1>
      </header>
      <div id="bod">
        <p>{{text}}:
            <div id="bild">
              <img src="{{pic}}" alt="{{tracks}}" style="width: 100px; height: 100px;">
            </div>
            <div id="text">
              <p>{{tracks}}</p>
              <p><a href="{{url}}"><img src="{{url_pic}}" alt="Spotify" style="width: 30px; height: 30px;"></a>Starttid: {{time}}</p>
            </div>
        </p>
      </div>
    </div>
  </body>
</html>