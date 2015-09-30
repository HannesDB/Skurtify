<!DOCTYPE html>
<html>
  <head>
    <title>Skurtify</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="static/style.css" type="text/css"></link>
    <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
    <script type="text/javascript" src="static/script.js"></script>
  </head>

  <body>
    <h1>Skurtify</h1>
      <table>
        <tr>
          <td id="list">
            <ul id="unicorns">
            </ul>
          </td>
          <td id="info">
            <h2 id="unicornName">Ingen enhörning</h2>
            <span id="unicornImage"></span>
            <p id="unicornInfo"></p>
            <p id="unicornSighting"></p>
            <button type="button" id="addUnicorn">Lägg till enhörning</button>
            <button type="button" id="updateUnicorn">Uppdatera enhörning</button>
            <button type="button" id="deleteUnicorn">Ta bort enhörning</button>

            <form name="existingUnicorn" id="existingUnicorn">
              <input type="hidden" name="id">
              <label for="name">Enhörningens namn</label>
              <input type="text" name="name"><br>
              <label for="reportedBy">Vem såg den?</label>
              <input type="text" name="reportedBy"><br>
              <label for="spottedWhere.name">Var sågs den?</label>
              <input type="text" name="spottedWhere.name"><br>
              <label for="spottedWhere.lat">Latitud</label>
              <input type="text" name="spottedWhere.lat"><br>
              <label for="spottedWhere.lon">Longitud</label>
              <input type="text" name="spottedWhere.lon"><br>
              <label for="spottedWhen">När sågs den?</label>
              <input type="text" name="spottedWhen" class="date"><br>
              <label for="image">Bild</label>
              <input type="text" name="image"><br>
              <label for="description">Beskrivning</label>
              <textarea name="description"></textarea><br>
              <button type="button" id="putUnicorn">Skicka</button>
            </form>

            <form name="newUnicorn" id="newUnicorn">
              <input type="hidden" name="id">
              <label for="name">Enhörningens namn</label>
              <input type="text" name="name"><br>
              <label for="reportedBy">Vem såg den?</label>
              <input type="text" name="reportedBy"><br>
              <label for="spottedWhere.name">Var sågs den?</label>
              <input type="text" name="spottedWhere.name"><br>
              <label for="spottedWhere.lat">Latitud</label>
              <input type="text" name="spottedWhere.lat"><br>
              <label for="spottedWhere.lon">Longitud</label>
              <input type="text" name="spottedWhere.lon"><br>
              <label for="spottedWhen">När sågs den?</label>
              <input type="text" name="spottedWhen" class="date"><br>
              <label for="image">Bild</label>
              <input type="text" name="image"><br>
              <label for="description">Beskrivning</label>
              <textarea name="description"></textarea><br>
              <button type="button" id="postUnicorn">Skicka</button>
            </form>
          </td>
        </tr>
      </table>
  </body>
</html>