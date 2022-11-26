const headers = new Headers();
headers.append('Accept', 'application/json');

const requestHeaders = {
  method: 'GET',
  headers: headers,
  mode: 'cors',
  cache: 'default'
};

const request = new Request('http://localhost:3000/day_stat', requestHeaders);

const dataPlaceElement = document.querySelector('.js-data-place');
const chartPlaceElement = document.querySelector('.js-chart-place');

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

    console.log(typeof response);

    let labels = [];
    let data = [];
    for (line in response) {
        labels.push(line);
        time = response[line].split('.');
        hours = new Number(time[0]);
        minutes = new Number(time[1]);
        data.push(hours + new Number((minutes / 60).toFixed(2)));
    }

    new Chart(chartPlaceElement, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'working hours',
          data: data,
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });

    console.debug(response);
  }).catch((error) => {
    console.error(error);
  });