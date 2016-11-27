import React from "react";

import Numeral from "numeral"

export default class ResultTable extends React.Component {
  render() {
    var _data = this.props.data;
    return (
      <table className="table">
        <tbody>
          <tr>
            <th>First Name</th>
            <th>Middle Name</th>
            <th>Last Name</th>
            <th>Agency</th>
            <th>Dept</th>
            <th>Title</th>
            <th>Wages</th>
            <th>Year</th>
          </tr>
          {_data.map(function(object, i){
             return <tr key={i}>
                      <td>
                        { object.first_name }
                      </td>
                      <td>
                        { object.middle_name }
                      </td>
                      <td>
                        { object.last_name }
                      </td>
                      <td>
                        { object.agency }
                      </td>
                      <td>
                        { object.dept }
                      </td>
                      <td>
                        { object.title }
                      </td>
                      <td>
                        { "$" + Numeral(object.wages).format("0,0.00") }
                      </td>
                      <td>
                        { object.year }
                      </td>
                    </tr>;
           })}
        </tbody>
      </table>
    );
  }
}
