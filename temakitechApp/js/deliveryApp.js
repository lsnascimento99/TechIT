// var itemsJson;
// var itemsJsonCategoria;
var data;
var dataItems;
var categoryJson;



// function getCategorias() {

//   var xhr = new XMLHttpRequest();
//   var itemsJsonCategoria
//   xhr.onreadystatechange = function () {
//     var data;
//     if (xhr.readyState == 4) {
//       return itemsJsonCategoria = xhr;
//     }
//   }
//   xhr.open('GET', 'http://127.0.0.1:5000/categoria/list', true);
//   xhr.send(null);

// }

// function readyItems(items) {
//   var data;
//   var categorias = getCategorias();
//   if (!xhr.responseType || xhr.responseType === "text") {
//     data = xhr.responseText;


//     itemJson = JSON.parse(data);


//     for (var i = 0; i < itemJson.produtos.length; i++) {
//       var obj = itemJson.produtos[i];
//       var item = document.createElement("div");
//       var items = document.getElementsByClassName("items")[0];
//       var imgDiv = document.createElement("div");
//       var img = document.createElement("img");
//       var titulo = document.createElement("h3");
//       var desc = document.createElement("h5");
//       var priceButton = document.createElement("div");
//       var moeda = document.createElement("p");
//       var preco = document.createElement("p");
//       var buttonA = document.createElement("a");


//       item.classList.add("item");


//       // Adicionando a imagem ao item section principal
//       imgDiv.classList.add('img-main');
//       img.setAttribute("src", "img/teppan.jpg");
//       imgDiv.appendChild(img);
//       item.appendChild(imgDiv);


//       titulo.classList.add('title-produto');
//       titulo.innerHTML = obj.nome;
//       item.appendChild(titulo);

//       desc.classList.add('desc-produto');
//       desc.innerHTML = obj.detalhe
//       item.appendChild(desc);

//       priceButton.classList.add('bottom-produto');
//       moeda.classList.add('moeda');
//       moeda.innerHTML = "R$";
//       preco.classList.add('preco');
//       preco.innerHTML = obj.preco;
//       priceButton.appendChild(moeda);
//       priceButton.appendChild(preco);

//       buttonA.setAttribute('href', '#')
//       buttonA.className = "button-add fa-lg";
//       // buttonI.classList.add('fas fa-plus-circle');
//       // buttonA.appendChild(buttonI);
//       buttonA.innerHTML = '<i class="fas fa-plus-circle"></i>'
//       priceButton.appendChild(buttonA);
//       item.appendChild(priceButton);
//       items.appendChild(item);
//     }
//   } else if (xhr.responseType === "document") {
//     data = xhr.responseXML;
//   } else {
//     data = xhr.response;
//     return insertCards(data);
//   }
// }
// function getItemList(callback) {
//   var xhr = new XMLHttpRequest();
//   xhr.onreadystatechange = function () {
//     if (xhr.readyState == 4) {
//       itemsJson = readyItems(xhr);
//     }

//     xhr.open('GET', 'http://127.0.0.1:5000/produto/list', true);
//     xhr.send(null);
//   }
// }

// getItemList(data);
// if (data) {

// }

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

function getCategoryList(callback) {
  var xhr = new XMLHttpRequest();

  xhr.onreadystatechange = (e) => {
    if (xhr.readyState !== 4) {
      return;
    }

    if (xhr.status === 200) {
      callback(JSON.parse(xhr.responseText));
      categoryJson = JSON.parse(xhr.responseText)
    } else {
      console.warn('request_error');
    }
  };

  xhr.open('GET', 'http://127.0.0.1:5000/categoria/list');
  xhr.send();
}

