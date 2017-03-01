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
      showPlot: false,
      canPlot: false
    };
  }

  componentDidMount () {
    this.getLimits()
      .then(this.updateQuery.bind(this));
  }

  componentWillReceiveProps ({ location: { query } }) {
    this.setState({ filters: query }, this.updateQuery);
  }

  filterChange (filters) {
    var params = objectAssign(filters, { page: 1 });
    this.props.router.push({ query: params });
    this.setState({ filters: params }, this.updateQuery);
  }

  getLimits () {
    var self = this;
    return new Promise(function (resolve, reject) {
      Request.get("/api/limits")
             .end(function (err, res) {
               if (res.body.status === "Okay") {
                 var limits = res.body.data;
                 self.setState({
                   queryLimit: limits.query_size_limit,
                   statsLimit: limits.stats_limit
                 });
               }
               resolve();
             });
    });
  }

  showPlot () {
    var self = this;
    self.setState({ showPlot: true });
    if (self.state.wageList.length === 0) {
      Request.get("/api/wage_list")
             .query(self.state.filters)
             .end(function (err, res) {
               if (res.body.status === "Okay") {
                 self.setState({ wageList: res.body.data.wages });
               }
             });
    }
  }

  hidePlot () {
    this.setState({ showPlot: false });
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
           .query({ limit: 10 })
           .end(function (err, res) {
             if (res.body.status === "Okay") {
               var data = res.body.data;
               var newState = {};
               newState["wages"] = data.wages;
               newState["total"] = data.total_results;
               var curPage = parseInt(data.cur_page, 10);
               var lastPage = parseInt(data.last_page, 10);
               if (curPage > 1) {
                 newState["prevPage"] = curPage - 1;
               } else {
                 newState["prevPage"] = null;
               }
               if (curPage !== lastPage) {
                 newState["nextPage"] = curPage + 1;
               } else {
                 newState["nextPage"] = null;
               }
               newState["canPlot"] = data.total_results < self.state.statsLimit;
               self.setState(newState);
             }
           });
  }

  render () {
    return (
      <div>
        <Control filters={this.state.filters}
                 handleSubmit={this.filterChange.bind(this)}
                 showPlot={this.showPlot.bind(this)}
                 allowPlot={this.state.canPlot}/>
        <Result data={this.state.wages}/>
        <StatsBox data={this.state.wageList}
                  onClose={this.hidePlot.bind(this)}
                  show={this.state.showPlot}/>
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
