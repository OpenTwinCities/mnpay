import React from "react";

export default class PageNavButton extends React.Component {

  handleClick (e) {
    this.props.handleClick(this.props.pageValue);
  }

  render () {
    var className;
    if (this.props.displayText === "Previous") {
      className = "previous";
    } else if (this.props.displayText === "Next") {
      className = "next";
    }
    return (
      <li className={className} onClick={this.handleClick.bind(this)}>
        <a>{this.props.displayText}</a>
      </li>
    );
  }
}
PageNavButton.propTypes = {
  displayText: React.PropTypes.string.isRequired,
  handleClick: React.PropTypes.func.isRequired,
  pageValue: React.PropTypes.number.isRequired
};
