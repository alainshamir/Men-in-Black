
  
// Plot the default route once the page loads
var defaultURL = "/Robbery";
  d3.json(defaultURL).then(function(data){
  // d3.json(defaultURL),function(data){
  graphdatax=[];
  graphdatay=[];

  for(i=0;i<data.length;i++){
     graphdatax.push(data[i][1]);
     graphdatay.push(data[i][2]);
   }
  var data = [{
    x: graphdatax,
    y:graphdatay,
    type: 'scatter'
  }];
  
  var layout = {
    title: 'Robbery',
    xaxis: {
      title: 'Year',
      showgrid: false,
      zeroline: false
    },
    yaxis: {
      title: 'Count',
      showline: false
    }
  };
  Plotly.newPlot("bar", data, layout);
  
 })

// Update the plot with new data
function updatePlotly(newdata) {
  console.log(newdata[0],newdata[1]);
  graphdatax=[];
  graphdatay=[];
  for(i=0;i<newdata.length;i++){
    graphdatax.push(newdata[i][1]);
    graphdatay.push(newdata[i][2]);
  }
  var data = [{
    x: graphdatax,
    y:graphdatay,
    type: 'scatter'
  }];
  var selDataset_ddl = document.getElementById("selDataset");
  var plotTitle = selDataset_ddl.options[selDataset_ddl.selectedIndex].text;
  var layout = {
    title: plotTitle,
    xaxis: {
      title: 'Year',
      showgrid: false,
      zeroline: false
    },
    yaxis: {
      title: 'Count',
      showline: false
    }
  };
  //Plotly.restyle("bar", "x", graphdatax);
  //Plotly.restyle("bar", "y", graphdatay);
  
  Plotly.newPlot("bar", data, layout);
}
// Plot the default route once the page loads

// Get new data whenever the dropdown selection changes
function getData(route) {
  console.log(route);
  d3.json(route,function(data) {
    console.log("newdata", data);
    console.log(data);
    updatePlotly(data);
  });
}
