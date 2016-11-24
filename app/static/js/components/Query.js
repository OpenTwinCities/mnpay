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
             self.setState({max_page: res.body.max_page});
           })
  }

  render() {
    return (
      <div>
        <Control filters={this.state.filters} handleSubmit={this.filterChange.bind(this)}/>
        <Result data={this.state.data}/>
        <PageNav handlePageTransition={this.pageChange.bind(this)}
         page={this.state.page}
         max_page={this.state.max_page}
         num_buttons={7}/>
      </div>
    );
  }
}
