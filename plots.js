/**
 * Helper function to select stock data
 * Returns an array of values
 * @param {array} rows
 * @param {integer} index
 * index 0 - Date
 * index 1 - Open
 * index 2 - High
 * index 3 - Low
 * index 4 - Volume
 */
function unpack(rows, index) {
  return rows.map(function(row) {
    return row[index];
  });
}

// Submit Button handler
function handleSubmit() {
  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input value from the form
  var stock = d3.select("#neighborhood").node().value;
  //var stock = d3.select("#stockInput").property("value");
  console.log(d3.select("#neighborhood"));

  // clear the input value
  d3.select("#neighborhood").node().value = "";

  // Build the plot with the new stock
  buildPlot("Neighborhood");
}

function buildPlot(stock) {
  var apiKey = "LruxDFpgj8CyzmAamRDU";

  var url = `https://www.quandl.com/api/v3/datasets/WIKI/${stock}.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`;

  d3.json(url).then(function(data) {

    // Grab values from the response json object to build the plots
    var offensegroup = data.crime.offensegroup;
    var Neighborhood = data.crime.Neighborhood;
    var Year = data.crime.Year;
    var Method = data.crime.Method;
    var offense = data.crime.offense;

    var trace1 = {
      type: "scatter",
      mode: "lines",
      name: name,
      x: Year,
      y: closingPrices,
      line: {
        color: "#17BECF"
      }
    };

    var data = [trace1];

    var layout = {
      title: `${stock} closing prices`,
      xaxis: {
        range: [startDate, endDate],
        type: "date"
      },
      yaxis: {
        autorange: true,
        type: "linear"
      }
    };

    Plotly.newPlot("plot", data, layout);

  });
}

// Add event listener for submit button
d3.select("#submit").on("click", handleSubmit);
