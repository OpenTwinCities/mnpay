import React from "react";

import ResultTable from "./ResultTable"

export default class Layout extends React.Component {
  constructor () {
    super()
    this.state = {data: []}
  }

  componentDidMount () {
    fetch("http://localhost:5000/api/salaries")
      .then( (response) => {
        return response.json()} )
          .then( (json) => {
            this.setState({data: json["data"]})
          })
  }

  render() {
    return (
        <ResultTable data={this.state.data}/>
    );
  }
}
