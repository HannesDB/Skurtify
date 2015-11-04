<!DOCTYPE html>
<html>
  <head>
    <title>Skurtify</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="../static/style.css" type="text/css">
    <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">
  </head>

  <body>
    <div id="bodydiv">
      <header id="head">
        <h1>Skurtify</h1>
      </header>
      <div id="bod">
        <p>Välj radiokanal</p>
        <form action="/search/" method="GET">
          <select name="channel">
            <option value="132">P1</option>
            <option value="163">P2</option>
            <option value="164">P3</option>
            <option value="220">P4</option>
          </select>
          <p>Tryck på knappen för att se vilken låt som spelas på radio just nu:</p>
          <input type="submit" name="send" value="Search">
        </form>
      </div>
    </div>
  </body>
</html>