function getItemList(callback) {
  var xhr = new XMLHttpRequest();

  xhr.onreadystatechange = (e) => {
    if (xhr.readyState !== 4) {
      return;
    }

    if (xhr.status === 200) {
      itemJson = JSON.parse(xhr.responseText);
      itemJson.produtos.sort(function(a,b){
        return a.idCategoria - b.idCategoria;
        }
    );
      for(var i = 0; i < categoryJson.Categorias.length; i++) {
        var items = document.getElementsByClassName("items")[0];
        var br = document.createElement('br');
        var objCategory = categoryJson.Categorias[i];
        var estacoes = document.createElement("div");
        estacoes.classList.add('estacoes')
        estacoes.innerHTML='<i class="fas fa-tag fa-lg"></i>'
        var estacao = document.createElement("h1");
        estacao.classList.add("estacao");
        estacao.innerHTML ="Estação "+objCategory.categoria;
        estacoes.appendChild(estacao);
        items.appendChild(estacoes);


        for (j = 0; j < itemJson.produtos.length; j++) {
          var objItem = itemJson.produtos[j];
          if (objCategory.id == objItem.idCategoria) {
          
            var item = document.createElement("div");
            item.grid
            var items = document.getElementsByClassName("items")[0];
            var imgDiv = document.createElement("div");
            var img = document.createElement("img");
            var titulo = document.createElement("h3");
            var desc = document.createElement("h5");
            var priceButton = document.createElement("div");
            var moeda = document.createElement("p");
            var preco = document.createElement("p");
            var buttonA = document.createElement("a");
    
    
            item.classList.add("item");
    
    
            // Adicionando a imagem ao item section principal
            imgDiv.classList.add('img-main');
            img.setAttribute("src", "img/"+objItem.img);
            imgDiv.appendChild(img);
            item.appendChild(imgDiv);
    
    
            titulo.classList.add('title-produto');
            titulo.innerHTML = objItem.nome;
            item.appendChild(titulo);
    
            desc.classList.add('desc-produto');
            desc.innerHTML = objItem.detalhe
            item.appendChild(desc);
    
            priceButton.classList.add('bottom-produto');
            moeda.classList.add('moeda');
            moeda.innerHTML = "R$";
            preco.classList.add('preco');
            preco.innerHTML = objItem.preco;
            priceButton.appendChild(moeda);
            priceButton.appendChild(preco);
    
            buttonA.setAttribute('href', '#')
            buttonA.className = "button-add fa-lg";
            // buttonI.classList.add('fas fa-plus-circle');
            // buttonA.appendChild(buttonI);
            buttonA.innerHTML = '<i class="fas fa-plus-circle"></i>'
            priceButton.appendChild(buttonA);
            item.appendChild(priceButton);
            items.appendChild(item);
          }
        }
      }


      
      // for (var i = 0; i < itemJson.produtos.length; i++) {
      //   var obj = itemJson.produtos[i];
      //   var item = document.createElement("div");
      //   var items = document.getElementsByClassName("items")[0];
      //   var imgDiv = document.createElement("div");
      //   var img = document.createElement("img");
      //   var titulo = document.createElement("h3");
      //   var desc = document.createElement("h5");
      //   var priceButton = document.createElement("div");
      //   var moeda = document.createElement("p");
      //   var preco = document.createElement("p");
      //   var buttonA = document.createElement("a");


      //   item.classList.add("item");


      //   // Adicionando a imagem ao item section principal
      //   imgDiv.classList.add('img-main');
      //   img.setAttribute("src", "img/teppan.jpg");
      //   imgDiv.appendChild(img);
      //   item.appendChild(imgDiv);


      //   titulo.classList.add('title-produto');
      //   titulo.innerHTML = obj.nome;
      //   item.appendChild(titulo);

      //   desc.classList.add('desc-produto');
      //   desc.innerHTML = obj.detalhe
      //   item.appendChild(desc);

      //   priceButton.classList.add('bottom-produto');
      //   moeda.classList.add('moeda');
      //   moeda.innerHTML = "R$";
      //   preco.classList.add('preco');
      //   preco.innerHTML = obj.preco;
      //   priceButton.appendChild(moeda);
      //   priceButton.appendChild(preco);

      //   buttonA.setAttribute('href', '#')
      //   buttonA.className = "button-add fa-lg";
      //   // buttonI.classList.add('fas fa-plus-circle');
      //   // buttonA.appendChild(buttonI);
      //   buttonA.innerHTML = '<i class="fas fa-plus-circle"></i>'
      //   priceButton.appendChild(buttonA);
      //   item.appendChild(priceButton);
      //   items.appendChild(item);
      // }
    } else {
      console.warn('request_error');
    }
  };

  xhr.open('GET', 'http://127.0.0.1:5000/produto/list');
  xhr.send();
}

getCategoryList(data => console.log("The data is:", data));
sleep(1000);
getItemList(dataItems => console.log("The data is:", dataItems));



