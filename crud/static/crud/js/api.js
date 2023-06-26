
fetch('https://musicpro.bemtorres.win/api/v1/bodega/producto')
  .then(function(response) {
    if (response.ok) {
      return response.json();
    }
    throw new Error('Error en la respuesta de la API');
  })
  .then(function(data) {
    // Aquí puedes trabajar con la respuesta del servidor
    console.log(data);
  })
  .catch(function(error) {
    // Manejo de errores
    console.log(error);
  });


