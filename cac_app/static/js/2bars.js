$(function () {
   var data = {
      //labels: ["January", "February", "March", "April", "May", "June", "July"],
      labels: {{2bars.labels}},
      datasets: [
          {
              label: "My First dataset",
              fillColor: "rgba(220,220,220,0.5)",
              strokeColor: "rgba(220,220,220,0.8)",
              highlightFill: "rgba(220,220,220,0.75)",
              highlightStroke: "rgba(220,220,220,1)",
              data: {{2bars.data1}}
          },
          {
              label: "My Second dataset",
              fillColor: "rgba(151,187,205,0.5)",
              strokeColor: "rgba(151,187,205,0.8)",
              highlightFill: "rgba(151,187,205,0.75)",
              highlightStroke: "rgba(151,187,205,1)",
              data: {{2bars.data2}}
          }
    ]
    };
   
    var option = {
    responsive: true,
    };
   
    // Get the context of the canvas element we want to select
    var ctx = document.getElementById("2bars").getContext('2d');
    var myBarChart = new Chart(ctx).Bar(data, option); //'Line' defines type of the chart.
});