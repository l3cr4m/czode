var x = document.getElementsByClassName("search-hide");
var max = 20;

function booksearch(){
  var search = document.getElementById('search').value
  document.getElementById('results').innerHTML = ""

  console.log(search)

  $.ajax({
    url: "https://www.googleapis.com/books/v1/volumes?q=" + search + "&langRestrict=cs_cz&printType=books&maxResults=" + 20,
    dataType: "json",

    success: function(data){
      for(i=0; i<data.items.length; i++){
        results.innerHTML += "  <div class='product'> <a href=''> <img src=" + data.items[i].volumeInfo.imageLinks.thumbnail + " alt=''> <div class='product-title'> <h3>" + data.items[i].volumeInfo.title + "</h3> </div></a></div>"


      }
    },

    type: "GET"
  });
}

function booksearch20(){
  var search = document.getElementById('search').value
  console.log(search)

  $.ajax({
    url: "https://www.googleapis.com/books/v1/volumes?q=" + search + "&langRestrict=cs_cz&printType=books&maxResults=" + 20 + "&startIndex=" + max,
    dataType: "json",

    success: function(data){
      for(i=0; i<data.items.length; i++){
        results.innerHTML += "  <div class='product'> <a href=''> <img src=" + data.items[i].volumeInfo.imageLinks.thumbnail + " alt=''> <div class='product-title'> <h3>" + data.items[i].volumeInfo.title + "</h3> </div></a></div>"


      }
    },

    type: "GET"
  });
}

document.getElementById("button").onkeypress = function(event){
          if (event.keyCode == 13 || event.which == 13){
            booksearch();
            x[0].style.display = "flex";
            x[1].style.display = "flex";
            x[2].style.display = "flex";

          }
      };

document.getElementById("next").onclick = function(){
          max += 20;
          booksearch20();
      };
