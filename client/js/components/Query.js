import React from "react";
import Request from "superagent";
import Promise from "bluebird";
import objectAssign from "object-assign";

import Result from "./Query/Result";
import Control from "./Query/Control";
import PageNav from "./Query/PageNav";
import StatsBox from "./Query/StatsBox";

export default class Query extends React.Component {
  constructor ({ location: { query } }) {
    super();
    this.state = {
      wages: [],
      filters: query,
      wageList: [],
      canPlot: false
    };
  }

  componentDidMount () {
      this.updateQuery();
  }

  componentWillReceiveProps ({ location: { query } }) {
    this.setState({ filters: query }, this.updateQuery);
  }

  filterChange (filters) {
    var params = objectAssign(filters, { page: 1 });
    this.props.router.push({ query: params });
    this.setState({ filters: params }, this.updateQuery);
  }

  pageChange (pageNumber) {
    var params = objectAssign(this.state.filters, { page: pageNumber });
    this.props.router.push({ query: params });
    this.setState({ filters: params }, this.updateQuery);
  }

  updateQuery () {
    var self = this;
    self.setState({ stats: [] });
    Request.get("/api/wages")
           .query(self.state.filters)
           .end(function (err, res) {
             if (res.statusText === "OK") {
               var data = res.body;
               var newState = {};
               newState["wages"] = data.results;
               newState["total"] = data.count;
               newState["nextPage"] = data.next;
               newState["prevPage"] = data.previous;
               self.setState(newState);
             }
           });
  }

  render () {
    return (
      <div>
        <Control filters={this.state.filters}
                 handleSubmit={this.filterChange.bind(this)}
                 allowPlot={this.state.canPlot}/>
        <Result data={this.state.wages}/>
        <PageNav handlePageTransition={this.pageChange.bind(this)}
                 prev_page={this.state.prevPage}
                 next_page={this.state.nextPage}/>
      </div>
    );
  }
}
Query.propTypes = {
  router: React.PropTypes.objectOf(React.PropTypes.any).isRequired
};
