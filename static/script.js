    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
    <script type="text/javascript" src="static/script.js"></script>

function postUnicorn() {
  return function() {
    var data = {};
    data.name = $('#newUnicorn input[name=name]').val();
    data.description = $('#newUnicorn textarea[name=description]').val();
    data.reportedBy = $('#newUnicorn input[name=reportedBy]').val();
    data.spottedWhere = {};
    data.spottedWhere.name = $('#newUnicorn input[name="spottedWhere.name"]').val();
    data.spottedWhere.lat = $('#newUnicorn input[name="spottedWhere.lat"]').val();
    data.spottedWhere.lon = $('#newUnicorn input[name="spottedWhere.lon"]').val();
    data.spottedWhen = $('#existingUnicorn input[name=spottedWhen]').val();
    if (data.spottedWhen.length == 10) {
      data.spottedWhen += ' 00:00:00';
    }
    data.image = $('#newUnicorn input[name=image]').val();
    
    $.ajax({
      method: "POST",
      url: 'http://unicorns.idioti.se',
      data: JSON.stringify(data),
      headers: {"Accept": "application/json"}
    })
    .done(function(result) {
    });
  }
}

function putUnicorn(unicorn) {
   return function() {
     var data = {};
     data.id = $('#existingUnicorn input[name=id]').val(); 
     data.name = $('#existingUnicorn input[name=name]').val();
     data.description = $('#existingUnicorn textarea[name=description]').val();
     data.reportedBy = $('#existingUnicorn input[name=reportedBy]').val();
     data.spottedWhere = {};
     data.spottedWhere.name = $('#existingUnicorn input[name="spottedWhere.name"]').val();
     data.spottedWhere.lat = $('#existingUnicorn input[name="spottedWhere.lat"]').val();
     data.spottedWhere.lon = $('#existingUnicorn input[name="spottedWhere.lon"]').val();
     data.spottedWhen = $('#existingUnicorn input[name=spottedWhen]').val();
     if (data.spottedWhen.length == 10) {
       data.spottedWhen += ' 00:00:00';
     }
     data.image = $('#existingUnicorn input[name=image]').val();
     
     $.ajax({
       method: "PUT",
       url: 'http://unicorns.idioti.se/' + data.id,
       data: JSON.stringify(data),
       headers: {"Accept": "application/json"}
     })
     .done(function(result) {
     });
   }
}

/*
 * Det här är en väldigt enkel funktion att implementera. Delete-anrop kräver
 * inget mer än en URL till resursen som ska tas bort. Den bygger vi snabbt
 * ihop på samma sätt som i PUT.
 */
function deleteUnicorn(unicorn) {
  return function() {
    $.ajax({
      method: "DELETE",
      url: 'http://unicorns.idioti.se/' + unicorn
    });
  }
}

function fetchAndUpdateInfo(details) {
  return function() {
    $.ajax({
      url: details,
      headers: {"Accept": "application/json"}
    })
    .done(function (data) {
      date = new Date(data['spottedWhen'].date);
      sighting = 'Av: ' + data['reportedBy'] + ', '
               + date.toLocaleDateString()
               + ' i ' + data['spottedWhere']['name'];
      
      $('#unicornName').text(data['name']);
      $('#unicornImage').html('<img src="' + data['image'] + '">');
      $('#unicornInfo').text(data['description']);
      $('#unicornSighting').text(sighting);

      $('form').hide();
      
      $('#existingUnicorn input[name=id]').val(data['id']);
      $('#existingUnicorn input[name=name]').val(data['name']);
      $('#existingUnicorn input[name=reportedBy]').val(data['reportedBy']);
      $('#existingUnicorn input[name="spottedWhere.name"]').val(data['spottedWhere']['name']);
      $('#existingUnicorn input[name="spottedWhere.lat"]').val(data['spottedWhere']['lat']);
      $('#existingUnicorn input[name="spottedWhere.lon"]').val(data['spottedWhere']['lon']);
      $('#existingUnicorn input[name=spottedWhen]').val(date.toLocaleString());
      $('#existingUnicorn input[name=image]').val(data['image']);
      $('#existingUnicorn [name=description]').val(data['description']);
      
      $('#addUnicorn').unbind('click');
      $('#updateUnicorn').unbind('click');
      $('#deleteUnicorn').unbind('click');
      
      $('#addUnicorn').click(hideFormsAndShowOne('#newUnicorn'));
      $('#updateUnicorn').click(hideFormsAndShowOne('#existingUnicorn'));
      $('#deleteUnicorn').click(deleteUnicorn(data['id']));
    });
  }
}

function hideFormsAndShowOne(formName) {
  return function () {
    $('form').hide();
    $(formName).show();
  }
}

$(document).ready(function () {
  $.ajax({
    url: 'http://unicorns.idioti.se',
    headers: {"Accept": "application/json"}
  })
  .done(function (data) { 
    list = $('#unicorns');
    
    for (i = 0; i < data.length; i++) {
      html = '<li id="unicorn_' + i + '">' + data[i]['name'] + '</li>';
      list.append(html);
      $('#unicorn_' + i).click(fetchAndUpdateInfo(data[i]['details']));
    }
  });
  
  $(".date").datepicker({ dateFormat: "yy-mm-dd" });
  $('form').hide();
  $('#postUnicorn').click(postUnicorn());
  $('#putUnicorn').click(putUnicorn());
});