import React from "react";

import Numeral from "numeral";

export default class ResultTable extends React.Component {
  render () {
    var _data = this.props.data;
    return (
      <div className="table-responsive">
        <table className="table ">
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
            {_data.map(function (object, i) {
              object.numeral_wage = new Numeral(object.wage);
              return (<tr key={i}>
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
                          { "$" + object.numeral_wage.format("0,0.00") }
                        </td>
                        <td>
                          { object.year }
                        </td>
                      </tr>);
            })}
          </tbody>
        </table>
      </div>
    );
  }
}
ResultTable.propTypes = {
  data: React.PropTypes.array.required
};
