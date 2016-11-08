import React from "react";

export default class Control extends React.Component {
  constructor () {
    super()
    this.state = {first_name: "",
                  last_name: "",
                  agency: "",
                  dept: "",
                  title: "",
                  sortby: "wages",
                  direction: "desc"
                }
  }

  on_first_name_change(e){
    this.setState({first_name: e.target.value})
  }

  on_last_name_change(e){
    this.setState({last_name: e.target.value})
  }

  on_agency_change(e){
    this.setState({agency: e.target.value})
  }

  on_dept_change(e){
    this.setState({dept: e.target.value})
  }

  on_title_change(e){
    this.setState({title: e.target.value})
  }

  on_sortby_change(e){
    this.setState({sortby: e.target.value})
  }

  on_direction_change(e){
    this.setState({direction: e.target.value})
  }

  componentDidMount () {
    this.handleSubmit();
  }

  handleSubmit(e){
    var filters = {
      first_name: this.state.first_name,
      last_name: this.state.last_name,
      agency: this.state.agency,
      dept: this.state.dept,
      title: this.state.title,
      sortby: this.state.sortby,
      direction: this.state.direction
    };
    this.props.handleSubmit(filters);
  }

  _handleKeyPress(e){
    if (e.key === 'Enter') {
      this.handleSubmit(e)
    }
  }


  render() {
    return (
      <form className="form-horizontal" onKeyPress={this._handleKeyPress.bind(this)} method="get">
        <div className="form-group">
          <label className="control-label col-sm-2">First name:</label>
          <div className="col-sm-5">
            <input type="text" className="form-control" onChange={ this.on_first_name_change.bind(this) } name="first_name" value={ this.state.first_name }/>
          </div>
        </div>
        <div className="form-group">
          <label className="control-label col-sm-2">Last name:</label>
          <div className="col-sm-5">
            <input type="text" className="form-control" name="last_name" onChange={ this.on_last_name_change.bind(this)} value={ this.state.last_name }/>
          </div>
        </div>
        <div className="form-group">
          <label className="control-label col-sm-2">Agency:</label>
          <div className="col-sm-5">
            <input type="text" className="form-control" name="agency" onChange={ this.on_agency_change.bind(this)} value={ this.state.agency }/>
          </div>
        </div>
        <div className="form-group">
          <label className="control-label col-sm-2">Dept:</label>
          <div className="col-sm-5">
            <input type="text" className="form-control" name="dept" onChange={ this.on_dept_change.bind(this)} value={ this.state.dept }/>
          </div>
        </div>
        <div className="form-group">
          <label className="control-label col-sm-2">Title:</label>
          <div className="col-sm-5">
            <input type="text" className="form-control" name="title" onChange={ this.on_title_change.bind(this)} value={ this.state.title }/>
          </div>
        </div>
        <div className="form-group">
          <label className="control-label col-sm-2">Order by:</label>
          <div className="col-sm-5">
            <select className="form-control" value={this.state.sortby} onChange={this.on_sortby_change.bind(this)}>
              <option value="first_name">First name</option>
              <option value="last_name">Last name</option>
              <option value="agency">Agency</option>
              <option value="dept">Dept</option>
              <option value="title">Title</option>
              <option value="wages">Wages</option>
            </select>
          </div>
        </div>
        <div className="form-group">
          <label className="control-label col-sm-2">Direction:</label>
          <div className="col-sm-5">
            <select className="form-control" value={this.state.direction} onChange={this.on_direction_change.bind(this)}>
              <option value="asc">Ascending</option>
              <option value="desc">Descending</option>
            </select>
          </div>
        </div>
        <div className="form-group">
          <div className="col-sm-5 col-sm-offset-2">
            <button type="button" className="btn btn-primary btn-lg btn-block" onClick={ this.handleSubmit.bind(this) }>Submit</button>
          </div>
        </div>
      </form>
    );
  }
}
