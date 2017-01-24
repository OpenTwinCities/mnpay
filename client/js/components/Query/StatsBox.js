import React from "react";

import DistChart from "./StatsBox/DistChart";
import { Modal } from 'react-bootstrap';

export default class StatsBox extends React.Component {
  constructor () {
    super();
    this.state = {
      buckets: 25
    };
  }

  handleChange (e) {
    this.setState({ buckets: parseInt(e.target.value, 10) });
  }

  render () {
    return (
      <div>
        <Modal show={this.props.show}
               onHide={this.props.onClose}
               bsSize="large" >
          <Modal.Header closeButton>
            <Modal.Title>Salary Distribution</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <form className="form-inline">
              <div className="form-group col-sm-offset-1">
                <select id="buckets" className="form-control"
                    value={this.state.buckets} onChange={this.handleChange.bind(this)}>
                  <option value="25">25</option>
                  <option value="50">50</option>
                  <option value="75">75</option>
                  <option value="100">100</option>
                </select>
                <label htmlFor="buckets">&nbsp;Buckets</label>
              </div>
            </form>
            <DistChart data={this.props.data} buckets={this.state.buckets} />
          </Modal.Body>
        </Modal>
      </div>
    );
  }
}
StatsBox.propTypes = {
  data: React.PropTypes.array.isRequired,
  onClose: React.PropTypes.func.isRequired,
  show: React.PropTypes.bool.isRequired
};
