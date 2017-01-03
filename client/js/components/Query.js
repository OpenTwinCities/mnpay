import React from "react";
import Request from "superagent";

import Result from "./Query/Result"
import Control from "./Query/Control"
import PageNav from "./Query/PageNav"
import StatsBox from "./Query/StatsBox"

export default class Query extends React.Component {
  constructor ({location: { query }}) {
    super();
    this.state = {data: [],
                  filters: query,
                  stats: [],
                  showPlot: false};
  }

  filterChange(filters) {
    var params = Object.assign(filters, {page: 1});
    this.props.router.push({query: params});
    this.setState({filters: params}, this.updateQuery);
  }

  showPlot() {
    this.setState({showPlot: true});
  }

  hidePlot() {
    this.setState({showPlot: false});
  }

  pageChange(page_number) {
    var params = Object.assign(this.state.filters, {page: page_number});
    this.props.router.push({query: params});
    this.setState({filters: params}, this.updateQuery);
  }

  componentDidMount () {
    this.updateQuery();
  }

  componentWillReceiveProps({location: { query }}) {
    this.setState({filters: query}, this.updateQuery)
  }

  updateQuery () {
    var self = this;
    Request.get("/api/wages")
           .query(self.state.filters)
           .query({limit: 10})
           .end(function(err, res){
             self.setState({data: res.body.data});
             var cur_page = parseInt(res.body.cur_page);
             var last_page = parseInt(res.body.last_page);
             if (cur_page > 1) {
               self.setState({prev_page: cur_page - 1});
             }
             else {
               self.setState({prev_page: null});
             }
             if (cur_page != last_page) {
               self.setState({next_page: cur_page + 1});
             }
             else {
               self.setState({next_page: null});
             }
           })
     Request.get("/api/stats")
            .query(self.state.filters)
            .end(function(err, res){
              self.setState({stats: res.body.hist});
            })
  }

  render() {
    return (
      <div>
        <Control filters={this.state.filters}
                 handleSubmit={this.filterChange.bind(this)}
                 showPlot={this.showPlot.bind(this)}/>
        <Result data={this.state.data}/>
        <StatsBox data={this.state.stats}
                  onClose={this.hidePlot.bind(this)}
                  show={this.state.showPlot}/>
        <PageNav handlePageTransition={this.pageChange.bind(this)} prev_page={this.state.prev_page} next_page={this.state.next_page}/>
      </div>
    );
  }
}
