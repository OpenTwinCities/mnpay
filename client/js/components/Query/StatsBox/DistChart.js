import React from "react";

import Numeral from "numeral";
import { BarChart, XAxis, YAxis, Bar, CartesianGrid, ResponsiveContainer } from "recharts";

export default class DistChart extends React.Component {

  formatTick (value) {
    var numeralValue = new Numeral(value);
    return "$" + numeralValue.format("0,0");
  }

  render () {
    var BUCKETS = this.props.buckets || 20;
    var histData = [];
    var i;
    for (i = 0; i < BUCKETS; i++) {
      histData.push(0);
    }

    var minVal = Infinity;
    var maxVal = 0;
    var data = this.props.data;
    console.log(this.props.data);
    for (i = 0; i < data.length; i++) {
      if (data[i] < minVal) {
        minVal = data[i];
      }
      if (data[i] > maxVal) {
        maxVal = data[i];
      }
    }

    var minDisplay = Math.max(Math.floor(minVal / 10000) * 10000 - 10000, 0);
    var maxDisplay = Math.ceil(maxVal / 10000) * 10000 + 10000;
    var bucketSize = (maxVal - minVal) / BUCKETS;

    for (i = 0; i < data.length; i++) {
      histData[Math.floor((data[i] - minVal) / bucketSize)]++;
    }

    for (i = 0; i < histData.length; i++) {
      var midpoint = minVal + (i + 0.5) * bucketSize;
      histData[i] = { x: midpoint, y: histData[i] };
    }

    return (<ResponsiveContainer height={300}>
             <BarChart data={histData}>
               <XAxis dataKey="x"
                      tickCount={10}
                      type="number"
                      domain={[minDisplay, maxDisplay]}
                      tickFormatter={this.formatTick}/>
               <Bar dataKey="y"
                     fill="#82ca9d"/>
               <CartesianGrid strokeDasharray="3 3" />
               <YAxis />
             </BarChart>
           </ResponsiveContainer>);
  }
}
DistChart.propTypes = {
  buckets: React.PropTypes.number,
  data: React.PropTypes.array.isRequired
};
