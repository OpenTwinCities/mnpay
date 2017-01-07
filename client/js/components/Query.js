import React from "react";
import Request from "superagent";

import Result from "./Query/Result";
import Control from "./Query/Control";
import PageNav from "./Query/PageNav";
import StatsBox from "./Query/StatsBox";

export default class Query extends React.Component {
  constructor ({ location: { query } }) {
    super();
    this.state = {
      data: [],
      filters: query,
      stats: [],
      showPlot: false
    };
  }

  componentDidMount () {
    this.updateQuery();
  }

  componentWillReceiveProps ({ location: { query } }) {
    this.setState({ filters: query }, this.updateQuery);
  }

  filterChange (filters) {
    var params = Object.assign(filters, { page: 1 });
    this.props.router.push({ query: params });
    this.setState({ filters: params }, this.updateQuery);
  }

  showPlot () {
    var self = this;
    self.setState({ showPlot: true });
    if (self.state.stats.length === 0) {
      Request.get("/api/stats")
             .query(self.state.filters)
             .end(function (err, res) {
               self.setState({ stats: res.body.hist });
             });
    }
  }

  hidePlot () {
    this.setState({ showPlot: false });
  }

  pageChange (pageNumber) {
    var params = Object.assign(this.state.filters, { page: pageNumber });
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
             self.setState({ data: res.body.data });
             var curPage = parseInt(res.body.cur_page, 10);
             var lastPage = parseInt(res.body.last_page, 10);
             if (curPage > 1) {
               self.setState({ prev_page: curPage - 1 });
             } else {
               self.setState({ prev_page: null });
             }
             if (curPage !== lastPage) {
               self.setState({ next_page: curPage + 1 });
             } else {
               self.setState({ next_page: null });
             }
           });
  }

  render () {
    return (
      <div>
        <Control filters={this.state.filters}
                 handleSubmit={this.filterChange.bind(this)}
                 showPlot={this.showPlot.bind(this)}/>
        <Result data={this.state.data}/>
        <StatsBox data={this.state.stats}
                  onClose={this.hidePlot.bind(this)}
                  show={this.state.showPlot}/>
        <PageNav handlePageTransition={this.pageChange.bind(this)}
                 prev_page={this.state.prev_page}
                 next_page={this.state.next_page}/>
      </div>
    );
  }
}
Query.propTypes = {
  router: React.PropTypes.objectOf(React.PropTypes.any).isRequired
};
