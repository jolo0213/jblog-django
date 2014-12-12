var sample = '/static/';

var width = 500,
    height = 500,
    radius = Math.min(width, height) / 2;

var color = d3.scale.ordinal()
    .range(["#5E2D79",'#72587F','#694489','#754C78','#5C246E']);

var arc = d3.svg.arc()
    .outerRadius(radius - 25)
    .innerRadius(radius - 125);

var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) { return d.atk; });

var svg = d3.select("center").append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g")
    .attr('class','padchart')
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

d3.csv(sample + "samples/pad.csv", function(error, data) {

  data.forEach(function(d) {
    d.atk = +d.atk;
  });

  var total = d3.sum(data.map(function(d) {
    return d.atk
  }));

  var g = svg.selectAll(".arc")
      .data(pie(data))
    .enter().append("g")
      .attr("class", "arc");

  var padchart = d3.select('.padchart')

  padchart.append('text')
    .style('text-anchor','middle')
    .attr('class','secondary')
    .attr('dy','-2em')
    .text('Total ATK')

  padchart.append('text')
    .style('text-anchor','middle')
    .attr('class','primary')
    .attr('dy','.4em')
    .text(total)    

  g.append("path")
      .attr("d", arc)
      .style("fill", function(d) { return color(d.data.monster); });

  path = svg.selectAll('path')

  path.on('mouseover', function(d) {
    d3.select('.primary').text(d.data.atk);
    d3.select('.secondary').text(d.data.monster);
  });

  path.on('mouseout', function(d) {
    d3.select('.primary').text(total);
    d3.select('.secondary').text('Total ATK');
  });
});
