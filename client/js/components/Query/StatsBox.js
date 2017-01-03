import React from "react";

import DistChart from "./StatsBox/DistChart";
import { Modal, Button } from 'react-bootstrap';

export default class StatsBox extends React.Component {

  render() {

    return (
      <div>
        <Modal show={this.props.show}
               onHide={this.props.onClose}
               bsSize="large" >
          <Modal.Header closeButton>
            <Modal.Title>Salary Distribution</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <DistChart data={this.props.data} />
          </Modal.Body>
        </Modal>
      </div>
    );
  }
}
