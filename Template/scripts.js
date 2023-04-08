fetch("data.json")
   .then(function (res) {
      return res.json();
   })
   .then(function (datas) {
      let placholder = document.querySelector("#data-output");
      let out = ""
      for (let data of datas) {
         out += `
            <tr>
                <td>${data.name}</td>
                <td>${data.price}</td>
                <td>${data.change}</td>
                <td>${data.persentchange}</td>
                <td>${data.img}</td>
            </tr>
        `
      }

      placholder.innerHTML = out;
   })