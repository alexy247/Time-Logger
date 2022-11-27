const headers = new Headers();
headers.append('Accept', 'application/json');

const requestHeaders = {
  method: 'GET',
  headers: headers,
  mode: 'cors',
  cache: 'default'
};

const request = new Request('http://localhost:3000/day_stat', requestHeaders);

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
    average_per_day = response.average_per_day;
    average_per_week = response.average_per_week;
    data_stat = response.data_stat;

    let labels = [];
    let data = [];
    let average_per_day_list = [];
    let average_per_week_list = [];
    for (line in data_stat) {
        labels.push(line);
        time = data_stat[line].split('.');
        hours = new Number(time[0]);
        minutes = new Number(time[1]);
        data.push(hours + new Number((minutes / 60).toFixed(2)));
        average_per_day_list.push(average_per_day);
        average_per_week_list.push(average_per_week);
    }

    new Chart(chartPlaceElement, {
      data: {
        datasets: [{
          type: 'bar',
          label: 'Working hours',
          data: data,
          borderWidth: 1
      }, {
          type: 'line',
          label: 'Avarage of day per day',
          data: average_per_day_list,
      }, {
        type: 'line',
        label: 'Avarage of day per week',
        data: average_per_week_list,
      }],
        labels: labels
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