const headers = new Headers();
headers.append('Accept', 'application/json');

const requestHeaders = {
  method: 'GET',
  headers: headers,
  mode: 'cors',
  cache: 'default'
};

const request = new Request('http://localhost:3000', requestHeaders);

const dataPlaceElement = document.querySelector('.js-data-place');

fetch(request)
  .then((response) => {
    if (response.status === 200) {
      return response.json();
    } else {
      throw new Error('Something went wrong on API server!');
    }
  })
  .then((response) => {
    dataPlaceElement.innerHTML = JSON.stringify(response);
    console.debug(response);
  }).catch((error) => {
    console.error(error);
  });