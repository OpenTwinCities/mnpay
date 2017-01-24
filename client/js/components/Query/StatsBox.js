import React from "react";

import DistChart from "./StatsBox/DistChart";
import { Modal } from 'react-bootstrap';

export default class StatsBox extends React.Component {

  handleChange (event) {
    this.render();
  }

  render () {
    return (
      <div>
        <Modal show={this.props.show}
               onHide={this.props.onClose}
               bsSize="large" >
          <Modal.Header closeButton>
            <Modal.Title>Salary Distribution</Modal.Title>
            <select value={this.props.buckets} onChange={this.handleChange}>
              <option value="20">20</option>
              <option value="50">50</option>
              <option value="100">100</option>
            </select>
          </Modal.Header>
          <Modal.Body>
            <DistChart data={this.props.data} />
          </Modal.Body>
        </Modal>
      </div>
    );
  }
}
StatsBox.propTypes = {
  buckets: React.PropTypes.number,
  data: React.PropTypes.array.isRequired,
  onClose: React.PropTypes.func.isRequired,
  show: React.PropTypes.bool.isRequired
};
