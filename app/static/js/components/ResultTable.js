import React from "react";

export default class ResultTable extends React.Component {
  render() {
    var _data = this.props.data;
    console.log(_data);
    return (
      <table>
        <tbody>
          <tr>
            <th>First Name</th>
            <th>Middle Name</th>
            <th>Last Name</th>
            <th>Agency</th>
            <th>Dept</th>
            <th>Title</th>
            <th>Salary</th>
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
                        { object.wages }
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
