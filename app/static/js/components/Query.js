import React from "react";
import Request from "superagent";

import Result from "./Query/Result"
import Control from "./Query/Control"
import PageNav from "./Query/PageNav"

export default class Query extends React.Component {
  constructor () {
    super();
    this.state = {data: [], filters: {}, page: 1};
  }

  filterChange(filters) {
    this.setState({filters: filters, page: 1}, this.updateQuery)
  }

  pageChange(page_number) {
    this.setState({page: page_number}, this.updateQuery);
  }

  updateQuery () {
    var self = this;
    Request.get("/api/salaries")
           .query(self.state.filters)
           .query({page: self.state.page})
           .query({limit: 10})
           .end(function(err, res){
             self.setState({data: res.body.data});
             self.setState({next_page: res.body.next_page});
             self.setState({prev_page: res.body.prev_page});
           })
  }

  render() {
    return (
      <div>
        <Control filters={this.state.filters} handleSubmit={this.filterChange.bind(this)}/>
        <Result data={this.state.data}/>
        <PageNav handlePageTransition={this.pageChange.bind(this)} prev_page={this.state.prev_page} next_page={this.state.next_page}/>
      </div>
    );
  }
}
