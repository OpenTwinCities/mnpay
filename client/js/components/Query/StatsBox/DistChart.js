import React from "react";

import Numeral from "numeral";
import { BarChart, XAxis, YAxis, Bar, CartesianGrid, ResponsiveContainer } from "recharts";

export default class DistChart extends React.Component {

  formatTick (value) {
    var numeralValue = new Numeral(value);
    return "$" + numeralValue.format("0,0");
  }

  findBoundaries () {
    var i;
    var minVal = Infinity;
    var maxVal = 0;
    var data = this.props.data;
    for (i = 0; i < data.length; i++) {
      if (data[i] < minVal) {
        minVal = data[i];
      }
      if (data[i] > maxVal) {
        maxVal = data[i];
      }
    }
    return { minVal: minVal, maxVal: maxVal };
  }

  render () {
    var boundaries = this.findBoundaries();

    var minVal = boundaries.minVal;
    var maxVal = boundaries.maxVal;
    var buckets = this.props.buckets;
    var data = this.props.data;

    var minDisplay = Math.max(Math.floor(minVal / 10000) * 10000 - 10000, 0);
    var maxDisplay = Math.ceil(maxVal / 10000) * 10000 + 10000;
    var bucketSize = Math.ceil((maxVal - minVal) / buckets);
    var histData = [];
    var midpoint;
    var i;

    for (i = 0; i < buckets; i++) {
      midpoint = minVal + (i + 0.5) * bucketSize;
      histData.push({ x: midpoint, y: 0 });
    }

    for (i = 0; i < data.length; i++) {
      histData[Math.floor((data[i] - minVal) / bucketSize)].y++;
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
  buckets: React.PropTypes.number.isRequired,
  data: React.PropTypes.array.isRequired
};
