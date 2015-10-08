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
      <form action="/search/" method="POST">
        <input required type="text" name="search" placeholder="Search">
        <input type="submit" name="send" value="Search">
      </form>
    </div>
  </body>
</html>