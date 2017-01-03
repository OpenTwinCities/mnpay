import React from "react";

import Numeral from "numeral";
import {BarChart, XAxis, YAxis, Bar, CartesianGrid, Tooltip, ResponsiveContainer} from "recharts";

export default class DistChart extends React.Component {

  formatTick(value) {
    return Numeral(value).format("0,0")
  }

  render() {
    var data = this.props.data.map(function(object, i){
      var midpoint = (object.upper + object.lower)/2;
      midpoint = Number(midpoint.toFixed(2));
      return { x: midpoint, y: object.count}
    })
    return <ResponsiveContainer height={300}>
             <BarChart data={data}>
               <XAxis dataKey="x"
                      tickCount={10}
                      type="number"
                      domain={[0, 'dataMax']}
                      tickFormatter={this.formatTick}/>
               <Bar dataKey="y"
                     fill="#82ca9d"/>
               <CartesianGrid strokeDasharray="3 3" />
               <YAxis />
             </BarChart>
           </ResponsiveContainer>
  }
}
