// var itemsJson;
// var itemsJsonCategoria;
var data;
var dataItems;
var categoryJson;

// window.onscroll = function () { myFunction() };

// function myFunction() {
//   var myElement = document.getElementsByClassName('item');
//   var topPos = myElement.offsetTop;
//   document.getElementsByClassName('items')[0].scrollTop = topPos;

//   var posArray = $('item').positionedOffset();
//   $('items').scrollTop = posArray[1];
// }

function move_up() {
  document.getElementsByClassName('items').scrollTop += 10;
}

function move_down() {
  document.getElementsByClassName('items').scrollTop -= 10;
}

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds) {
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
      itemJson.produtos.sort(function (a, b) {
        return a.idCategoria - b.idCategoria;
      }
      );
      for (var i = 0; i < categoryJson.Categorias.length; i++) {
        var items = document.getElementsByClassName("items")[0];
        var br = document.createElement('br');
        var objCategory = categoryJson.Categorias[i];
        var estacoes = document.createElement("div");
        estacoes.classList.add('estacoes')
        estacoes.innerHTML = '<i class="fas fa-tag fa-lg"></i>'
        var estacao = document.createElement("h1");
        estacao.classList.add("estacao");
        estacao.innerHTML = "Esta????o " + objCategory.categoria;
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
            buttonA.setAttribute("id",objItem.id);


            item.classList.add("item");


            // Adicionando a imagem ao item section principal
            imgDiv.classList.add('img-main');
            img.setAttribute("src", "img/" + objItem.img);
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
            buttonA.setAttribute( "onClick", "addProduct(this.id);");
            // buttonI.classList.add('fas fa-plus-circle');
            // buttonA.appendChild(buttonI);
            buttonA.innerHTML = '<i class="fas fa-plus-circle"></i>'
            priceButton.appendChild(buttonA);
            item.appendChild(priceButton);
            items.appendChild(item);
          }
        }
      }


    } else {
      console.warn('request_error');
    }
  };

  xhr.open('GET', 'http://127.0.0.1:5000/produto/list');
  xhr.send();
}

function addProduct(id){
  var teste;
  teste = 123;
};

getCategoryList(data => console.log("The data is:", data));
sleep(1000);
getItemList(dataItems => console.log("The data is:", dataItems));





