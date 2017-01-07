import React from "react";

export default class Control extends React.Component {
  constructor () {
    super();
    this.state = {
      first_name: "",
      last_name: "",
      agency: "",
      dept: "",
      title: "",
      sortby: "wage",
      direction: "desc"
    };
  }

  onChange (e) {
    this.setState({ [e.target.id]: e.target.value });
  }

  handleSubmit (e) {
    var filters = {
      first_name: this.state.first_name,
      last_name: this.state.last_name,
      agency: this.state.agency,
      dept: this.state.dept,
      title: this.state.title,
      sortby: this.state.sortby,
      direction: this.state.direction
    };
    Object.keys(filters).forEach(function (key) {
      if (filters[key] === "") {
        delete filters[key];
      }
    });
    this.props.handleSubmit(filters);
  }

  handleClear (e) {
    this.setState({
      first_name: "",
      last_name: "",
      agency: "",
      dept: "",
      title: "",
      sortby: "wage",
      direction: "desc"
    }, this.handleSubmit);
  }

  handleKeyPress (e) {
    if (e.key === 'Enter') {
      this.handleSubmit(e);
    }
  }


  render () {
    return (
      <form className="form-horizontal" onKeyPress={this.handleKeyPress.bind(this)} method="get">
        <div className="form-group">
          <div className="col-xs-6 col-sm-4">
            <label htmlFor="first_name">First name:</label>
            <input type="text" className="form-control" id="first_name" name="first_name"
                onChange={this.onChange.bind(this)} value={this.state.first_name}/>
          </div>
          <div className="col-xs-6 col-sm-4">
            <label htmlFor="last_name">Last name:</label>
            <input type="text" className="form-control" id="last_name" name="last_name"
                onChange={this.onChange.bind(this)} value={this.state.last_name}/>
          </div>
          <div className="col-sm-4">
            <label htmlFor="title">Title:</label>
            <input type="text" className="form-control" id="title" name="title"
                onChange={this.onChange.bind(this)} value={this.state.title}/>
          </div>
        </div>
        <div className="form-group">
          <div className="col-sm-4">
            <label htmlFor="agency">Agency:</label>
            <input type="text" className="form-control" id="agency" name="agency"
                onChange={this.onChange.bind(this)} value={this.state.agency}/>
          </div>
          <div className="col-sm-4">
            <label htmlFor="dept">Dept:</label>
            <input type="text" className="form-control" id="dept" name="dept"
                onChange={this.onChange.bind(this)} value={this.state.dept}/>
          </div>
          <div className="col-xs-6 col-sm-2">
            <label htmlFor="sortby">Order by:</label>
            <select className="form-control" id="sortby" value={this.state.sortby} onChange={this.onChange.bind(this)}>
              <option value="first_name">First name</option>
              <option value="last_name">Last name</option>
              <option value="agency">Agency</option>
              <option value="dept">Dept</option>
              <option value="title">Title</option>
              <option value="wage">Wage</option>
              <option value="year">Year</option>
            </select>
          </div>
          <div className="col-xs-6 col-sm-2">
            <label htmlFor="direction">Direction:</label>
            <select className="form-control" id="direction"
                value={this.state.direction} onChange={this.onChange.bind(this)}>
              <option value="asc">Ascending</option>
              <option value="desc">Descending</option>
            </select>
          </div>
        </div>
        <div className="form-group">
          <div className="col-xs-6 col-sm-4 button-wrapper">
            <button type="button" className="btn btn-primary btn-lg btn-block"
                onClick={this.handleSubmit.bind(this)}>Search</button>
          </div>
          <div className="col-xs-3 col-sm-2 button-wrapper">
            <button type="button" className="btn btn-info btn-lg btn-block"
                onClick={this.props.showPlot}>
            <div className="hidden-xs">
              Plot <span className="glyphicon glyphicon-align-left" />
            </div>
            <div className="visible-xs">
              Plot
            </div>
            </button>
          </div>
          <div className="col-xs-3 col-sm-2 col-sm-offset-4">
            <button type="button" className="btn btn-warning btn-lg btn-block"
                onClick={this.handleClear.bind(this)}>Clear</button>
          </div>
        </div>
      </form>
    );
  }
}
Control.propTypes = {
  handleSubmit: React.PropTypes.function.required,
  showPlot: React.PropTypes.function.required
};
